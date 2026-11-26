#!/usr/bin/env python3
"""Regenerates index.html from links.json. Run: python3 build.py"""
import json, html
d = json.load(open('links.json', encoding='utf-8'))
e = html.escape
body = f'<h1>{e(d["title"])}</h1>\n<p class="intro">{e(d["intro"])}</p>\n'
for c in d['channels']:
    body += f'<section class="lp-channel"><h2>{e(c["name"])}</h2>\n<img class="lp-photo" src="{e(c["photo"])}" alt="{e(c["alt"])}" width="88" height="88">\n<p class="lp-tagline">{e(c["tagline"])}</p>\n<div class="lp-links">\n'
    for l in c['links']:
        inner = f'<span class="lp-btn-label">{e(l["label"])}</span><span class="lp-btn-note">{e(l["note"])}</span>'
        if l['live']:
            body += f'<a class="lp-btn" href="{e(l["href"])}" target="_blank" rel="noopener">{inner}</a>\n'
        else:
            body += f'<span class="lp-btn lp-btn-soon" aria-disabled="true">{inner}</span>\n'
    body += '</div></section>\n'
body += f'<p class="closing">{e(d["closing"])}</p>\n'
page = f'''<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(d["title"])}</title>
<meta name="description" content="{e(d["intro"])}">
<meta name="theme-color" content="#fdfcfb">
<meta property="og:title" content="{e(d["title"])}">
<meta property="og:description" content="{e(d["intro"])}">
<meta property="og:type" content="website">
<meta property="og:image" content="img/kids.jpg">
<link rel="icon" href="favicon.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;700&family=Noto+Sans+Arabic:wght@300;400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main class="page">
{body}</main>
</body>
</html>
'''
open('index.html', 'w', encoding='utf-8').write(page)
