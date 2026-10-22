# 10. Project Management, YouTrack Traceability, and Risk Matrix

## 10.1. Project Governance and Links
- **Active YouTrack Agile Board:** [https://govnav-kz.youtrack.cloud/projects/DIP](https://govnav-kz.youtrack.cloud/projects/DIP)
- **Backlog CSV Export:** [`docs/youtrack_tasks.csv`](youtrack_tasks.csv)
- **Developer:** Aldiyar Amangaliyev (`SE-2403`) — 100% individual execution across all project workpackages.
- **Supervisor:** Shynar Akhmetzhanova — weekly sprint review and milestone sign-off.

## 10.2. Traceability Matrix (YouTrack Tasks to Git Branches & Deliverables)
| YouTrack ID | Task Summary | State | Git Branch | Primary Deliverable |
| :--- | :--- | :--- | :--- | :--- |
| **DIP-1** | Initialize repository structure and configuration | Done | `DIP-1-repo-init` | `.gitignore`, `Dockerfile`, `docker-compose.yml`, `config/.env.example` |
| **DIP-2** | Write Project Proposal and define Project Scope | Done | `DIP-2-project-proposal` | `docs/01-project-proposal.md` |
| **DIP-5** | Document Evidence of Relevance and user interviews | Done | `DIP-3-relevance-evidence` | `docs/02-evidence-of-relevance.md` |
| **DIP-6** | Conduct Literature Review of 12 sources | Done | `DIP-4-literature-review` | `docs/03-literature-review.md` |
| **DIP-7** | Complete Existing System and Technology Comparisons | Done | `DIP-5-system-tech-comparison` | `docs/04-existing-system-comparison.md`, `docs/05-technology-comparison.md` |
| **DIP-8** | Specify Functional and Non-Functional Requirements | Done | `DIP-6-requirements-spec` | `docs/06-requirements-specification.md` |
| **DIP-9** | Design System Architecture and UML/C4 Diagrams | Done | `DIP-7-architecture-diagrams` | `docs/07-architecture.md`, `diagrams/*.mmd` |
| **DIP-10** | Develop UX Mockups, FastAPI NLP Prototype, and Pytest Suite | Done | `DIP-8-prototype-and-mvp` | `docs/08-ux-and-api-prototype.md`, `src/**`, `tests/**` |
| **DIP-11** | Create Verification Plan, Risk Matrix, and Supervisor Log | Done | `DIP-9-verification-and-review` | `docs/09`, `docs/10`, `docs/11`, `README.md`, Tag `pre-defense-1` |

## 10.3. Risk Register and Mitigation Strategy
| Risk ID | Risk Description | Probability | Impact | Mitigation Action |
| :--- | :--- | :--- | :--- | :--- |
| **RSK-01** | High morphological variance and code-switching (RU/KZ) in citizen queries lowering recall | Medium | High | Combine subword embeddings with domain stem matching and curated trilingual synonym lists. |
| **RSK-02** | High memory footprint of deep Transformer models during concurrent requests on AWS EC2 | Medium | Medium | Pre-compute service passport embeddings in PostgreSQL; execute lightweight vector similarity at runtime. |
| **RSK-03** | Changes in external eGov.kz statutory URLs or MCI fee rates | Low | Medium | Decouple catalog data into structured PostgreSQL tables with admin update scripts and schema validation. |
| **RSK-04** | Scope creep in single-developer full-stack + AI diploma timeline | Medium | High | Enforce strict MoSCoW prioritization in YouTrack (`DIP` board) and automated CI regression tests via `pytest`. |
