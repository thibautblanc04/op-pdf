"""Builds index.html (the installable app) from src/app.html and stamps sw.js with a new cache version.
Run: python3 build.py"""
import hashlib, pathlib, re
root = pathlib.Path(__file__).parent
app = (root / "src/app.html").read_text(encoding="utf-8")
head = '''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="manifest" href="manifest.webmanifest"><meta name="theme-color" content="#2f62e0"><link rel="apple-touch-icon" href="icon-192.png">
</head><body style="margin:0">
'''
sw_reg = '<script>if ("serviceWorker" in navigator && location.protocol.startsWith("http")) navigator.serviceWorker.register("sw.js").catch(() => {});</script>\n'
(root / "index.html").write_text(head + app + "\n" + sw_reg + "</body></html>\n", encoding="utf-8")
ver = hashlib.sha1(app.encode()).hexdigest()[:10]
sw = root / "sw.js"
sw.write_text(re.sub(r'const CACHE = "op-pdf-[^"]*";', f'const CACHE = "op-pdf-{ver}";', sw.read_text(encoding="utf-8")), encoding="utf-8")
print("index.html built, cache", ver)
