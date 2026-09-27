"""NEPSE Research API.

Run:  uvicorn api.main:app --reload     then open http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI

app = FastAPI(title="NEPSE Research API")


@app.get("/health")
def health():
    return {"status": "ok"}


# Week 1, Tuesday: GET /index?start=YYYY-MM-DD&end=YYYY-MM-DD
#   returns [{"date": ..., "close": ...}, ...] using nepse_research.db.load_nepse_index
# Week 1, Wednesday: a bad date gives a 422 error, not a crash
# Week 1, Thursday: a Pydantic response model
