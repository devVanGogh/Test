# Signal Research Sandbox

**Synthetic-only external development workspace** for independent research components. All code is research-only, portable and strictly disconnected from any owner's trading software.

## Four research tracks

| Priority | Track | Research question | Lead deliverable |
|---|---|---|---|
| P0 | Decision abstention / HOLD | Does abstaining help, and when does forcing a decision reduce economic value? | Deterministic coverage, calibration and economics evaluator |
| P1 | Defensive portfolio stress | Can simulated stress reveal hidden common-factor concentrations? | Synthetic scenario evaluator |
| P1 | News & rumor quality | Can evidence quality filters reject duplicate/manipulated messages without losing useful information? | Provenance and credibility features |
| P2 | Research hypothesis tests | Can novel conditional signals survive chronological out-of-sample and placebo checks? | Bounded walk-forward evaluator |

**Claims under test, not facts:** “uncensored” models outperform standard ones; commercial models choose HOLD in 70% of cases; self-reported 75% confidence implies 75% accuracy. These require evidence.

## For Lukas and Codex

Start with [the development contract](docs/LUKAS_CODEX_TASK.md), [hypothesis test matrix](docs/THEORY_TEST_MATRIX.md), [security rules](SECURITY.md) and [contribution workflow](CONTRIBUTING.md). Work through GitHub Issues, one branch and PR per issue. The repository contains no production connectors or live trading authority.

```bash
python -m unittest discover -s tests -v
python tools/safe_share_check.py
```

Python 3.10+; standard library only for starter code. Synthetic examples illustrate formats, **not validated trading alpha**.

## Data & integration boundary

Only fabricated price series, fake accounts, mock signals and generic JSON contracts. NEVER include real positions, historical proprietary signal ledgers, confidential models/prompts, order/fill data, private repo links, credentials, internal hosts or restricted news archives. Any private integration must be separately reviewed and implemented by the owner.

[Task board (Issues)](../../issues) · [Theory tests](docs/THEORY_TEST_MATRIX.md) · [Security](SECURITY.md)

**Research first. Risk always. No deployment or trading.**
