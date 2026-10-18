# 5. Technology Stack Comparison and Justification

Four core architectural layers were evaluated across 3 industry-standard alternatives each.

## 5.1. Technology Trade-Off Matrix
| Architectural Layer | Option 1 (Selected) | Option 2 | Option 3 | Engineering Justification for Selection |
| :--- | :--- | :--- | :--- | :--- |
| **1. Backend API Framework** | **FastAPI (Python 3.11+)** | Django REST Framework (Python) | Spring Boot (Java) | **FastAPI** delivers high-throughput ASGI concurrency, automatic OpenAPI 3.1 documentation, strict `Pydantic v2` schema validation, and zero-overhead in-process integration with Python ML/NLP libraries (`spaCy`, `Scikit-learn`, `Transformers`). |
| **2. Primary Data Persistence** | **PostgreSQL 16** | MongoDB (Document NoSQL) | MySQL 8 | Public service regulations require strict relational integrity (ACID) across service categories, document checklists, and prerequisite graphs. **PostgreSQL** supports relational schemas, `JSONB` metadata, full-text search, and `pgvector` embeddings in one unified engine. |
| **3. NLP & Semantic Search Engine** | **Hybrid Python Pipeline (`spaCy` + `Scikit-learn` + `Transformers`)** | Standalone Elasticsearch (BM25) | External Commercial LLM API (OpenAI) | Running a self-contained **Hybrid Python NLP Pipeline** guarantees data sovereignty (citizen queries never leave national infrastructure), eliminates per-token API costs, prevents generative hallucinations, and keeps p95 latency below 500 ms. |
| **4. Frontend & Cloud DevOps** | **React / Next.js + Docker + AWS EC2** | Vue.js + Manual VPS Setup | Angular + Shared Hosting | **React / Next.js** provides server-side rendering (SSR) for SEO and fast initial load. **Docker Compose** and **AWS EC2** guarantee reproducible container builds and horizontal scalability. |
