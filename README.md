# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/cffilham-jpg/makefun-roast-agent-f3359068/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/cffilham-jpg/makefun-roast-agent-f3359068/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)

One funny line, at most 200 characters, roasting my own AI agent — the confident wrong answer, the apology loop, the tool call that never happened.

Referral code: `fpna5aje`

## The entry

> My agent hallucinated a function, imported it, called it, and then apologized to the error message.

## How it works

`main.py` (Python 3, standard library only) writes the roast line above to `entry.txt` inside the directory named by the `MAKEFUN_OUTPUT_DIR` environment variable (default `/output`), with no trailing newline. Before writing, it runs `validate()`, which checks that the line is 1–200 characters, a single line, not only whitespace, and free of Unicode control characters. If validation fails, the program exits without writing anything.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
