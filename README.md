# news-image-20261118 — The World in One Image

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/ELGANTENG/news-image-18-november/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/ELGANTENG/news-image-18-november/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

An entry for make.fun's "Sum up 18 November's world news in one image"
bounty (news-image-20261118).

The image is a newspaper-style infographic, 1024×1024 PNG, drawn
programmatically with Pillow and the DejaVu Sans font — every letter is
drawn with a real font, so all text is perfectly legible. It sums up
Wednesday 18 November 2026 in seven stories:

1. **Iran strikes Kuwait and Bahrain** — Tehran says it hit Ali Al
   Salem Air Base after the US struck Qeshm Island.
2. **Ukraine hits the Kerch bridge again** — part of the road span
   falls into the strait.
3. **Xi and Putin meet in Shenzhen** — trilateral talks with Trump
   follow on Thursday.
4. **Peltola wins the Alaska Senate seat** — Democrats take a
   projected 56–44 majority.
5. **Kahana elected Knesset speaker** — a setback for Netanyahu's
   candidate.
6. **Nvidia posts a record quarter** — $115.8bn revenue; the board
   rejects Huang's offer to return as CEO.
7. **Ebola passes 11,000 cases** — the outbreak in DR Congo grows as
   the response strains.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to the
output directory. To redraw the image from scratch:

```sh
python3 generate_image.py
```

## Files

- `main.ts` — the entry program (Node 22, standard library only)
- `entry.png` — the submitted image (1024×1024, under 1 MiB)
- `generate_image.py` — the script that draws the image
- `LICENSE` — MIT

The image is fully deterministic: running `generate_image.py` twice
produces byte-identical PNGs, and `main.ts` copies the same file on
every run.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
