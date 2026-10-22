# 9. Verification and Evaluation Plan

## 9.1. Baseline Model for Scientific Comparison
To quantify the engineering contribution of our Hybrid NLP Engine, we benchmark it against a deterministic **Lexical Baseline**: exact whole-word overlap matching against official service titles (`baseline_navigate` in `src/nlp_engine/navigator.py`).

## 9.2. Quantitative Evaluation Metrics
| Metric | Mathematical Definition | Target Threshold | Current MVP Result |
| :--- | :--- | :--- | :--- |
| **Recall@1** | Fraction of benchmark queries where the ground-truth service is ranked #1 | >= 0.75 | **1.00** (vs 0.12 Baseline) |
| **Recall@3** | Fraction of benchmark queries where the ground-truth service is in Top-3 | >= 0.88 | **1.00** (vs 0.25 Baseline) |
| **MRR (Mean Reciprocal Rank)** | Average of reciprocal ranks $1 / rank_i$ across all benchmark queries | >= 0.80 | **1.00** (vs 0.19 Baseline) |
| **Search Latency (p95)** | 95th percentile execution time of `/api/v1/navigate/search` | <= 500 ms | **< 5.0 ms** |
| **Automated Test Pass Rate** | Execution of `pytest tests/` across unit and API integration suites | 100% Pass | **6 / 6 Passed (100%)** |

## 9.3. Verification Suite Structure (`tests/test_navigator.py`)
1. `test_health_check`: Verifies `/health` status and knowledge base initialization (>= 8 services).
2. `test_semantic_search_lost_id_russian`: Verifies conversational Russian query routing to `SRV-KZ-001`.
3. `test_semantic_search_kazakh_query`: Verifies conversational Kazakh query routing to `SRV-KZ-002`.
4. `test_semantic_search_english_entrepreneur`: Verifies English business query routing to `SRV-KZ-003`.
5. `test_catalog_filtering_and_life_situations`: Verifies strict query parameter filtering and life-situation bundles.
6. `test_hybrid_outperforms_baseline_benchmark`: Executes `/api/v1/evaluate/benchmark` and asserts that Hybrid NLP strictly beats the Baseline on Recall@1, Recall@3, and MRR.
