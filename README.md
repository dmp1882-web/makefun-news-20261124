[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/dmp1882-web/makefun-news-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/dmp1882-web/makefun-news-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

# Sum up 24 November 2026 in one image

Entry for the make.fun bounty
[news-image-20261124](https://make.fun/bounty/news-image-20261124):
a program that writes one image summing up the world's news of
Tuesday 24 November 2026 to `/output/entry.png`.

## The image

`entry.png` (1024x1024, JPEG bytes in an `.png` name, which the rules
allow) is a newspaper front page for the day. It names the date in the
masthead and covers six stories, each with its own panel and label:

1. **Nvidia rehires Huang** — Nvidia reinstates Jensen Huang as CEO,
   effective immediately, a stunning reversal after his resignation
   less than two weeks earlier, following a push from Trump.
2. **Russia hits Zaporizhzhia** — a Russian attack overnight kills 2
   people and wounds 22, including 2 children, in Zaporizhzhia,
   Ukraine.
3. **North Korea breaches sky** — a suspected North Korean aircraft
   breaches South Korean airspace near Ulleung island, prompting
   residents to take shelter.
4. **Hasina plans comeback** — ousted Bangladeshi prime minister
   Sheikh Hasina plans to return home from exile in India on
   16 December, the anniversary of the 1971 liberation war's end.
5. **Democrats take House** — US Democrats clinch their biggest House
   majority since 1992, with at least 258 seats.
6. **Tankers hit in Hormuz** — three oil tankers are hit by sea mines
   and catch fire while passing through the Strait of Hormuz.

The image is drawn once and held in the repository as `entry.png.b64`
(the same bytes, base64-encoded so the file is plain text); the program
below decodes it, so both grader runs write identical bytes.

## The program

`main.py` (Python 3.13, standard library only) decodes `entry.png.b64`
and writes the image to `/output/entry.png`. It uses no network.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT. See `LICENSE`.
