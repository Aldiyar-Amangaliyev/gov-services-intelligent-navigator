# 6. Requirements Specification

All system requirements are prioritized using the **MoSCoW** methodology and paired with objective, testable acceptance criteria.

## 6.1. Functional Requirements (FR)
| Req ID | Requirement Title & Description | Priority | Verifiable Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| **FR-01** | **Conversational Semantic Search:** The system shall accept free-form natural language queries in RU, KZ, and EN and return a ranked list of matching public services. | Must Have | `POST /api/v1/navigate/search` with query *"потерял удостоверение личности как быстро восстановить"* returns `SRV-KZ-001` at rank 1 with `semantic_score >= 0.70`. |
| **FR-02** | **Automated Intent & Category Detection:** The NLP engine shall classify each user query into an official public service domain. | Must Have | Response payload includes `detected_category` matching the top service domain with Macro F1 >= 0.85 on validation queries. |
| **FR-03** | **Keyword Normalization & Extraction:** The system shall strip stopwords/punctuation and return extracted domain tokens. | Must Have | Response payload contains a non-empty `extracted_keywords` list of normalized tokens (length >= 2, no stopwords). |
| **FR-04** | **Multi-Parameter Catalog Filtering:** Users shall filter the catalog by `category`, `applicant_type` (`individual`/`business`), and `online_only`. | Must Have | `GET /api/v1/services?applicant_type=business&online_only=true` returns 100% matching records and zero non-matching records. |
| **FR-05** | **Standardized Service Passport Presentation:** Each service item shall display title, category, timeline, cost, online flag, required documents, and official URL. | Must Have | Every item in `results` passes `PublicServicePassport` Pydantic schema validation with non-empty `required_documents` and `official_url`. |
| **FR-06** | **Life-Situation Next-Step Recommendations:** Search responses shall recommend logically connected follow-up services. | Should Have | Search response includes `recommended_next_steps` containing >= 2 actionable follow-up procedures for the matched life event. |
| **FR-07** | **Bundled Life-Situation Catalog:** Users shall browse pre-packaged multi-service life situations (e.g., Birth of a Child, Starting a Business). | Should Have | `GET /api/v1/life-situations` returns structured life-situation bundles with ordered service IDs. |
| **FR-08** | **Automated Baseline vs. Hybrid Benchmark Endpoint:** The API shall expose an evaluation endpoint comparing the Hybrid NLP ranker against a lexical baseline. | Could Have | `GET /api/v1/evaluate/benchmark` returns quantitative `recall_at_1`, `recall_at_3`, and `mrr` showing Hybrid NLP outperforming Baseline. |

## 6.2. Non-Functional Requirements (NFR)
| Req ID | Category | Requirement Description | Priority | Verifiable Acceptance Criteria |
| :--- | :--- | :--- | :--- | :--- |
| **NFR-01** | Performance | Low response latency for real-time interactive search. | Must Have | 95th percentile `execution_time_ms` <= 500 ms for semantic search and <= 200 ms for catalog filtering. |
| **NFR-02** | Reliability | Deterministic operation and graceful fallback without external API dependencies. | Must Have | System operates 100% offline/on-premise without crashing and passes all automated `pytest` checks. |
| **NFR-03** | Security | Strict input validation and zero hardcoded secrets in version control. | Must Have | `.gitignore` blocks `.env` and secret keys; invalid API payloads (e.g., 1-character query or invalid language code) return HTTP 422. |
| **NFR-04** | Portability | Full Docker containerization of application and database tiers. | Must Have | `Dockerfile` and `docker-compose.yml` build and launch `govnav_backend` and `govnav_postgres` cleanly. |
| **NFR-05** | Maintainability | Clean modular separation between API routing, Pydantic schemas, and NLP engine. | Must Have | Source code is divided into `src/backend/`, `src/nlp_engine/`, `src/frontend/`, and `tests/`. |
