"""Analyze abstention / coverage without producing trade instructions."""
from collections import Counter
from math import isfinite

ACTIONS = frozenset(("BUY", "SELL", "HOLD"))

def audit_decisions(rows):
    rows = list(rows)
    counts, labeled = Counter(), []
    for item in rows:
        action = item["action"]
        if action not in ACTIONS:
            raise ValueError("invalid action")
        counts[action] += 1
        label = item.get("outcome_correct")
        if action != "HOLD" and label is not None:
            if type(label) is not bool:
                raise ValueError("outcome_correct must be bool or null")
            labeled.append(label)
    n = len(rows)
    return {
        "sample_size": n,
        "counts": {key: counts[key] for key in ("BUY", "SELL", "HOLD")},
        "hold_rate": counts["HOLD"] / n if n else None,
        "trade_coverage": (n - counts["HOLD"]) / n if n else None,
        "labeled_trade_count": len(labeled),
        "conditional_accuracy": sum(labeled) / len(labeled) if labeled else None,
    }

def brier_score(probabilities, outcomes):
    """Only use probabilities externally verified as meaningful, not raw LLM conviction."""
    probabilities, outcomes = list(probabilities), list(outcomes)
    if not probabilities or len(probabilities) != len(outcomes):
        raise ValueError("nonempty equal-length input required")
    for p, y in zip(probabilities, outcomes):
        if type(p) not in (float, int) or not isfinite(p) or not 0 <= p <= 1:
            raise ValueError("invalid probability")
        if type(y) is not bool:
            raise ValueError("outcome label must be bool")
    return sum((p - int(y)) ** 2 for p, y in zip(probabilities, outcomes)) / len(outcomes)
