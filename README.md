# NEPSE Research Lab

My 90-day build (Sep 29 → Dec 28, 2026): **statistics, data science, backend, LLMs and research**, all learned by building
one project on real NEPSE and XAUUSD market data.

This repo is the **practice gym**. The real project is **[NEPSE Sentinel](https://github.com/Pukar99/nepse-sentinel)**
(self-supervised detection of trade-based manipulation on NEPSE): the course's practice builds its baselines and its
transformer stream, written up as a paper, served by an API, and explained by a fine-tuned LLM.

> Not financial advice. This is research and engineering, not trading signals.

## Progress

| Week | Dates | Theme | Status |
|---|---|---|---|
| [1](weeks/week-01.md) | Sep 29 – Oct 5 | Returns, fat tails, FastAPI, transformer basics | 🟡 in progress |
| 2 | Oct 6 – Oct 12 | Z-scores, abnormal volume, a GPT built from scratch | ⬜ |
| 3 | Oct 13 – Oct 19 | Hypothesis tests, Sentinel rule baseline (HHI), CI | ⬜ |
| 4 | Oct 20 – Oct 26 | Regression, Isolation Forest, SEBON cases | ⬜ |
| 5–9 | Oct 27 – Nov 30 | Build: Sentinel's transformer stream, RAG, QLoRA | ⬜ |
| 10–13 | Dec 1 – Dec 28 | Ship: Sentinel dashboard, two papers, launch | ⬜ |

The full plan is in [ROADMAP.md](ROADMAP.md). Each week gets its own file in [`weeks/`](weeks/) with day-by-day tasks.

## What's where

| Folder | Track | What goes in it |
|---|---|---|
| `src/nepse_research/stats/` | Statistics | Functions you write yourself; `tests/` checks them |
| `notebooks/` | Data science | One notebook per finding, numbered |
| `api/` | Backend | The FastAPI service |
| `llm/` | LLM | RAG and QLoRA fine-tuning |
| `research/` | Research | Reading notes and the two papers |
| `content/` | Content | Post drafts and a log of what was published |
| `journal/` | Review | The Sunday review, one file per week |

## Data

This project reads, never writes, two local databases:

- **`nepse_trading_db`** (from [nepse-data](https://github.com/Pukar99/nepse-data)): the NEPSE index since 1997 and daily
  prices per stock.
- **AlgoGold's database**: XAUUSD daily and 1-minute candles from MetaTrader 5.

Loaders are in `src/nepse_research/db.py`.

## Run it

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
pip install -e .
copy .env.example .env          # then fill in the two database URLs
pytest                          # your exercises: red until you solve them
```

## Rules

1. **Try it yourself first**, then ask AI. Never commit code you can't explain line by line.
2. **Commit every day**, even if it's small.
3. **Every week ends with something someone else can see**: a notebook, an endpoint or a post.
