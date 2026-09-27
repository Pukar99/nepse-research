# Week 1 (Sep 29 – Oct 5): returns and fat tails

**Goal:** understand how market returns really behave (not like a bell curve), and prove it on NEPSE and gold.

**Deliverable (must be public by Sunday):** `notebooks/01_fat_tails.ipynb` plus one post with its main chart.

Tick each box when it's done. Commit at the end of every day.

---

## Monday, Sep 29

- [ ] **Stats:** simple vs log returns. Watch StatQuest *Logs* (and any short video on log returns).
      Write in `journal/week-01.md`: *why can log returns be added across days but simple returns can't?*
- [ ] **DS:** set up the project. Create `.venv`, run `pip install -r requirements.txt` then `pip install -e .`, fill in
      `.env`, and in Python run `from nepse_research.db import load_nepse_index; load_nepse_index().tail()`.
- [ ] **Backend:** FastAPI tutorial, *First Steps* (fastapi.tiangolo.com/tutorial). Run `uvicorn api.main:app --reload`
      and open `/health` and `/docs`.
- [ ] **LLM:** Karpathy *Zero to Hero*, video 1 (micrograd), first half.
- [ ] **Research:** *Attention Is All You Need* (arxiv.org/abs/1706.03762), **pass 1** only: title, abstract,
      headings, figures, conclusion. 10 minutes. Then read Keshav's *How to Read a Paper*.
- [ ] **Content:** post: "Starting a 90-day build: stats, ML, LLMs and research on NEPSE. Following along here: <repo link>"

## Tuesday, Sep 30

- [ ] **Stats:** mean, variance, standard deviation, skew, kurtosis. What does *excess kurtosis > 0* mean?
- [ ] **DS:** 🧩 **Exercise:** implement `simple_returns` and `log_returns` in `src/nepse_research/stats/returns.py`.
      Run `pytest -k returns` until those tests pass.
- [ ] **Backend:** in `api/main.py`, write `GET /index?start=&end=` returning NEPSE closes as JSON.
- [ ] **LLM:** video 1, second half.
- [ ] **Research:** *Attention* **pass 2**: read carefully, skip the proofs, understand Figure 1. Fill in
      `research/reading-notes.md`.
- [ ] **Content:** commit and update the README progress table.

## Wednesday, Oct 1

- [ ] **Stats:** the normal distribution vs fat tails. What a QQ-plot shows.
- [ ] **DS:** 🧩 implement `summary_stats`. In the notebook: a histogram of NEPSE daily log returns with a normal curve on
      top, then a QQ-plot. How many days moved more than 4σ? (A normal distribution expects almost none.)
- [ ] **Backend:** validate `start`/`end` (a bad date gives a 422 error, not a crash).
- [ ] **LLM:** code micrograd yourself, without looking back at the video.
- [ ] **Research:** start the 10-paper table at the bottom of `research/reading-notes.md`.
- [ ] **Content:** commit.

## Thursday, Oct 2

- [ ] **Stats:** volatility clustering: big moves follow big moves.
- [ ] **DS:** 🧩 implement `annualized_volatility` and `rolling_volatility`. Plot 20-day and 60-day rolling volatility for
      NEPSE. Mark the 2020 COVID closure and the 2021 bull run.
- [ ] **Backend:** a Pydantic response model for `/index`.
- [ ] **LLM:** Karpathy video 2 (makemore / bigram), first half.
- [ ] **Research:** read `nepse-data/docs/DATA_STATE.md` as a researcher: what would a reviewer ask? Write the questions
      into `research/paper1-data-audit/outline.md`.
- [ ] **Content:** commit.

## Friday, Oct 3

- [ ] **Stats:** drawdown. 🧩 implement `max_drawdown`. What was NEPSE's worst drawdown, and when?
- [ ] **DS:** repeat the whole analysis on XAUUSD daily (`load_xauusd()`). Put NEPSE and gold side by side:
      which one has fatter tails? Which one is more volatile?
- [ ] **Backend:** write a Dockerfile for the API, then run `docker build` and `docker run`.
- [ ] **LLM:** video 2, second half; train the bigram model.
- [ ] **Research:** fill in the Paper 1 outline headings: Introduction, Data sources, Method, Findings, Limitations.
- [ ] **Content:** commit. `pytest` should be fully green.

## Saturday, Oct 4: deliverable day

- [ ] Clean up `notebooks/01_fat_tails.ipynb`: a clear title, 3 findings at the top, charts with labels, and a
      conclusion.
- [ ] Post the best chart plus one finding (e.g. "NEPSE had N days beyond 4σ; a bell curve expects ~0").
      Log it in `content/posts.md`.

## Sunday, Oct 5: review (1 hour)

- [ ] Fill in `journal/week-01.md` using the template: what got done, what slipped and why, next week's one goal.
- [ ] Update the progress table in `README.md`.

---

### Done when

- [ ] `pytest` is all green (every function in `stats/returns.py` is written by you)
- [ ] `/index` works in Docker
- [ ] The notebook and the post are public
- [ ] Two papers on the reading table, and the Paper 1 outline exists
