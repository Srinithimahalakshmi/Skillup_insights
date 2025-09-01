from pathlib import Path
from typing import List, Dict, Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.recommender import load_model, recommend, list_known_skills

APP_DIR = Path(__file__).parent
MODEL_PATH = APP_DIR / "model" / "recommender.pkl"

app = FastAPI(title="SkillUp Insight API", version="1.0.0")

# CORS for React dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictRequest(BaseModel):
    skills: List[str]

class PredictResponse(BaseModel):
    recommendations: List[str]
    progress: List[Dict[str, Any]]

@app.on_event("startup")
def _startup() -> None:
    load_model(MODEL_PATH)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/skills", response_model=List[str])
def skills():
    return list_known_skills()

@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    recs = recommend(payload.skills, top_k=3)
    # Simple, deterministic “progress” levels for charting
    progress = [
        {"skill": s, "level": 40 + (abs(hash(s)) % 61)}  # 40..100
        for s in payload.skills
        if s.strip()
    ]
    return {"recommendations": recs, "progress": progress}
