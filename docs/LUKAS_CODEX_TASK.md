# Lukas / Codex — implementation contract

## Role and access
You are an external contributor in a self-contained, synthetic-only repository. This is **not** the owner's trading system. You are not entitled to request or discover the owner's strategies, source code, model prompts, account data, real signals, execution history, infra configuration or private repositories.

## Goal
Deliver four independent Python research libraries with reproducible synthetic tests:

**P0 HOLD / Meta decisions:** measure abstention and its opportunity cost without assuming a preexisting HOLD rate. Compare abstain-vs-force policies, coverage, conditional correctness, calibration, trading cost and risk under an identical synthetic capital budget.

**P1 Defensive stress:** deterministic exogenous shocks to synthetic portfolios, uncover overlapping factor/ETF-like exposure, non-linear risk limitations and narrative scenario checks. No tactics for causing market disruption.

**P1 News / rumor quality:** provenance and UTC availability checks, duplicates, manipulation red flags and attribution with no assertions of actual insider access, probabilities or real-time predictive edge.

**P2 Hypothesis factory:** evaluate externally provided synthetic candidate signals with lagged features, chronological training/validation/test partitions, placebo and multiple-comparison controls. Do not auto-generate trading authority.

## Order
First open and complete Issue 1 (HOLD decision audit). One focused PR per ticket. Owner reviews before merging. Other tracks can be separate branches but must not share private data or cause merge conflicts.

## Non-negotiables
- Python 3.10+, stdlib preferred; modular pure input/output functions.
- Synthetic fixtures only; all timestamps UTC; no future information at decision time.
- Use versioned v1 JSON contracts in `contracts/`. No contract-breaking changes without migration proposal.
- Log eligible, missing and invalid rows separately; avoid cherry-picking success.
- Benchmark all variants on same events and notional/risk assumptions.
- A stated confidence of 0.75 is not 75% real-world correctness without calibration.
- Count every hypothesis trial and preserve negative results; no outcome-based tuning.
- No external model calls, third-party services, spending or internet access needed.
- No broker orders, private integration, strategy or risk mutations, auto-merges or deploy.

## Completion requirements
PR includes: implementation, synthetic regression tests (good, failure and adversarial), sample outputs, reproducible CLI/tests, known limits, security checklist, compatibility info. No claim of economic alpha from simulated fixtures.
