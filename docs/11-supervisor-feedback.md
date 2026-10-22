# 11. Supervisor Feedback and Iterative Improvement Log

- **Academic Supervisor:** Shynar Akhmetzhanova
- **Student:** Aldiyar Amangaliyev (Group SE-2403, Astana IT University)

## 11.1. Record of Consultation Sessions
| Date | Reviewed Artifact | Supervisor Feedback & Recommendations | Engineering Action Implemented | Status |
| :--- | :--- | :--- | :--- | :--- |
| **12 Oct 2026** | Topic Justification & `01-project-proposal.md` | Define clear In-Scope vs. Out-of-Scope boundaries so the navigator focuses on intelligent NLP discovery rather than duplicating eGov cryptographic signing. | Added explicit Scope table in `docs/01-project-proposal.md` positioning the platform as an intelligent discovery and routing layer. | **Completed** |
| **16 Oct 2026** | `03-literature-review.md` & `04-existing-system-comparison.md` | Highlight why standard generative chatbots are risky for government consulting (hallucinated laws/fees) and justify the deterministic database retrieval approach. | Expanded Literature Review (12 papers) and System Comparison (8 criteria) to emphasize zero-hallucination retrieval from verified PostgreSQL passports. | **Completed** |
| **20 Oct 2026** | `06-requirements-specification.md`, `07-architecture.md` & MVP Code | Include a quantifiable baseline comparison in the prototype and ensure all requirements have testable acceptance criteria verified by `pytest`. | Added `/api/v1/evaluate/benchmark` endpoint comparing Hybrid NLP vs. Lexical Baseline, created 4 Mermaid diagrams, and wrote 6 automated `pytest` tests. | **Completed** |
