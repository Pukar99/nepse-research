# Roadmap: 13 weeks

Six 1-hour blocks a day: **Stats · DS/ML · Backend · LLM · Research · Content**.
On a bad day, do only three: **DS/ML, Research, commit.**

Each week has one **deliverable**. The week counts as done only when that deliverable is public.

---

## Phase 1: Foundations (weeks 1–4)

### Week 1 (Sep 29 – Oct 5): returns and fat tails
- **Stats:** simple vs log returns, mean/variance/skew/kurtosis, fat tails, volatility clustering, drawdown
- **DS:** load the NEPSE index and XAUUSD from your databases, then compare their return distributions
- **Backend:** FastAPI basics, one endpoint reading the NEPSE index, Dockerfile
- **LLM:** Karpathy *Zero to Hero* 1–2 (micrograd, bigram)
- **Research:** *Attention Is All You Need*, 3-pass reading; outline Paper 1
- **Deliverable:** `notebooks/01_fat_tails.ipynb` plus a post with its main chart

### Week 2 (Oct 6 – 12): probability and sampling
- **Stats:** probability rules, central limit theorem, sampling, the bootstrap
- **DS:** NEPSE EDA: day-of-week effect, Dashain/Tihar months, sector correlations
- **Backend:** `/stocks/{symbol}` endpoint, query parameters, error handling
- **LLM:** Karpathy *Let's build GPT*: code it yourself
- **Research:** DLinear, *Are Transformers Effective for Time Series Forecasting?*
- **Deliverable:** `02_calendar_effects.ipynb` with bootstrap confidence intervals

### Week 3 (Oct 13 – 19): hypothesis testing and first baselines
- **Stats:** hypothesis tests, p-values, multiple testing (why most backtests lie)
- **DS:** features; logistic regression predicting up/down, split by time
- **Backend:** pytest for the API, GitHub Actions CI
- **LLM:** Hugging Face `transformers`, tokenizers, run a 1–3B model on Colab
- **Research:** PatchTST paper. **Paper 1** (data audit): write the Data and Method sections
- **Deliverable:** CI green; baseline results table

### Week 4 (Oct 20 – 26): regression and walk-forward validation
- **Stats:** OLS with `statsmodels`, checking the assumptions, residuals
- **DS:** walk-forward validation, data leakage, XGBoost baseline
- **Backend:** AlgoGold (Express) calls this API for a signal
- **LLM:** embeddings, prompt engineering
- **Research:** a table of 10 papers. **Paper 1:** Results section
- **Deliverable:** `04_walk_forward.ipynb`; all baselines scored the same way

## Phase 2: Build (weeks 5–9)

### Week 5 (Oct 27 – Nov 2): time series
- **Stats:** stationarity, ADF test, ACF/PACF, ARIMA
- **DS:** ARIMA baseline
- **Backend:** pgvector in Postgres
- **LLM:** RAG v1 over NEPSE announcements and news
- **Research:** **Paper 1 finished and posted as a preprint (SSRN/arXiv)**
- **Deliverable:** Paper 1 is public

### Week 6 (Nov 3 – 9): volatility
- **Stats:** GARCH
- **DS:** PyTorch basics, LSTM baseline
- **Backend:** RAG endpoint that cites its sources
- **LLM:** evaluate RAG: does it find the right chunks, and are answers faithful to them?
- **Research:** **Paper 2** research question, hypothesis and method
- **Deliverable:** LSTM on the baseline table; RAG demo

### Week 7 (Nov 10 – 16): the transformer
- **Stats:** Bayesian basics (a small PyMC model)
- **DS:** a PatchTST-style transformer you write yourself in PyTorch
- **Backend:** background jobs for training runs
- **LLM:** read the LoRA and QLoRA papers; build a 1–2k example dataset
- **Research:** experiment protocol fixed and written down before looking at results
- **Deliverable:** the transformer trains end to end

### Week 8 (Nov 17 – 23): fair comparison
- **Stats:** Diebold–Mariano test, bootstrap confidence intervals, Sharpe and deflated Sharpe ratio
- **DS:** transformer vs every baseline, walk-forward
- **Backend:** authentication, rate limits, logging
- **LLM:** QLoRA fine-tune of Qwen2.5-3B or Llama-3.2-3B (PEFT + TRL, free Colab/Kaggle GPU)
- **Research:** results tables
- **Deliverable:** the main results table, with significance tests

### Week 9 (Nov 24 – 30): ablations and release
- **Stats:** effect sizes, reading ablations
- **DS:** ablations (lookback, patch size, features); track experiments in W&B
- **Backend:** Docker Compose; deploy
- **LLM:** base vs fine-tuned vs RAG; publish to Hugging Face with a model card
- **Research:** Paper 2 results written
- **Deliverable:** live API plus the Hugging Face model

## Phase 3: Ship (weeks 10–13)

- **Week 10 (Dec 1 – 7):** backtest with real NEPSE costs (commission, circuit limits) · dashboard in HTML/CSS · Paper 2
  Intro, Related Work and Method
- **Week 11 (Dec 8 – 14):** one-command reproduction · Paper 2 complete · stats notebooks cleaned up
- **Week 12 (Dec 15 – 21):** feedback from 2–3 people · 3-minute demo video · all READMEs polished
- **Week 13 (Dec 22 – 28):** Paper 2 preprint · portfolio page · launch post · 90-day look-back

## Reading list (free)

- Statistics: StatQuest (YouTube); *An Introduction to Statistical Learning with Python* (statlearning.com)
- Time series: *Forecasting: Principles and Practice* (otexts.com/fpp3)
- Deep learning: Karpathy, *Neural Networks: Zero to Hero* (karpathy.ai/zero-to-hero.html)
- LLMs: Hugging Face LLM course; PEFT and TRL docs
- Finance ML: López de Prado, *Advances in Financial Machine Learning*, chapters 3, 7 and 8
- How to read papers: S. Keshav, *How to Read a Paper* (3-pass method)
