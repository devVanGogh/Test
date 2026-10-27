# Contributing

1. Pick a ticket from GitHub Issues. Start with P0 HOLD analysis.
2. Open a topic branch `feature/issue-number-short-name`. Do not push directly to `main`.
3. Work only with synthetic inputs and generic public contracts.
4. Write deterministic unit tests (positive, negative, adversarial), include sample size, eligibility and assumptions.
5. Run `python -m unittest discover -s tests -v` and `python tools/safe_share_check.py`.
6. Open a PR using the template; report test results, tradeoffs, failure cases and security review.
7. Owner reviews and merges manually. Never deploy or link to any private system.

No hidden calls to APIs, no scraping of unauthorized sources, no new dependencies without approval, no `eval`/`exec`, no speculative trading promises.

The output of an external module is a **research hypothesis or metric**, not authority to place orders.
