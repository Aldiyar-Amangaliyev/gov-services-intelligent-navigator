# Development of an Intelligent Navigation System for Public Services of the Republic of Kazakhstan

- **English:** Development of an Intelligent Navigation System for Public Services of the Republic of Kazakhstan
- **Russian:** Разработка интеллектуальной системы навигации по государственным услугам Республики Казахстан
- **Kazakh:** Қазақстан Республикасының мемлекеттік қызметтері бойынша интеллектуалды навигация жүйесін әзірлеу

---

## 1. Executive Summary & Problem Statement
Citizens and entrepreneurs in the Republic of Kazakhstan frequently struggle to find the right public service regulation because statutory standards are written in complex legal terminology, while standard portal search engines rely on rigid keyword matching.

**GovNav KZ** is a full-stack intelligent navigation platform powered by a hybrid Natural Language Processing (NLP) pipeline (`spaCy`, `Scikit-learn`, `Hugging Face Transformers`) and a deterministic `PostgreSQL` knowledge base. It understands conversational queries in **Kazakh, Russian, and English**, maps them to verified public service passports without generative hallucinations, and recommends sequential follow-up services for real-world life situations.

---

## 2. Project Team and Academic Supervision
| Role | Full Name | Affiliation | Responsibility Scope |
| :--- | :--- | :--- | :--- |
| **Developer** | **Aldiyar Amangaliyev** | Group SE-2403, Software Engineering, Astana IT University | **100% Individual Project:** System architecture, PostgreSQL design, FastAPI backend, Python NLP engine, Next.js UI, automated testing, Docker & CI/CD |
| **Supervisor** | **Shynar Akhmetzhanova** | Department of Software Engineering, Astana IT University | Academic supervision, methodology validation, and milestone evaluation |

---

