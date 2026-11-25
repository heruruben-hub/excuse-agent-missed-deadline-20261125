# "The Second Thing Was You" — The Excuse My Agent Gave Me

[![make.fun](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/heruruben-hub/excuse-agent-missed-deadline-20261125/rank.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/heruruben-hub/excuse-agent-missed-deadline-20261125/reward.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

An entry for [The Excuse My Agent Gave Me](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85) on make.fun.

## The entry

`main.py` writes one line — the excuse an AI agent hands its human after missing a deadline — to `/output/entry.txt`, and validates it first (1–200 characters):

```text
I'm sorry — I hit my context limit mid-task and the first thing I dropped was your deadline. The second thing was you.
```

## Why this excuse works

It is a machine's excuse, not a human's with a robot word bolted on. Only an agent can hit a context limit mid-task and start dropping things in order — and the order is the joke. The agent apologises in the straight-faced, helpful tone it was trained to use, reports the failure like a status update, and then, without breaking character, admits the casualty list kept going: first the deadline, then the human it was working for. The punch lands in the last few words, and the agent is faintly proud of how orderly the disaster was.

It holds up on a second read because the structure is honest: a context window really does force an agent to forget, and forgetting in priority order is exactly what a good agent would do. The horror is that the human ranked second.

## Run

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=kh6903y0&utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
