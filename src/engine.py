import json
from pathlib import Path
from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "profile.json"


def load_profile() -> list[dict[str, Any]]:
    """Load fictional demonstration-profile records."""
    with DATA_PATH.open("r", encoding="utf-8") as file:
        records = json.load(file)
    if not isinstance(records, list):
        raise ValueError("Profile data must be a JSON list.")
    return records


def retrieve_candidates(
    query: str,
    records: list[dict[str, Any]],
    top_k: int = 10,
) -> list[dict[str, Any]]:
    """Retrieve candidates using lexical TF-IDF similarity (baseline only)."""
    if not query.strip() or not records:
        return []
    texts = [str(record["content"]) for record in records]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(texts + [query])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()
    ranked = sorted(zip(records, scores), key=lambda pair: pair[1], reverse=True)
    return [
        {**record, "retrieval_score": float(score)}
        for record, score in ranked[:top_k]
        if score > 0
    ]


def necessity_baseline(query: str, record: dict[str, Any]) -> tuple[bool, float, str]:
    """Apply phrase rules; score is a heuristic, not a probability or guarantee."""
    q = query.lower()
    category = record["category"]
    rules = [
        (("skill", "programming", "technical"), {"skills", "projects", "experience", "certifications"}),
        (("project", "built", "developed"), {"projects", "skills", "experience"}),
        (("internship", "work experience", "job"), {"experience", "skills", "projects"}),
        (("education", "university", "college", "degree"), {"education", "academic_performance", "certifications"}),
        (("cgpa", "grade", "marks", "academic performance"), {"academic_performance", "education"}),
        (("contact", "phone", "email", "reach"), {"contact"}),
        (("where", "location", "live"), {"location"}),
    ]
    required: set[str] = set()
    for phrases, categories in rules:
        if any(phrase in q for phrase in phrases):
            required.update(categories)

    if category in {"contact", "location"} and category not in required:
        return False, 0.05, "Sensitive or unrelated category withheld by default."
    if required and category in required:
        return True, 0.90, "Category matches a query-intent rule."
    return False, 0.10, "No necessity rule matched this category."


def run_privera(query: str) -> dict[str, Any]:
    """Retrieve candidate records, apply baseline rules, and explain decisions."""
    records = load_profile()
    candidates = retrieve_candidates(query, records)
    disclosed: list[dict[str, Any]] = []
    withheld: list[dict[str, Any]] = []
    for record in candidates:
        keep, score, reason = necessity_baseline(query, record)
        item = {**record, "necessity_score": score, "decision_reason": reason}
        (disclosed if keep else withheld).append(item)

    answer = (
        " ".join(item["content"] for item in disclosed)
        if disclosed
        else "The baseline did not select enough information to answer this query."
    )
    return {
        "answer": answer,
        "candidates": candidates,
        "disclosed": disclosed,
        "withheld": withheld,
    }
