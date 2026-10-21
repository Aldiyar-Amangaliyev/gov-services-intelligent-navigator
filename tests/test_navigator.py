from fastapi.testclient import TestClient
from src.backend.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["catalog_size"] >= 8
    assert data["life_situations_count"] >= 3


def test_semantic_search_lost_id_russian():
    response = client.post(
        "/api/v1/navigate/search",
        json={"query": "потерял удостоверение личности как быстро восстановить", "language": "ru", "top_k": 3}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["detected_category"] == "Documents and Citizenship"
    assert data["results"][0]["service_id"] == "SRV-KZ-001"
    assert data["results"][0]["semantic_score"] >= 0.70
    assert len(data["recommended_next_steps"]) >= 1


def test_semantic_search_kazakh_query():
    response = client.post(
        "/api/v1/navigate/search",
        json={"query": "бала туу бойынша жәрдемақы алу", "language": "kz", "top_k": 2}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["results"][0]["service_id"] == "SRV-KZ-002"
    assert data["detected_category"] == "Family and Social Support"


def test_semantic_search_english_entrepreneur():
    response = client.post(
        "/api/v1/navigate/search",
        json={"query": "how to open a small business shop in kazakhstan", "language": "en", "top_k": 2}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["results"][0]["service_id"] == "SRV-KZ-003"
    assert data["detected_category"] == "Business and Entrepreneurship"


def test_catalog_filtering_and_life_situations():
    response = client.get("/api/v1/services", params={"applicant_type": "business", "online_only": True})
    assert response.status_code == 200
    items = response.json()
    assert len(items) >= 1
    assert all(item["applicant_type"] == "business" for item in items)
    ls_resp = client.get("/api/v1/life-situations")
    assert ls_resp.status_code == 200
    assert len(ls_resp.json()) >= 3


def test_hybrid_outperforms_baseline_benchmark():
    response = client.get("/api/v1/evaluate/benchmark")
    assert response.status_code == 200
    metrics = response.json()
    assert metrics["hybrid_recall_at_3"] >= 0.88
    assert metrics["hybrid_recall_at_1"] > metrics["baseline_recall_at_1"]
    assert metrics["hybrid_mrr"] > metrics["baseline_mrr"]
