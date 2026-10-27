"""Lagged Pearson correlation diagnostic, not an investment strategy."""
from math import isfinite, sqrt

def lagged_pearson(leading, trailing, lag=1):
    """corr(leading[t], trailing[t+lag]); caller must chronologically split datasets."""
    if type(lag) is not int or lag < 1:
        raise ValueError("lag must be positive integer")
    x, y = list(leading), list(trailing)
    if len(x) != len(y) or len(x) - lag < 3:
        raise ValueError("need 3 aligned observations")
    x, y = x[:-lag], y[lag:]
    if any(type(v) not in (int, float) or not isfinite(v) for v in x + y):
        raise ValueError("invalid numeric observation")
    mx, my = sum(x) / len(x), sum(y) / len(y)
    dx, dy = [v-mx for v in x], [v-my for v in y]
    denom = sqrt(sum(v*v for v in dx) * sum(v*v for v in dy))
    if denom == 0:
        return None
    return sum(a*b for a, b in zip(dx, dy)) / denom
