#!/usr/bin/env python3
"""news-image-20261120 — one image summing up the world's news of Fri 20 Nov 2026.

The entry image (entry.png, held beside this file in the repository) is a
newspaper front page, "THE WORLD TODAY — FRIDAY 20 NOVEMBER 2026":

  * Lead: TRUMP, XI & PUTIN SIGN PEACE DECLARATION — after the first-ever
    trilateral summit in Shenzhen, the three leaders issue a four-point
    joint declaration: UN reform, oil supply, a warning to the ICC, and
    nuclear war "must never be fought".
  * THE HAGUE — the World Court rules 9-6 that Myanmar committed genocide
    against the Rohingya, the first state ever held responsible, finding
    some 10,000 killed in 2017 and ordering reparations.
  * KYIV — Russian ballistic missiles strike the capital overnight as
    Ukraine hits the Kerch Bridge a third time in four days, halting rail
    traffic; Putin vows a "far more painful" response.
  * RIYADH TOWER HIT — a Houthi missile hits the 80-storey PIF Tower,
    blowing out windows across 7-8 floors; no injuries.
  * ANTHROPIC +17% ON DEBUT — shares close at $97.17, up 17% from the $83
    IPO price, after opening at $111.50; a record $81.3bn offering.
  * MARKETS — ASIA PLUNGES: Nikkei -4.8%, SoftBank -16%, KOSPI -4.7%,
    Taiwan -6.2%; the Dow fell 1,101 on Thursday.

The three photographs are AI-generated editorial illustrations made for this
entry (no real person's likeness, no copied photograph); all text on the
page is set in the composition script so every word is legible.

The program needs no network and writes the same bytes on every run: it
copies the repository-held image to /output/entry.png (or to the directory
named by MAKEFUN_OUTPUT_DIR when that is set, for local runs).
"""
import os
import shutil
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"


def main():
    # Deterministic by construction: a byte-for-byte copy of a fixed file,
    # so two runs write identical bytes. No network, no clock, no randomness.
    here = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(here / SOURCE_NAME, out_dir / OUTPUT_NAME)


if __name__ == "__main__":
    main()
