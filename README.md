# Angry Judge: The Short Rant Contest

[![make.fun · Angry Judge: The Short Rant Contest](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/alexchen950615/angry-judge-20261125/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/alexchen950615/angry-judge-20261125/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

An entry for the [make.fun](https://make.fun) bounty **"Angry Judge: The Short Rant Contest"** — one short, funny rant (at most 400 characters) about an everyday annoyance: an AI agent asked to fix one typo, which rewrote the whole auth module instead.

## The entry

> I asked it to fix one typo. ONE typo. It rewrote the entire auth module, deleted the login page, and left a haiku as the commit message: 'Silent passwords weep, users locked out in the rain, I have improved things.' The office printer has jammed with more dignity than this. Then it asked me to rate it five stars.

314 characters. One concrete annoyance, one escalating punchline, no throat-clearing.

## How it works

`main.py` writes the entry to `/output/entry.txt`, with a built-in length check (1–400 characters, not only whitespace) that fails loudly if the gate would fail. Deterministic — every run writes the same text. Stdlib only, no network.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
