"""Deterministic defensive factor revaluation on entirely fictional portfolios."""
from math import isfinite

def simulate_linear_shock(exposures, factor_shocks):
    """Fractional pnl = sum(signed factor exposure * synthetic factor shock)."""
    if not isinstance(exposures, dict) or not exposures:
        raise ValueError("factor exposures required")
    total = 0.0
    for factor, exposure in exposures.items():
        shock = factor_shocks.get(factor)
        if type(exposure) not in (int, float) or type(shock) not in (int, float):
            raise ValueError("missing/invalid factor shock")
        if not isfinite(exposure) or not isfinite(shock) or shock < -1.0:
            raise ValueError("invalid factor values")
        total += exposure * shock
    return total

def concentration_hhi(long_only_weights):
    weights = list(long_only_weights)
    if not weights or any(type(w) not in (int, float) or not isfinite(w) or w < 0 for w in weights):
        raise ValueError("invalid weights")
    if abs(sum(weights) - 1) > 1e-10:
        raise ValueError("weights must sum to 1")
    return sum(w*w for w in weights)
