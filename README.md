# Links page handover (بستان الحكايا وازرعها)

Original: https://files.instinct.com/cr9d897bjnil (React page on the Instinct Files host; the page chrome comes from that host, so it is not in original-source/).
This folder is a standalone static replica for GitHub Pages: index.html + style.css + app.js + links.json + img/.

## To change links
Edit links.json only. Per link: label, note, href, live (true = gold-bordered navy button, false = greyed "قريبًا" button, no href).
Current state: Bustan: YouTube, Instagram, TikTok, Facebook all live. Ezra3ha: YouTube live, TikTok + Facebook "soon". (Ezra3ha Instagram is not listed yet; add when live.)
Facebook href is the share link the user sent (https://www.facebook.com/share/1FVv1NHXJX/); swap for a clean page URL later.

## Design spec (measured from the live page)
- Direction RTL, lang ar. Page background #fdfcfb. Body text #101113. Headings/intro color #4d3533.
- Headings: Georgia/serif stack (host uses "Aime"), weight 400; h1 36px, group h2 21px. Intro/closing 14px, weight 350. Arabic fallback: Noto Sans Arabic / Noto Naskh Arabic.
- Channel photo: 88px circle, 3px border #d4a53f (gold).
- Buttons: full width, padding 14px 18px, radius 14px, gradient 135deg #1c2b4a to #24365c, text #f5eeda, border 1px #d4a53f at 33% alpha. Label 17px bold, note 13px at 75% opacity. Soon state: 45% opacity.
- Column max width about 640px, centered.
- Photos: img/kids.jpg (Bustan logo, rabbit and turtle), img/agri.jpg (arugula seedling), resized to 400px from originals.
- original-source/App.tsx and style.css are the exact original React source for reference.

## Static build
index.html is generated from links.json. After editing links.json run `python3 build.py` and commit both. No JavaScript is needed at runtime.
