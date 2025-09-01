from __future__ import annotations
from pathlib import Path
from typing import List
import joblib

_model = None
_known_skills: List[str] = []

def load_model(model_path: Path) -> None:
    """Load the joblib pipeline (TF-IDF + NearestNeighbors) and cache known skills."""
    global _model, _known_skills
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found at {model_path}. "
            "Run `python backend/model/train.py` first to create it."
        )
    _model = joblib.load(model_path)
    # keep a small, curated list of skills for UI hints (from training data)
    _known_skills = sorted(_model.get("catalog_skills", []))

def list_known_skills() -> List[str]:
    return _known_skills

def recommend(skills: List[str], top_k: int = 3) -> List[str]:
    """Return top-k careers closest to the user's skill text."""
    assert _model is not None, "Model not loaded. Call load_model() on startup."
    text = ", ".join([s.strip().lower() for s in skills if s.strip()])
    if not text:
        return []
    vec = _model["vectorizer"].transform([text])
    distances, idx = _model["nn"].kneighbors(vec, n_neighbors=min(top_k, len(_model["careers"])))
    # idx is shape (1, k)
    result = [_model["careers"][i] for i in idx[0]]
    return result
