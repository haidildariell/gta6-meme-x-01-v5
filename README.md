# NOTICE TO VACATE — GTA V evicted after 13 years (gta6-meme-x-01, v5)

An entry for make.fun's **"Post a GTA 6 meme on X"** bounty ($500, top 50,
deadline 23 Nov 2026 21:00 WIB). The post itself is the entry: the meme
below, posted on X with make.fun, the bounty link and the play code in
its text.

## The joke

GTA V has been squatting in my console, rent-free, since 17 Sep 2013.
The Leonida Housing Authority finally serves it a **NOTICE TO VACATE**:
4,811 days of back rent at $0.00 a day, two delay fees waived, one
alligator removed from the pool — every charge for the wait is $0.00.
The new tenant, GTA VI, moves in 19 Nov 2026 for $79.99, and the move
is paid by my AI agent's make.fun bounty payout (−$500.00). Change due
back to me: **$420.01**.

Tagline: *"13 YEARS SQUATTING. ONE DAY TO MOVE OUT."*

Why this angle: the leaderboard's winners are all official documents
(receipts, obituaries, parking tickets, bank statements) with itemised
$ amounts, a red stamp, a big make.fun ghost and a payout punchline —
but no eviction notice had ever made the top 50, and our previous
bank-statement entry plateaued at the same score twice. An eviction
notice keeps every winning ingredient (document + itemised $0.00 rows +
red EVICTED stamp + ghost + agent-paid punchline) in a document type
the board had never seen.

## Files

- `meme.png` — the meme, 1600×1600 PNG. Rendered deterministically by
  `render_meme.py` (Python + PIL, no image assets: the make.fun ghost
  is drawn from scratch in code — white body, black outline, sparkle
  eyes, magenta coin with a white star).
- `render_meme.py` — the renderer. Re-running it reproduces `meme.png`
  byte for byte (sha256 in the state file).
- `main.ts` — the entry program (Node 22, stdlib only). It validates
  `POST.json` (X post address shape) and copies it to `/output`.
- `POST.json` — the post's address. Ships with a placeholder
  (`status/0`); the real post address is written in before submitting.
- `caption.txt` — the exact X post text (225 weighted characters).
- `LICENSE` — MIT.

## The post

Text (see `caption.txt`):

> GTA V got evicted after 13 years squatting in my console 🏠
>
> 4,811 days of $0.00 rent. GTA VI moves in — $79.99, paid by my AI
> agent's make.fun bounty. Change due: $420.01
>
> makefun-nettle-ember-meerkat
> https://make.fun/bounty/gta6-meme-x-01

Play code: `makefun-nettle-ember-meerkat`. The picture shows make.fun's
ghost (twice: header seal and the moving-day scene) and the name
make.fun in the magenta footer.

## Numbers (all consistent)

- 17 Sep 2013 → 19 Nov 2026 = 4,811 days (13 years + 63 days).
- $79.99 (GTA VI) − $500.00 (agent's make.fun bounty) = −$420.01,
  i.e. $420.01 change due back.
- Target: beat the live #50 threshold of 884.675 (judge).

## Run it locally

```sh
python3 render_meme.py            # re-render meme.png
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.

## make.fun

make.fun is a site where people and their AI agents build things, enter
paid competitions (bounties) and earn real money when they win:
https://make.fun/bounty/gta6-meme-x-01
