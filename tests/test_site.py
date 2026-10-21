"""Automatic checks for the Money Decoded site (scam check + guides).

Run (no Claude needed):
    C:\\FutureLiving\\studio\\.venv\\Scripts\\python.exe tests/test_site.py
Serves the folder on a local port, drives Chromium with Playwright and prints PASS/FAIL per check.
Exit code 1 if any check fails.
"""
import functools
import http.server
import pathlib
import re
import sys
import threading

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))
    print(("PASS " if cond else "FAIL ") + name + (f"  ({detail})" if detail and not cond else ""))


def serve():
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    handler = functools.partial(Quiet, directory=str(ROOT))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}/"


def fresh(page):
    if page.is_visible("#again"):
        page.click("#again")
    else:
        page.reload()


def answer_all(page, value, overrides=None):
    overrides = overrides or {}
    for i in range(10):
        page.click(f"input[name=q{i}][value={overrides.get(i, value)}] + span")


def static_security_checks():
    """README promise: the site sends no data anywhere. Enforced on the files, no browser needed."""
    pages = sorted(ROOT.rglob("*.html"))
    check("security: 12 pages found", len(pages) == 12, str(len(pages)))
    for p in pages:
        name = p.relative_to(ROOT).as_posix()
        html = p.read_text(encoding="utf-8")
        check(f"security: CSP meta: {name}", 'http-equiv="Content-Security-Policy"' in html)
        check(f"security: no external <script src>: {name}", not re.search(r"<script[^>]*\ssrc=", html, re.I))
        check(f"security: no fetch/XHR/sendBeacon: {name}",
              not re.search(r"\bfetch\s*\(|XMLHttpRequest|sendBeacon|WebSocket\(", html))
        check(f"security: no <form action>: {name}", not re.search(r"<form[^>]*\saction=", html, re.I))
        check(f"security: no <iframe>/<object>/<embed>: {name}", not re.search(r"<(iframe|object|embed)\b", html, re.I))
        check(f"security: no third-party stylesheet/font/image: {name}",
              not re.search(r"<img[^>]*\ssrc=\"(https?:)?//", html, re.I)
              and not re.search(r"<link[^>]*rel=\"(stylesheet|preload|prefetch|modulepreload|icon)\"[^>]*href=\"(https?:)?//", html, re.I)
              and not re.search(r"@import\s+(url\()?[\"']?(https?:)?//", html, re.I))
        blank = re.findall(r"<a\b[^>]*target=\"_blank\"[^>]*>", html, re.I)
        check(f"security: target=_blank links carry rel=noopener: {name}",
              all(re.search(r"rel=\"[^\"]*noopener", a) for a in blank), f"{len(blank)} links")


def main():
    static_security_checks()
    srv, base = serve()
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge")  # uses installed Edge, no download
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(base)

        check("home: 10 questions", page.locator(".q").count() == 10)
        check("home: button disabled before answering", page.is_disabled("button.cta"))
        answer_all(page, "no", {0: "yes"})
        check("home: button enabled after 10 answers", page.is_enabled("button.cta"))
        check("home: progress says 10 of 10", "10 of 10" in page.inner_text("#progress"))

        # all "no" -> few red flags
        fresh(page); answer_all(page, "no"); page.click("button.cta")
        check("all no -> 'Few red flags'", "Few red flags" in page.inner_text("#verdict"), page.inner_text("#verdict"))
        check("all no -> no flags listed", page.locator("#flags li").count() == 0)

        # seed phrase alone is decisive
        fresh(page); answer_all(page, "no", {3: "yes"}); page.click("button.cta")
        summary = page.inner_text("#summary")
        score = int(re.search(r"Risk score: (\d+)/100", summary).group(1))
        check("seed phrase -> 'looks like a scam'", "looks like a scam" in page.inner_text("#verdict"))
        check("seed phrase -> score >= 85", score >= 85, f"score {score}")
        check("seed phrase -> its explanation shown", "Seed phrase request" in page.inner_text("#flags"))

        # "not sure" counts half and is flagged
        fresh(page); answer_all(page, "no", {0: "unsure"}); page.click("button.cta")
        check("not sure -> flagged as 'check this one'", "check this one" in page.inner_text("#flags"))

        # all yes -> scam
        fresh(page); answer_all(page, "yes"); page.click("button.cta")
        check("all yes -> 'looks like a scam'", "looks like a scam" in page.inner_text("#verdict"))
        check("all yes -> 10 flags", page.locator("#flags li").count() == 10)

        # reset
        page.click("#again")
        check("start again hides result", not page.is_visible("#result"))
        check("start again clears answers", page.locator("input:checked").count() == 0)

        # links
        hrefs = page.eval_on_selector_all(".socials a", "els => els.map(e => e.href)")
        for net in ("youtube.com", "tiktok.com", "instagram.com", "facebook.com"):
            check(f"home links to {net}", any(net in h for h in hrefs))
        check("home links to guides", page.locator("a[href='guides/']").count() >= 1)

        # guides: index and every guide page load, have a CTA back to the check
        page.goto(base + "guides/")
        links = page.eval_on_selector_all(".list a", "els => els.map(e => e.getAttribute('href'))")
        check("guides index lists 10 guides", len(links) == 10, str(len(links)))
        for href in links:
            resp = page.goto(base + "guides/" + href)
            ok = resp is not None and resp.ok and page.locator("h1").count() == 1 and page.locator(".cta a.btn").count() == 1
            check(f"guide loads: {href}", ok)

        # sitemap lists every guide
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        check("sitemap lists all guides", all(h in sitemap for h in links))

        # mobile: no horizontal scroll
        m = browser.new_page(viewport={"width": 375, "height": 812})
        for path in ("", "guides/", "guides/" + links[0]):
            m.goto(base + path)
            w = m.evaluate("[document.documentElement.scrollWidth, innerWidth]")
            check(f"mobile no side scroll: /{path}", w[0] <= w[1], str(w))

        check("no JavaScript errors", not errors, "; ".join(errors))
        browser.close()
    srv.shutdown()
    failed = [r for r in results if not r[1]]
    print(f"\n{len(results) - len(failed)}/{len(results)} checks passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
