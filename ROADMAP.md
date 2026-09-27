# Roadmap: 13 weeks

Six 1-hour blocks a day: **Stats · DS/ML · Backend · LLM · Research · Content**.
On a bad day, do only three: **DS/ML, Research, commit.**

**Two repos, one plan:**
- **`nepse-research`** (this repo) is the **practice gym**: exercises with tests, stats notebooks, reading notes, LLM
  work.
- **[`nepse-sentinel`](https://github.com/Pukar99/nepse-sentinel)** is the **real project**: self-supervised detection of
  trade-based manipulation on NEPSE. The course's practice builds its baselines and its transformer stream (Stream 2).
  The graph neural network (Stream 1) and fusion come in 2027.

Each week has one **deliverable**. The week counts as done only when that deliverable is public.
🛡️ marks work that goes into Sentinel.

---

## Phase 1: Foundations (weeks 1–4). Learn the basics, build Sentinel's baselines

### Week 1 (Sep 29 – Oct 5): returns and fat tails
- **Stats:** simple vs log returns, mean/variance/skew/kurtosis, fat tails, volatility clustering, drawdown
- **DS:** load the NEPSE index and XAUUSD, then compare their return distributions
- **Backend:** FastAPI basics, one endpoint reading the NEPSE index, Dockerfile
- **LLM:** Karpathy *Zero to Hero* 1–2 (micrograd, bigram)
- **Research:** *Attention Is All You Need*, 3-pass reading; outline Paper 1
- **Deliverable:** `notebooks/01_fat_tails.ipynb` plus a post with its main chart

### Week 2 (Oct 6 – 12): distributions, z-scores, abnormal volume
- **Stats:** probability, z-scores, central limit theorem, the bootstrap
- **DS:** 🛡️ per-stock *normal* volume and price range (rolling median/MAD), then flag days far outside it
- **Backend:** `/stocks/{symbol}` endpoint, query parameters, error handling
- **LLM:** Karpathy *Let's build GPT*: code it yourself
- **Research:** a survey of market-manipulation detection (find one on Google Scholar); DLinear paper
- **Deliverable:** `02_abnormal_volume.ipynb`: the 20 most abnormal stock-days since 2014, each checked against the news

### Week 3 (Oct 13 – 19): hypothesis tests, concentration, rule baselines
- **Stats:** hypothesis tests, p-values, multiple testing (why flagging thousands of days creates false alarms)
- **DS:** 🛡️ **Baseline 1: rules**. Broker concentration (HHI) per stock-day from the floorsheet, plus volume-spike
  rules
- **Backend:** pytest for the API, GitHub Actions CI
- **LLM:** Hugging Face `transformers`, tokenizers, run a 1–3B model on Colab
- **Research:** **Paper 1** (data audit): Data and Method sections
- **Deliverable:** 🛡️ the rule baseline as code in `nepse-sentinel`, with tests

### Week 4 (Oct 20 – 26): regression, anomaly detection, the event calendar
- **Stats:** OLS regression, residuals as "unexpected" moves
- **DS:** 🛡️ **Baseline 2: Isolation Forest** on stock-day features. 🛡️ Event calendar v1 (bonus/rights/unlock dates,
  Sentinel risks R1–R2)
- **Backend:** 🛡️ `/alerts?date=` endpoint serving the baseline scores
- **LLM:** embeddings, prompt engineering
- **Research:** **Paper 1:** Results section. 🛡️ Collect SEBON enforcement cases into a table (the validation set)
- **Deliverable:** both baselines scored on the same stock-days; the SEBON case table

## Phase 2: Build (weeks 5–9). Learn deep learning, build Sentinel's Stream 2

### Week 5 (Oct 27 – Nov 2): time series
- **Stats:** stationarity, ADF test, ACF/PACF, ARIMA
- **DS:** 🛡️ build per-stock sequences (price, volume, NEPSE index, sector index) for the transformer, split by time
- **Backend:** pgvector in Postgres
- **LLM:** RAG v1 over NEPSE announcements and news (it also answers "what happened to this stock that day?" for
  alerts)
- **Research:** **Paper 1 finished and posted as a preprint (SSRN/arXiv)**
- **Deliverable:** Paper 1 is public

### Week 6 (Nov 3 – 9): PyTorch and self-supervised learning
- **Stats:** GARCH (the volatility a model should *expect*)
- **DS:** PyTorch basics; 🛡️ **Baseline 3: LSTM** autoencoder (Sentinel goal G3)
- **Backend:** RAG endpoint that cites its sources
- **LLM:** evaluate RAG: does it find the right chunks, and are answers faithful to them?
- **Research:** read masked pretraining for time series (PatchTST self-supervised, TS2Vec). Write the **Paper 2**
  question and protocol **before** seeing results
- **Deliverable:** LSTM baseline scored

### Week 7 (Nov 10 – 16): the transformer
- **Stats:** Bayesian basics (a small PyMC model)
- **DS:** 🛡️ **Stream 2**: a PatchTST-style transformer you write yourself, pretrained by masking and reconstructing
  patches of price/volume
- **Backend:** background jobs for training runs
- **LLM:** read the LoRA and QLoRA papers; build a 1–2k example dataset (NEPSE news → summary / what happened)
- **Research:** experiment protocol frozen in `nepse-sentinel/docs/experiments.md`
- **Deliverable:** 🛡️ Stream 2 pretrains end to end

### Week 8 (Nov 17 – 23): anomaly scores and fair comparison
- **Stats:** precision@k, bootstrap confidence intervals, false-positive rates per cause
- **DS:** 🛡️ reconstruction error → anomaly score; compare with all 3 baselines on SEBON cases (Sentinel goal G3)
- **Backend:** authentication, rate limits, logging
- **LLM:** QLoRA fine-tune of Qwen2.5-3B or Llama-3.2-3B (PEFT + TRL, free Colab/Kaggle GPU)
- **Research:** results tables
- **Deliverable:** the main table: does Stream 2 beat the baselines?

### Week 9 (Nov 24 – 30): false alarms and release
- **Stats:** effect sizes, reading ablations
- **DS:** 🛡️ false alarms per cause (corporate actions, unlocks, index effects; goal G5); ablations; W&B tracking
- **Backend:** Docker Compose; deploy the alerts API
- **LLM:** base vs fine-tuned vs RAG; publish to Hugging Face with a model card
- **Research:** Paper 2 results written
- **Deliverable:** live alerts API plus the Hugging Face model

## Phase 3: Ship (weeks 10–13)

- **Week 10 (Dec 1 – 7):** 🛡️ Sentinel dashboard in HTML/CSS (anonymized broker IDs, concern tiers: never
  accusations) · the LLM explains each alert · Paper 2 Intro, Related Work and Method
- **Week 11 (Dec 8 – 14):** one-command reproduction · Paper 2 complete · stats notebooks cleaned up
- **Week 12 (Dec 15 – 21):** feedback from 2–3 people · 3-minute demo video · all READMEs polished
- **Week 13 (Dec 22 – 28):** Paper 2 preprint · portfolio page · launch post · 90-day look-back

**Paper 2:** *NEPSE Sentinel v1: Self-Supervised Detection of Trade-Based Manipulation on the Nepal Stock Exchange*
(the transformer stream vs rule, Isolation Forest and LSTM baselines, validated on SEBON enforcement cases).

**2027:** Stream 1 (GNN on the daily broker graph), fusion, all six manipulation classes.

## Reading list (free)

- Statistics: StatQuest (YouTube); *An Introduction to Statistical Learning with Python* (statlearning.com)
- Time series: *Forecasting: Principles and Practice* (otexts.com/fpp3)
- Deep learning: Karpathy, *Neural Networks: Zero to Hero* (karpathy.ai/zero-to-hero.html)
- LLMs: Hugging Face LLM course; PEFT and TRL docs
- Finance ML: López de Prado, *Advances in Financial Machine Learning*, chapters 3, 7 and 8
- How to read papers: S. Keshav, *How to Read a Paper* (3-pass method)
