from typing import List, Optional
from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=2)
    language: str = Field(default="ru", pattern="^(ru|kz|en)$")
    applicant_type: Optional[str] = Field(default=None)
    online_only: bool = Field(default=False)
    top_k: int = Field(default=3, ge=1, le=10)


class PublicServicePassport(BaseModel):
    service_id: str
    title: str
    category: str
    applicant_type: str
    semantic_score: float = 0.0
    delivery_time: str
    cost: str
    is_online: bool
    required_documents: List[str]
    official_url: str


class NavigationResponse(BaseModel):
    query: str
    detected_category: str
    extracted_keywords: List[str]
    execution_time_ms: float
    results: List[PublicServicePassport]
    recommended_next_steps: List[str]


class LifeSituationBundle(BaseModel):
    bundle_id: str
    title: str
    description: str
    service_ids: List[str]


class BenchmarkMetrics(BaseModel):
    queries_evaluated: int
    hybrid_recall_at_1: float
    hybrid_recall_at_3: float
    hybrid_mrr: float
    baseline_recall_at_1: float
    baseline_recall_at_3: float
    baseline_mrr: float