## 3. YouTrack Project Management & Pre-Defense 1 Documentation Index
- **Active YouTrack Agile Board:** [https://govnav-kz.youtrack.cloud/projects/DIP](https://govnav-kz.youtrack.cloud/projects/DIP)
- **YouTrack Backlog CSV Export:** [`docs/youtrack_tasks.csv`](docs/youtrack_tasks.csv)
- **Release Milestone Tag:** `pre-defense-1` (24 October Deliverable)

| # | Mandatory Pre-Defense 1 Deliverable | Repository Document Link | Status |
| :--- | :--- | :--- | :--- |
| **01** | **Project Proposal, Aim, Objectives & Scope** | [`docs/01-project-proposal.md`](docs/01-project-proposal.md) | Completed |
| **02** | **Evidence of Relevance & 5 User Interviews** | [`docs/02-evidence-of-relevance.md`](docs/02-evidence-of-relevance.md) | Completed |
| **03** | **Critical Literature Review (12 Scientific Sources)** | [`docs/03-literature-review.md`](docs/03-literature-review.md) | Completed |
| **04** | **Existing System Comparison Matrix (5 Systems x 8 Criteria)** | [`docs/04-existing-system-comparison.md`](docs/04-existing-system-comparison.md) | Completed |
| **05** | **Technology Stack Comparison & Justification** | [`docs/05-technology-comparison.md`](docs/05-technology-comparison.md) | Completed |
| **06** | **Functional & Non-Functional Requirements Specification** | [`docs/06-requirements-specification.md`](docs/06-requirements-specification.md) | Completed |
| **07** | **System Architecture & Editable C4/UML Diagrams** | [`docs/07-architecture.md`](docs/07-architecture.md) & [`diagrams/`](diagrams/) | Completed |
| **08** | **UX Wireframes & REST API Prototype Specification** | [`docs/08-ux-and-api-prototype.md`](docs/08-ux-and-api-prototype.md) | Completed |
| **09** | **Verification Plan & Baseline vs. Hybrid Evaluation** | [`docs/09-verification-and-evaluation-plan.md`](docs/09-verification-and-evaluation-plan.md) | Completed |
| **10** | **Project Management, YouTrack Traceability & Risk Matrix** | [`docs/10-project-management-and-risks.md`](docs/10-project-management-and-risks.md) | Completed |
| **11** | **Supervisor Feedback & Iterative Improvement Log** | [`docs/11-supervisor-feedback.md`](docs/11-supervisor-feedback.md) | Completed |

---

## 4. Technology Stack
- **Backend API:** Python 3.11+, FastAPI, Pydantic v2, Uvicorn, SQLAlchemy
- **NLP & Semantic Ranking Engine:** Python, spaCy, Hugging Face Transformers, Scikit-learn
- **Database Layer:** PostgreSQL 16 (Relational Service Passports + Vector Embeddings)
- **Frontend Client:** React 18, Next.js 14, TypeScript, Tailwind CSS
- **Quality Assurance & DevOps:** Pytest, HTTPX, Docker, Docker Compose, AWS EC2

---

## 5. Repository Structure
```text
gov-services-intelligent-navigator/
├── config/
│   └── .env.example                           # Environment variable template (no secrets)
├── diagrams/
│   ├── system-context.mmd                     # Editable C4 System Context diagram
│   ├── use-case.mmd                           # Editable UML Use Case diagram
│   ├── component-diagram.mmd                  # Editable Component Architecture diagram
│   └── search-sequence.mmd                    # Editable Semantic Search Sequence diagram
├── docs/
│   ├── 01-project-proposal.md                 # Problem, Users, Aim, Objectives, Scope
│   ├── 02-evidence-of-relevance.md            # 5 User Interviews & Verified Findings
│   ├── 03-literature-review.md                # 12 Academic & Technical Sources Review
│   ├── 04-existing-system-comparison.md       # 5 Existing Systems Compared Across 8 Criteria
│   ├── 05-technology-comparison.md            # 4 Core Stack Decisions Compared & Justified
│   ├── 06-requirements-specification.md       # Prioritized FR & NFR with Acceptance Criteria
│   ├── 07-architecture.md                     # Architecture Documentation & Rendered Diagrams
│   ├── 08-ux-and-api-prototype.md             # UI Wireframes & OpenAPI Payload Contracts
│   ├── 09-verification-and-evaluation-plan.md # Baseline Comparison, Metrics & Testing Plan
│   ├── 10-project-management-and-risks.md     # YouTrack Board, Milestones & Risk Matrix
│   ├── 11-supervisor-feedback.md              # Supervisor Review Log & Action Taken
│   └── youtrack_tasks.csv                     # Exported YouTrack Tasks (DIP-1 to DIP-11)
├── src/
│   ├── backend/
│   │   ├── main.py                            # FastAPI Application & REST Endpoints
│   │   └── models.py                          # Pydantic v2 Request/Response Schemas
│   ├── nlp_engine/
│   │   └── navigator.py                       # Trilingual Hybrid NLP Engine & Benchmark Evaluator
│   └── frontend/
│       ├── package.json                       # React / Next.js Client Dependencies
│       └── README.md                          # Frontend Module Overview
├── tests/
│   └── test_navigator.py                      # Automated Pytest Suite (6 Verification Tests)
├── Dockerfile                                 # Backend Container Definition
├── docker-compose.yml                         # FastAPI + PostgreSQL 16 Orchestration
├── requirements.txt                           # Python Package Dependencies
└── README.md                                  # Main Project Documentation
```

---

## 6. Local Setup, Execution, and Verification
1. Clone the repository and configure environment variables:
   ```bash
   git clone <repository-url>
   cd gov-services-intelligent-navigator
   cp config/.env.example .env
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the FastAPI server:
   ```bash
   uvicorn src.backend.main:app --reload --port 8000
   ```
   Open `http://localhost:8000/docs` to test `/api/v1/navigate/search` and `/api/v1/evaluate/benchmark` interactively.
4. Run the automated verification test suite:
   ```bash
   pytest tests/ -v
   ```
