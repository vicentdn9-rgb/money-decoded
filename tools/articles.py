"""Generate the guide pages of the Money Decoded site.

Each article is original educational content written for the site. Run:
    python tools/articles.py
It writes guides/<slug>.html and guides/index.html. Edit ARTICLES below and re-run.
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://vicentdn9-rgb.github.io/money-decoded/"
UPDATED = "2026-10-03"

ARTICLES = [
    {
        "slug": "crypto-seed-phrase-scam",
        "title": "Seed Phrase Scams: Why Anyone Who Asks Is Trying to Rob You",
        "desc": "No real company, support agent or app will ever ask for your seed phrase. Here is how the fake-support scam works and how to protect your wallet.",
        "body": [
            ("p", "Your seed phrase (also called recovery phrase) is the list of 12 or 24 words you got when you created your crypto wallet. It is not a password you can reset. It is the master key: whoever has those words can move every coin in the wallet from any device in the world, and the transfer cannot be reversed."),
            ("h2", "How the scam works"),
            ("p", "You post a question about a stuck transaction or a wallet error on social media. Within minutes, a friendly \"support agent\" replies or sends you a DM. They look official, use the right logo and sound helpful. After a few messages they send you a link to \"validate\" or \"sync\" your wallet, which asks for your seed phrase. Seconds after you type it, your wallet is empty."),
            ("p", "Variations include fake wallet apps in app stores, pop-ups saying your wallet \"needs verification\", and emails that copy the design of real exchanges."),
            ("h2", "Red flags"),
            ("ul", [
                "Anyone, for any reason, asks for your 12 or 24 words.",
                "\"Support\" contacts you first, by DM, comment or email.",
                "A website or form asks you to type or upload your recovery phrase.",
                "You are told to act fast or your funds will be lost.",
            ]),
            ("h2", "How to protect yourself"),
            ("ul", [
                "Never type your seed phrase into a website, app, chat or email. The only time you enter it is when you restore your own wallet on your own device.",
                "Write it on paper or metal and keep it offline. No photos, no cloud notes, no screenshots.",
                "Only contact support through the official website you type yourself, never through a link someone sends you.",
                "If you already shared it, create a new wallet on a clean device right away and move whatever is left.",
            ]),
        ],
    },
    {
        "slug": "pig-butchering-scam",
        "title": "Pig Butchering Scam: The Friendly Stranger Who Teaches You to Trade",
        "desc": "A wrong-number text, a new friend, and a trading app that only goes up. How pig butchering crypto scams work and the signs to stop before you lose money.",
        "body": [
            ("p", "Pig butchering is a long-con investment scam. The name comes from the scammers themselves: they \"fatten\" the victim with trust for weeks before taking everything. It is one of the most costly crypto scams for ordinary people."),
            ("h2", "How it works"),
            ("p", "It often starts with a text sent to the \"wrong number\", or a match on a dating app or social media. The stranger is friendly, successful and patient. Over days or weeks you become friends. Then they casually mention how much they make trading crypto and offer to show you."),
            ("p", "They guide you to a trading website or app that looks professional. Your first small deposit shows big profits, and you may even withdraw a little to prove it is real. Then you are encouraged to invest more. When you try to withdraw a large amount, you are told to pay a \"tax\", \"fee\" or \"unlock deposit\" first. The money, the platform and the friend disappear."),
            ("h2", "Red flags"),
            ("ul", [
                "A stranger who contacted you first starts talking about investing.",
                "They refuse video calls or always have an excuse not to meet.",
                "The platform is one you had never heard of and they send you the link.",
                "Profits look too steady and too high.",
                "You must pay before you can withdraw.",
            ]),
            ("h2", "What to do"),
            ("ul", [
                "Never invest on a platform recommended by someone you only know online.",
                "Check whether the platform is registered with a financial regulator in your country.",
                "If you are asked to pay to withdraw, stop sending money: the balance you see is not real.",
                "Report it to your local police and, in the US, to the FBI's IC3 (ic3.gov).",
            ]),
        ],
    },
    {
        "slug": "crypto-wallet-drainer",
        "title": "Wallet Drainers: How \"Connect Wallet\" Can Empty Your Crypto",
        "desc": "Fake airdrops and mint pages trick you into approving a contract that drains your wallet. Learn the signs and how to revoke dangerous approvals.",
        "body": [
            ("p", "A wallet drainer is a malicious website that looks like a free airdrop, an NFT mint or a popular app. It does not need your seed phrase. It only needs you to click \"connect\" and then \"approve\" or \"sign\"."),
            ("h2", "How it works"),
            ("p", "You see a post or DM about a free token claim or a limited mint. The site looks legitimate and asks you to connect your wallet. Then your wallet shows a request to approve spending or sign a message. That approval can give the site permission to move your tokens or NFTs, now or later, without asking again."),
            ("h2", "Red flags"),
            ("ul", [
                "Free tokens or NFTs you did not expect, with a countdown.",
                "Links from replies, DMs or sponsored posts instead of the project's official site.",
                "Your wallet asks for an approval with an unlimited amount, or a signature you do not understand.",
                "The website address is slightly different from the real one.",
            ]),
            ("h2", "How to protect yourself"),
            ("ul", [
                "Keep long-term savings in a separate wallet that never connects to new sites.",
                "Read every wallet pop-up. If you do not understand what you are signing, reject it.",
                "Regularly check and revoke old token approvals with a reputable approval checker for your network.",
                "Bookmark the real sites you use and only open them from your bookmarks.",
            ]),
        ],
    },
    {
        "slug": "crypto-ponzi-guaranteed-returns",
        "title": "\"2% a Day, Guaranteed\": How to Spot Ponzi Math in Crypto",
        "desc": "Guaranteed daily returns are the oldest trick in the book. See why 2% a day is impossible and how Ponzi schemes pay early investors with new money.",
        "body": [
            ("p", "If an investment promises a fixed daily or weekly return, do the math before anything else. 2% a day sounds small. Compounded for a year, it would turn $1,000 into more than $1,300,000. No real business, bank or trading strategy does that consistently."),
            ("h2", "How a Ponzi scheme works"),
            ("p", "Early investors are paid \"profits\" that actually come from the deposits of newer investors. Payments arrive on time at the beginning, which builds trust and word of mouth. Many schemes add referral bonuses so members recruit friends and family. When new deposits slow down, withdrawals are delayed, then frozen, and the operators disappear."),
            ("h2", "Red flags"),
            ("ul", [
                "Guaranteed or fixed returns, especially daily ones.",
                "Bonuses for bringing in new people.",
                "Vague explanations like \"AI trading bot\", \"arbitrage\" or \"secret strategy\".",
                "Withdrawal limits, waiting periods or new fees when you try to cash out.",
                "No registered company or regulator behind it.",
            ]),
            ("h2", "What to do"),
            ("ul", [
                "Treat any guaranteed return as a warning, not a feature.",
                "Search the company name together with words like \"scam\", \"withdrawal\" and \"regulator\".",
                "Never recruit others into something you cannot fully explain.",
            ]),
        ],
    },
    {
        "slug": "crypto-giveaway-scam",
        "title": "Crypto Giveaway Scams: Nobody Will Double Your Money",
        "desc": "\"Send 1 BTC, get 2 back\" live streams and posts use deepfakes of famous people. How the fake giveaway scam works and why you should never send first.",
        "body": [
            ("p", "The fake giveaway is simple and still steals large amounts every year. A post, ad or live stream claims that a famous person or company is giving away crypto: send any amount to an address and you will receive double back."),
            ("h2", "How it works"),
            ("p", "Scammers hijack or create accounts that look official, often with AI-generated deepfake video of a celebrity or CEO. Bot comments celebrate their \"winnings\" and a countdown pushes you to hurry. Anything you send goes straight to the scammer and never comes back."),
            ("h2", "Red flags"),
            ("ul", [
                "Any offer to multiply crypto you send.",
                "A countdown or \"only the first 1,000 participants\".",
                "Comments full of people thanking the account for paying them.",
                "The account or channel was recently renamed or has few real posts.",
            ]),
            ("h2", "Remember"),
            ("p", "Real giveaways never ask you to send money first. If you have to pay to receive, it is not a giveaway."),
        ],
    },
    {
        "slug": "crypto-address-poisoning",
        "title": "Address Poisoning: The Tiny Transaction That Sets You Up",
        "desc": "Scammers send dust from a look-alike address so you copy the wrong one from your history. How address poisoning works and how to check every address.",
        "body": [
            ("p", "Address poisoning is a trick that relies on one habit: copying a wallet address from your recent transactions instead of from a trusted source."),
            ("h2", "How it works"),
            ("p", "After you send crypto to someone, a scammer creates an address that starts and ends with the same characters as the real one. They send you a tiny amount, or a zero-value token transfer, from that look-alike address so it appears in your history. Next time you want to pay the same person, you copy the address from your history, pick the fake one, and your money goes to the scammer."),
            ("h2", "Red flags"),
            ("ul", [
                "Small, unexpected transactions or unknown tokens appearing in your wallet.",
                "Two addresses in your history that look almost identical.",
            ]),
            ("h2", "How to protect yourself"),
            ("ul", [
                "Never copy addresses from your transaction history. Use your wallet's address book or ask the recipient again.",
                "Check the full address, not just the first and last characters.",
                "For large amounts, send a small test first and confirm it arrived.",
                "Ignore and hide unknown tokens; do not interact with them.",
            ]),
        ],
    },
    {
        "slug": "crypto-rug-pull",
        "title": "Rug Pulls: When the Chart Only Goes Up Until It Hits Zero",
        "desc": "A new token rockets 10x, then the creators pull the liquidity and it goes to zero in minutes. How rug pulls work and the checks to do before buying.",
        "body": [
            ("p", "A rug pull happens when the creators of a token or project suddenly take the money investors put in and leave. The price collapses to almost zero and holders cannot sell."),
            ("h2", "How it works"),
            ("p", "A new token is launched with heavy hype on social media and paid influencers. Early buyers see huge gains, which attracts more buyers. The creators control most of the supply or the trading liquidity. At the peak they sell everything or remove the liquidity pool, and the token becomes worthless within minutes. Some tokens are even coded so that buyers cannot sell at all."),
            ("h2", "Red flags"),
            ("ul", [
                "Anonymous team and no working product.",
                "A few wallets hold most of the supply.",
                "Liquidity is not locked, or the lock ends soon.",
                "Promises of 100x, pressure to buy now, and influencers who were paid to promote it.",
                "You cannot find anyone who has successfully sold.",
            ]),
            ("h2", "What to do"),
            ("ul", [
                "Treat brand-new tokens as gambling, not investing, and only use money you can afford to lose.",
                "Check who holds the supply and whether liquidity is locked before buying.",
                "Be extra careful with tokens promoted in DMs or Telegram groups.",
            ]),
        ],
    },
    {
        "slug": "crypto-recovery-scam",
        "title": "Crypto Recovery Scams: The Second Scam After the First",
        "desc": "Lost crypto to a scam? Fake recovery agents and \"fraud investigators\" will promise to get it back for a fee. How to recognise them and what actually helps.",
        "body": [
            ("p", "After someone loses money to a crypto scam, they often become the target of a second one. Fake \"recovery experts\", \"blockchain investigators\" or even people posing as lawyers or police contact the victim and promise to get the money back."),
            ("h2", "How it works"),
            ("p", "They find victims through scam-report forums, social media posts and ads aimed at people who lost money. They sound professional, may show fake certificates or case numbers, and claim they can trace and freeze the stolen funds. They ask for an upfront fee, then more fees for \"taxes\", \"legal costs\" or \"wallet unlocking\". No money is ever recovered."),
            ("h2", "Red flags"),
            ("ul", [
                "Someone contacts you first offering to recover your crypto.",
                "They guarantee results or say they can \"hack back\" the funds.",
                "They want payment upfront, in crypto or gift cards.",
                "They ask for your seed phrase or remote access to your computer.",
            ]),
            ("h2", "What actually helps"),
            ("ul", [
                "Stop sending money to anyone.",
                "Save every message, address and transaction ID.",
                "Report it to the exchange you used, your bank and the police. In the US, also to the FBI's IC3 (ic3.gov) and the FTC (reportfraud.ftc.gov).",
                "If you want a lawyer, find one yourself through your local bar association, never through an ad or a DM.",
            ]),
        ],
    },
    {
        "slug": "crypto-wrong-network",
        "title": "Same Coin, Different Network: How to Avoid Losing Crypto by Mistake",
        "desc": "USDT on Ethereum is not the same as USDT on Tron. Sending on the wrong network can lose your funds. A simple checklist before every transfer.",
        "body": [
            ("p", "Not every loss is a scam. One of the most common ways people lose crypto is sending it on the wrong network. Many coins, especially stablecoins like USDT and USDC, exist on several blockchains at the same time."),
            ("h2", "Why it happens"),
            ("p", "When you withdraw from an exchange, you choose both the coin and the network. If the receiving wallet or exchange does not support that network, the funds can arrive somewhere you cannot access. Sometimes support can recover them for a fee; often they are gone."),
            ("h2", "Checklist before every transfer"),
            ("ul", [
                "Ask the receiver which network they support and match it exactly.",
                "Check that the address format fits that network.",
                "Send a small test amount first and wait until it arrives.",
                "Double-check memo or tag fields when the receiver requires them.",
                "Check the network fee before confirming.",
            ]),
            ("h2", "Remember"),
            ("p", "Same name does not mean same network. A few seconds of checking is cheaper than a lost transfer."),
        ],
    },
    {
        "slug": "crypto-exchange-safety",
        "title": "Is Your Crypto Safe on an Exchange? 3 Checks Before You Trust One",
        "desc": "Not your keys, not your coins. Three checks to do before leaving crypto on an exchange, and when a self-custody wallet makes more sense.",
        "body": [
            ("p", "When your crypto sits on an exchange, the exchange holds the keys. If it is hacked, freezes withdrawals or goes bankrupt, you may not get your money back. That is what \"not your keys, not your coins\" means."),
            ("h2", "Check 1: Is it regulated where you live?"),
            ("p", "Look for registration with the financial regulator in your country, and be wary of platforms that cannot say where they are based. A copycat website with a similar name is a common trap, so type the address yourself."),
            ("h2", "Check 2: Can you withdraw easily?"),
            ("p", "Test with a small withdrawal. Unusual delays, surprise fees or new requirements to withdraw are warning signs."),
            ("h2", "Check 3: Is your account locked down?"),
            ("ul", [
                "Use an authenticator app or security key for two-factor login, not SMS if you can avoid it.",
                "Turn on withdrawal address allow-lists if available.",
                "Use a unique password and a separate email for your crypto accounts.",
            ]),
            ("h2", "When to use your own wallet"),
            ("p", "For savings you do not trade often, many people move funds to a self-custody wallet, such as a hardware wallet, where only they hold the keys. That also means only you are responsible for backing up the seed phrase safely."),
        ],
    },
]

CSS = """
:root{--bg:#070b1f;--panel:#0f1a45;--panel2:#0a1030;--line:#1d2a5c;--text:#f4f7ff;--muted:#aab4d6;--cyan:#2ee6ff;--magenta:#ff3d9a;--gold:#ffc83d}
*{box-sizing:border-box}html,body{margin:0}
body{background:var(--bg);color:var(--text);font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:760px;margin:0 auto;padding:24px 16px 64px}
header{display:flex;align-items:center;gap:12px;margin-bottom:24px}
header a{display:flex;align-items:center;gap:12px;color:var(--text);text-decoration:none}
header img{width:40px;height:40px;border-radius:50%;border:2px solid var(--cyan)}
.brand{font-weight:800;letter-spacing:.5px}.brand span{color:var(--cyan)}
h1{font-size:clamp(28px,6vw,40px);line-height:1.15;margin:0 0 10px}
h2{font-size:22px;margin:28px 0 8px;color:var(--gold)}
.meta{color:var(--muted);font-size:14px;margin-bottom:20px}
a{color:var(--cyan)}ul{padding-left:22px}li{margin:6px 0}
.cta{margin-top:32px;padding:18px;border-radius:16px;background:linear-gradient(180deg,var(--panel),var(--panel2));border:1px solid var(--line)}
.cta a.btn{display:inline-block;margin-top:8px;padding:12px 18px;border-radius:12px;font-weight:800;color:#070b1f;text-decoration:none;background:linear-gradient(90deg,var(--cyan),var(--magenta))}
.list a{display:block;padding:14px 16px;margin:10px 0;border-radius:14px;border:1px solid var(--line);background:var(--panel2);color:var(--text);text-decoration:none}
.list a:hover{border-color:var(--cyan)}.list small{display:block;color:var(--muted)}
footer{margin-top:40px;color:var(--muted);font-size:13px}
"""

SOCIALS = (
    '<a href="https://www.youtube.com/@MoneyDecoded.Explained" target="_blank" rel="noopener">YouTube</a> · '
    '<a href="https://www.tiktok.com/@money_decoded_real" target="_blank" rel="noopener">TikTok</a> · '
    '<a href="https://www.instagram.com/money_decoded_real/" target="_blank" rel="noopener">Instagram</a> · '
    '<a href="https://www.facebook.com/profile.php?id=61594367282797" target="_blank" rel="noopener">Facebook</a>'
)


def page(title, desc, canonical, inner, ld=None):
    ld_tag = '<script type="application/ld+json">%s</script>' % json.dumps(ld) if ld else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} | Money Decoded</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="article"><link rel="icon" href="../logo.png">
<style>{CSS}</style>{ld_tag}</head>
<body><div class="wrap">
<header><a href="../"><img src="../logo.png" alt="Money Decoded logo"><div class="brand">MONEY <span>DECODED</span></div></a></header>
{inner}
<footer>Educational content by Money Decoded. Not financial or legal advice. · {SOCIALS}</footer>
</div></body></html>
"""


def render_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == "p":
            out.append(f"<p>{html.escape(val)}</p>")
        elif kind == "h2":
            out.append(f"<h2>{html.escape(val)}</h2>")
        elif kind == "ul":
            out.append("<ul>" + "".join(f"<li>{html.escape(x)}</li>" for x in val) + "</ul>")
    return "\n".join(out)


def main():
    gdir = os.path.join(ROOT, "guides")
    os.makedirs(gdir, exist_ok=True)
    for a in ARTICLES:
        url = SITE + "guides/" + a["slug"] + ".html"
        inner = (
            f"<h1>{html.escape(a['title'])}</h1>"
            f"<div class=\"meta\">Updated {UPDATED} · <a href=\"./\">All scam guides</a></div>"
            + render_body(a["body"])
            + '<div class="cta"><b>Not sure about an offer right now?</b><br>'
            'Answer 10 quick questions and see the red flags.<br>'
            '<a class="btn" href="../">Take the free scam check</a>'
            '<p style="margin:14px 0 0;color:var(--muted)">Watch the 60-second animated explainers on ' + SOCIALS + '.</p></div>'
        )
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"],
              "description": a["desc"], "dateModified": UPDATED, "author": {"@type": "Organization", "name": "Money Decoded"},
              "mainEntityOfPage": url}
        with open(os.path.join(gdir, a["slug"] + ".html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(page(a["title"], a["desc"], url, inner, ld))
    items = "".join(
        f'<a href="{a["slug"]}.html">{html.escape(a["title"])}<small>{html.escape(a["desc"])}</small></a>' for a in ARTICLES
    )
    inner = ("<h1>Crypto Scam Guides</h1><div class=\"meta\">How each scam works, the red flags, and what to do. Updated "
             + UPDATED + ".</div><div class=\"list\">" + items + "</div>"
             '<div class="cta"><b>Check a specific offer</b><br><a class="btn" href="../">Take the free scam check</a></div>')
    with open(os.path.join(gdir, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(page("Crypto Scam Guides", "Plain-English guides to the most common crypto scams: how they work, red flags and what to do.",
                     SITE + "guides/", inner))
    urls = [SITE, SITE + "guides/"] + [SITE + "guides/" + a["slug"] + ".html" for a in ARTICLES]
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            f.write(f"  <url><loc>{u}</loc><lastmod>{UPDATED}</lastmod></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
    print(len(ARTICLES), "guides written")


if __name__ == "__main__":
    main()
