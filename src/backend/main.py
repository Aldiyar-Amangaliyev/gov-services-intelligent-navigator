from typing import List, Optional
from fastapi import FastAPI, Query
from src.backend.models import (
    BenchmarkMetrics,
    LifeSituationBundle,
    NavigationResponse,
    PublicServicePassport,
    SearchRequest
)
from src.nlp_engine.navigator import KNOWLEDGE_BASE, LIFE_SITUATIONS, IntelligentServiceNavigator

app = FastAPI(
    title="Intelligent Navigation System for Public Services of the Republic of Kazakhstan",
    description="Hybrid NLP semantic search, life-situation routing, and catalog API for RK public services",
    version="0.1.0-pre-defense-1"
)

navigator = IntelligentServiceNavigator()


@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "ok",
        "service": "gov-services-intelligent-navigator",
        "version": "pre-defense-1",
        "catalog_size": len(KNOWLEDGE_BASE),
        "life_situations_count": len(LIFE_SITUATIONS)
    }


@app.get("/api/v1/services", response_model=List[PublicServicePassport], tags=["Catalog"])
def list_services(
    category: Optional[str] = Query(default=None),
    applicant_type: Optional[str] = Query(default=None),
    online_only: bool = Query(default=False)
):
    results = []
    for item in KNOWLEDGE_BASE:
        if category and category.lower() not in item["category"].lower():
            continue
        if applicant_type and item["applicant_type"] != applicant_type:
            continue
        if online_only and not item["is_online"]:
            continue
        results.append(PublicServicePassport(**item, semantic_score=1.0))
    return results


@app.get("/api/v1/life-situations", response_model=List[LifeSituationBundle], tags=["Life Situations"])
def list_life_situations():
    return [LifeSituationBundle(**bundle) for bundle in LIFE_SITUATIONS]


@app.post("/api/v1/navigate/search", response_model=NavigationResponse, tags=["NLP Navigation"])
def semantic_navigate(payload: SearchRequest):
    detected_cat, keywords, ranked, recommendations, elapsed_ms = navigator.navigate(
        query=payload.query,
        applicant_type=payload.applicant_type,
        online_only=payload.online_only,
        top_k=payload.top_k
    )
    passports = [PublicServicePassport(**item) for item in ranked]
    return NavigationResponse(
        query=payload.query,
        detected_category=detected_cat,
        extracted_keywords=keywords,
        execution_time_ms=elapsed_ms,
        results=passports,
        recommended_next_steps=recommendations
    )


@app.get("/api/v1/evaluate/benchmark", response_model=BenchmarkMetrics, tags=["Evaluation"])
def run_benchmark():
    metrics = navigator.evaluate_benchmark()
    return BenchmarkMetrics(**metrics)
