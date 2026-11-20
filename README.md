# news-image-20261120 — The World Today

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/tulankganteng/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/tulankganteng/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

**Entry for the make.fun bounty [news-image-20261120](https://make.fun/bounty/news-image-20261120)
($250, deadline Sun 2026-11-22 07:00 WIB).** A program that writes one image
summing up the world's news of Friday 20 November 2026 to `/output/entry.png`.

## What the image shows

A newspaper front page, **"THE WORLD TODAY — FRIDAY 20 NOVEMBER 2026"**:

| Story | What happened |
|---|---|
| **TRUMP, XI & PUTIN SIGN PEACE DECLARATION** (lead) | After the first-ever trilateral summit in Shenzhen, the three leaders issue a four-point joint declaration: UN reform, oil supply, a warning to the ICC, and nuclear war "must never be fought". |
| **THE HAGUE — MYANMAR GUILTY OF GENOCIDE** | The World Court rules 9–6 that Myanmar committed genocide against the Rohingya — the first state ever held responsible — finding some 10,000 killed in 2017 and ordering reparations. |
| **KYIV HIT AGAIN** | Russian ballistic missiles strike the capital overnight as Ukraine hits the Kerch Bridge a third time in four days, halting rail traffic; Putin vows a "far more painful" response. |
| **RIYADH TOWER HIT** | A Houthi missile hits the 80-storey PIF Tower, blowing out windows across 7–8 floors; no injuries. The second landmark hit in 12 days. |
| **ANTHROPIC +17% ON DEBUT** | Shares close at $97.17, up 17% from the $83 IPO price, after opening at $111.50 — a record $81.3bn offering. |
| **MARKETS — ASIA PLUNGES** | Nikkei −4.8%, SoftBank −16%, KOSPI −4.7%, Taiwan −6.2%; the Dow fell 1,101 on Thursday. |

The three photographs are AI-generated editorial illustrations made for this
entry (no real person's likeness, no copied photograph); all text is set in
the composition script (`../compose.py`, kept outside the repo) so every word
is crisp and legible. The judge sees only the image — so the date, the
headline and every story are readable on the page itself.

## How it runs

`main.py` (Python 3.13, standard library only) copies the repository-held
`entry.png` to `/output/entry.png` (or to `$MAKEFUN_OUTPUT_DIR` for local
runs). No network, no clock, no randomness — two runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# out/entry.png — 1024×1024 PNG, < 1 MiB
```

## News sources (checked 20 Nov 2026)

- Trump–Xi–Putin peace declaration: Reuters
- ICJ Myanmar genocide ruling 9–6: CNN, Reuters, Le Monde, WSJ
- Kyiv / Kerch Bridge strikes: Reuters, AP
- Houthi strike on Riyadh PIF Tower: WSJ, Reuters
- Anthropic debut close $97.17 (+17%): Reuters, WSJ, CNN
- Asian markets plunge: Reuters, CNBC

## License

MIT — see [LICENSE](LICENSE).

## Reproducibility

The image is fixed: `main.py` copies the repository's own `entry.png`
to the output directory byte for byte, then reads the copy back and
compares it with the source before reporting success. No network calls,
no randomness, no image processing — two runs write identical bytes.
