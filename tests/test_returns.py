import math

import numpy as np
import pandas as pd
import pytest

from nepse_research.stats.returns import (
    annualized_volatility,
    log_returns,
    max_drawdown,
    rolling_volatility,
    simple_returns,
    summary_stats,
)


@pytest.fixture
def prices():
    dates = pd.date_range("2026-01-01", periods=3, freq="D")
    return pd.Series([100.0, 110.0, 99.0], index=dates)


def test_simple_returns(prices):
    r = simple_returns(prices)
    assert len(r) == 2
    assert r.index[0] == prices.index[1], "the first return belongs to the second day"
    assert r.tolist() == pytest.approx([0.10, -0.10])


def test_log_returns(prices):
    r = log_returns(prices)
    assert r.tolist() == pytest.approx([math.log(1.1), math.log(0.9)])


def test_log_returns_add_up(prices):
    assert log_returns(prices).sum() == pytest.approx(math.log(99 / 100))


def test_summary_stats_values():
    r = pd.Series([0.01, -0.02, 0.03, 0.00, -0.01, 0.05])
    s = summary_stats(r)
    assert set(s) == {"mean", "std", "skew", "kurtosis"}
    assert s["mean"] == pytest.approx(0.01)
    assert s["std"] == pytest.approx(np.std(r, ddof=1))
    assert all(isinstance(v, float) for v in s.values())


def test_summary_stats_fat_tails():
    rng = np.random.default_rng(0)
    normal = pd.Series(rng.normal(size=100_000))
    fat = pd.Series(rng.standard_t(df=3, size=100_000))
    assert abs(summary_stats(normal)["kurtosis"]) < 0.1, "a normal distribution has ~0 excess kurtosis"
    assert summary_stats(fat)["kurtosis"] > 3, "Student-t with 3 degrees of freedom has fat tails"


def test_annualized_volatility():
    r = pd.Series([0.01, -0.01, 0.02, -0.02])
    assert annualized_volatility(r, 240) == pytest.approx(r.std(ddof=1) * math.sqrt(240))


def test_rolling_volatility():
    r = pd.Series([0.01, -0.01, 0.02, -0.02, 0.03])
    v = rolling_volatility(r, window=3, periods_per_year=240)
    assert len(v) == len(r)
    assert v.iloc[:2].isna().all(), "not enough data for the first window - 1 days"
    assert v.iloc[2] == pytest.approx(r.iloc[:3].std(ddof=1) * math.sqrt(240))
    assert v.iloc[4] == pytest.approx(r.iloc[2:5].std(ddof=1) * math.sqrt(240))


def test_max_drawdown():
    assert max_drawdown(pd.Series([100.0, 120, 90, 130, 65])) == pytest.approx(-0.5)


def test_max_drawdown_only_rising():
    assert max_drawdown(pd.Series([1.0, 2, 3])) == pytest.approx(0.0)
