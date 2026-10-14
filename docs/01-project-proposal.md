# 1. Project Proposal

## 1.1. Project Title
- **English:** Development of an Intelligent Navigation System for Public Services of the Republic of Kazakhstan
- **Russian:** Разработка интеллектуальной системы навигации по государственным услугам Республики Казахстан
- **Kazakh:** Қазақстан Республикасының мемлекеттік қызметтері бойынша интеллектуалды навигация жүйесін әзірлеу

## 1.2. Project Team and Academic Supervision
| Role | Full Name | Academic Group / Department | Contribution Share |
| :--- | :--- | :--- | :--- |
| **Student / Lead Developer** | **Aldiyar Amangaliyev** | Group SE-2403, Department of Software Engineering, Astana IT University | **100% (Individual Project):** Requirements engineering, PostgreSQL schema design, FastAPI backend, Python NLP pipeline, Next.js UI, testing, Docker & AWS deployment |
| **Academic Supervisor** | **Shynar Akhmetzhanova** | Department of Software Engineering, Astana IT University | Methodology guidance, architectural validation, and milestone evaluation |

## 1.3. Problem Statement
Digital government infrastructure in the Republic of Kazakhstan provides over 600 public services to millions of citizens and businesses. Despite wide digitization, service discovery remains a critical bottleneck:
1. **Bureaucratic Vocabulary Mismatch:** Official service titles and statutory regulations are drafted in rigid legal terminology, whereas citizens formulate requests in everyday conversational language.
2. **Limitations of Keyword Search:** Existing catalog search engines rely on exact lexical substring matching, returning empty or irrelevant results when users use synonyms, colloquial expressions, or mixed-language queries.
3. **Fragmented Life-Situation Routing:** Real-world citizen events (e.g., birth of a child, opening a small business, purchasing property, losing identification documents) require executing 2 to 5 interconnected services across different agencies, but portals list them as isolated items.

## 1.4. Target Users
1. **Citizens of the Republic of Kazakhstan (Individuals):** Everyday users needing immediate, step-by-step checklists, required documents, state fees, and statutory processing timelines based on conversational descriptions of their problem.
2. **Individual Entrepreneurs and SMEs (Business Users):** Business owners searching for licensing, tax registration, sanitary permits, and activity notifications.
3. **Front-Office Consultants and Call-Center Operators:** Public service center personnel requiring a low-latency semantic lookup tool to consult citizens accurately.

## 1.5. Project Aim and Objectives
**Aim:** To design, implement, and evaluate a fault-tolerant, scalable web platform for intelligent semantic navigation across public services of the Republic of Kazakhstan, powered by a hybrid Natural Language Processing (NLP) pipeline and deterministic relational knowledge retrieval.

**Core Objectives:**
1. Conduct domain analysis of Kazakhstan public service standards, user search behavior, and multi-step life situations.
2. Design a modular client-server architecture (`FastAPI` REST backend + `PostgreSQL` relational database) capable of storing structured service passports, document checklists, and vector embeddings.
3. Implement a trilingual (KZ / RU / EN) hybrid NLP engine in Python combining `spaCy` morphological normalization, `Scikit-learn` intent classification, and `Hugging Face Transformers` semantic similarity ranking.
4. Develop a responsive web interface (`React / Next.js`) with multi-parameter filtering, life-situation bundles, and actionable checklists.
5. Execute automated unit, integration, and benchmark testing (`pytest`), containerize the application via `Docker`, and configure cloud deployment for `AWS EC2`.

## 1.6. Expected Outcomes and Success Metrics
- **Retrieval Recall (Recall@3):** >= 88% on the 200-query trilingual conversational validation benchmark.
- **Intent Classification Accuracy (Macro F1):** >= 0.85 across primary public service categories.
- **API Response Latency (p95):** <= 500 ms for semantic NLP search and <= 200 ms for structured catalog filtering.
- **Zero Legal Hallucinations:** 100% of displayed service parameters originate from verified PostgreSQL records.

## 1.7. Project Scope
| Scope Dimension | Included in Scope (In-Scope) | Excluded from Scope (Out-of-Scope) |
| :--- | :--- | :--- |
| **Functional Capabilities** | Conversational semantic search (KZ/RU/EN), intent detection, multi-faceted filtering, life-situation bundles, document checklists, official gateway routing | Direct cryptographic signing via EDS / NCALayer inside the platform (users are routed to the official eGov.kz / elicense.kz execution gateway) |
| **Data Layer** | Publicly available statutory service standards, fees (MCI), timelines, and prerequisite graphs stored in PostgreSQL | Storage or processing of classified citizen personal data (IIN databases, medical records, tax secrets) |
| **Engineering & DevOps** | FastAPI backend, Python NLP module, React/Next.js frontend, pytest suite, Docker Compose orchestration | Native iOS/Android mobile app development (web platform is mobile-responsive via browser) |
