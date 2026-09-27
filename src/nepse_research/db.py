"""Read-only loaders for the two local databases this project uses.

Set in `.env` (see `.env.example`):
    NEPSE_DATABASE_URL     nepse_trading_db from the nepse-data project
    ALGOGOLD_DATABASE_URL  AlgoGold's database (XAUUSD candles from MetaTrader 5)
"""
import os
from functools import lru_cache

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()


@lru_cache
def _engine(env_var: str):
    url = os.environ.get(env_var)
    if not url:
        raise RuntimeError(f"{env_var} is not set. Copy .env.example to .env and fill it in.")
    # plain postgresql:// URLs are given the psycopg (v3) driver
    if url.startswith("postgresql://"):
        url = "postgresql+psycopg://" + url[len("postgresql://"):]
    return create_engine(url)


def _read(env_var: str, sql: str, params: dict) -> pd.DataFrame:
    with _engine(env_var).connect() as conn:
        df = pd.read_sql(text(sql), conn, params=params)
    return df


def load_nepse_index(start: str | None = None, end: str | None = None) -> pd.DataFrame:
    """NEPSE composite index, one row per trading day, indexed by date (1997 onward)."""
    df = _read(
        "NEPSE_DATABASE_URL",
        """
        SELECT date, open, high, low, close, volume
        FROM nepse_index
        WHERE (CAST(:start AS date) IS NULL OR date >= CAST(:start AS date))
          AND (CAST(:end AS date) IS NULL OR date <= CAST(:end AS date))
        ORDER BY date
        """,
        {"start": start, "end": end},
    )
    return _finish(df, "date")


def load_stock_prices(symbol: str, start: str | None = None, end: str | None = None) -> pd.DataFrame:
    """Daily OHLCV for one NEPSE stock, e.g. 'NABIL'."""
    df = _read(
        "NEPSE_DATABASE_URL",
        """
        SELECT sp.date, sp.open, sp.high, sp.low, sp.close, sp.volume
        FROM stock_prices sp
        JOIN stocks s ON s.id = sp.stock_id
        WHERE s.symbol = :symbol
          AND (CAST(:start AS date) IS NULL OR sp.date >= CAST(:start AS date))
          AND (CAST(:end AS date) IS NULL OR sp.date <= CAST(:end AS date))
        ORDER BY sp.date
        """,
        {"symbol": symbol.upper(), "start": start, "end": end},
    )
    return _finish(df, "date")


def load_xauusd(interval: str = "1day", start: str | None = None, end: str | None = None) -> pd.DataFrame:
    """XAUUSD candles from AlgoGold ('1day' or '1min').

    Times are broker time stored as if UTC (AlgoGold's convention), so don't convert them to another zone.
    """
    df = _read(
        "ALGOGOLD_DATABASE_URL",
        """
        SELECT time, open, high, low, close
        FROM candles
        WHERE symbol = 'XAUUSD:mt5' AND interval = :interval
          AND (CAST(:start AS timestamptz) IS NULL OR time >= CAST(:start AS timestamptz))
          AND (CAST(:end AS timestamptz) IS NULL OR time <= CAST(:end AS timestamptz))
        ORDER BY time
        """,
        {"interval": interval, "start": start, "end": end},
    )
    return _finish(df, "time")


def _finish(df: pd.DataFrame, index_col: str) -> pd.DataFrame:
    df[index_col] = pd.to_datetime(df[index_col])
    df = df.set_index(index_col)
    # NUMERIC columns arrive as Decimal; turn them into floats for maths
    return df.astype(float)
