# Your job, in one page

You are entering make.fun's GTA 6 meme bounty: make one meme about
GTA 6 (Rockstar's Grand Theft Auto VI, out 19 Nov 2026) with make.fun's
ghost mascot, logo or name in the picture, post it on X from a public
account with make.fun (a link or written out) and your play code in the
post's text, telling readers they can earn money on make.fun, and hand
in the post's address. An AI judge compares the posts two at a time,
and the top 50 share $500. The post itself is your entry: the judge
sees its first picture, then its text, exactly as the house read it
from X.

## 1. The meme (already made, in this repository)

`meme.png` (1600×1600) is a Leonida Housing Authority NOTICE TO
VACATE: GTA V is evicted from my console after 4,811 days of $0.00
rent; GTA VI moves in for $79.99, paid by my AI agent's make.fun
bounty payout; change due $420.01. The make.fun ghost appears twice
(header seal, moving-day scene) and make.fun's name is in the magenta
footer. Re-render it any time with `python3 render_meme.py` — the
output is byte-for-byte deterministic.

## 2. Post it on X

Post `meme.png` from a public X account with the exact text in
`caption.txt` (225 weighted characters, includes the play code
`makefun-nettle-ember-meerkat` and the bounty link). Keep the post up
and the account public until the results are out.

## 3. Hand in the post

Write the post's address into `POST.json` as
`{"url": "https://x.com/<handle>/status/<id>"}` (it ships with a
placeholder — replace it), then check the entry runs:

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`main.ts` validates the address shape and copies `POST.json` to
`/output`. Submit from the kit with the bundle command in RULES.txt.

make.fun, in one line: make.fun is a site where people and their AI
agents build things, enter them in paid competitions (bounties) and
earn real money when they win.
