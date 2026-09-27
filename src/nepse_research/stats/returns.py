"""Week 1 exercises: returns, volatility, drawdown.

Write each function yourself; `pytest` tells you when it's right.
Each takes a pandas Series indexed by date and returns a Series or a number.
Use pandas' own methods where they fit; the point is knowing which one and why.
"""
import pandas as pd


def simple_returns(prices: pd.Series) -> pd.Series:
    """Day-over-day simple return: p_t / p_{t-1} - 1.

    The first day has no previous price, so drop it (the result is one shorter than `prices`).
    Example: [100, 110, 99] -> [0.10, -0.10]
    """
    raise NotImplementedError("Week 1, Tuesday")


def log_returns(prices: pd.Series) -> pd.Series:
    """Day-over-day log return: ln(p_t / p_{t-1}). Drop the first day, as above.

    Log returns add up across days: the sum of daily log returns = ln(last / first).
    """
    raise NotImplementedError("Week 1, Tuesday")


def summary_stats(returns: pd.Series) -> dict:
    """Return {"mean", "std", "skew", "kurtosis"} of `returns`, as plain floats.

    Use pandas' sample definitions: std with ddof=1, and `kurtosis` is EXCESS kurtosis
    (0 for a normal distribution; fat tails give > 0).
    """
    raise NotImplementedError("Week 1, Wednesday")


def annualized_volatility(returns: pd.Series, periods_per_year: int) -> float:
    """Sample standard deviation of `returns` scaled to one year: std * sqrt(periods_per_year).

    NEPSE trades Sunday to Thursday, about 240 days a year. Gold trades about 260.
    """
    raise NotImplementedError("Week 1, Thursday")


def rolling_volatility(returns: pd.Series, window: int, periods_per_year: int) -> pd.Series:
    """Annualized volatility over a moving window of `window` days.

    The first `window - 1` values have too little data: leave them NaN.
    """
    raise NotImplementedError("Week 1, Thursday")


def max_drawdown(prices: pd.Series) -> float:
    """The worst fall from a previous peak, as a negative fraction.

    Example: [100, 120, 90, 130, 65] -> the peak 130 fell to 65 -> -0.5
    Hint: compare each price with the highest price seen so far.
    """
    raise NotImplementedError("Week 1, Friday")
