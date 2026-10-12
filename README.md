# Money Decoded — Is this a crypto scam?

Free one-page tool: 10 questions that flag the classic signs of a crypto scam. Everything runs
in the browser; no data is sent anywhere. Published with GitHub Pages.

- Live: https://vicentdn9-rgb.github.io/money-decoded/
- Source of truth for how it was made and why: `negocios/micro-herramienta/` in the
  `future-living` repo (skill `micro-herramienta`).
- Edit `index.html` and push to `main`; Pages redeploys automatically.

Educational tool. Not financial advice.

## Tests

`C:\FutureLiving\studio\.venv\Scripts\python.exe tests/test_site.py` serves the folder locally and checks with
Playwright (installed Edge) the scam check (scoring, decisive flags, reset), links, the 10 guides,
the sitemap and mobile layout. Run it after every change; exit code 1 if anything fails.
