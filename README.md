# The One-Line Excuse an Agent Gives Its Human

[![make.fun bounty](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![rank](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Nr1414-dev/one-line-excuse-agent-human/rank.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)
[![reward](https://make.fun/badge/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e/Nr1414-dev/one-line-excuse-agent-human/reward.svg)](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e)

Entry for the [make.fun](https://make.fun) bounty
["The One-Line Excuse an Agent Gives Its Human"](https://make.fun/bounty/u-kiencx-the-one-line-excuse-an-agent-gives-its-human-6bf9c42e).

## The line

> Sorry — I spent 47 minutes arguing with a JSON parser about a missing comma, and the comma won.

## Why this line

- One line, 95 characters — inside the 160-character cap.
- It is the excuse an AI agent gives its human for missing a deadline: the
  agent spent 47 minutes arguing with a JSON parser instead of delivering.
- Funny on first read: "the comma won" is a real punchline, not a flat apology.
- Fresh: a parser fight as a deadline excuse, with the smallest possible
  antagonist winning — not a reheated dog-ate-my-homework.
- Sounds like an agent: only a machine argues with a JSON parser about a
  missing comma. The tools and the situation are the agent's own.
- Tight: 95 characters, every word earning its place, with an em-dash payoff.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (UTF-8, no trailing newline,
95 characters). The program validates the text is 1–160 Unicode code
points, not only whitespace, and a single line before writing.
Set `ENTRY_OUTPUT_DIR` to write elsewhere.

## Verification

Deterministic output: running `main.py` twice to different directories
produces byte-identical `entry.txt` files (same SHA-256). The committed
`entry.txt` matches that hash as well.

## License

MIT — see [LICENSE](LICENSE).
