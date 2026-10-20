# 7. System Architecture and Diagrams

The platform implements a decoupled 4-tier architecture: **Presentation Tier (`React / Next.js`)**, **API Gateway Tier (`FastAPI`)**, **Intelligent Navigation Tier (`Python Hybrid NLP Engine`)**, and **Persistence Tier (`PostgreSQL`)**.

All editable Mermaid diagram source files are stored in the [`../diagrams/`](../diagrams/) directory:
- [`diagrams/system-context.mmd`](../diagrams/system-context.mmd)
- [`diagrams/use-case.mmd`](../diagrams/use-case.mmd)
- [`diagrams/component-diagram.mmd`](../diagrams/component-diagram.mmd)
- [`diagrams/search-sequence.mmd`](../diagrams/search-sequence.mmd)

## 7.1. System Context Diagram (C4 Level 1)
```mermaid
flowchart TB
    Citizen["Citizen / Entrepreneur of RK\n(Primary User)"]
    Consultant["Front-Office Consultant\n(Support Operator)"]
    Admin["System Administrator\n(Catalog Maintainer)"]
    subgraph GovNav["Intelligent Navigation System for Public Services of RK"]
        Platform["GovNav KZ Web & NLP Platform\n(Next.js + FastAPI + Hybrid Python NLP + PostgreSQL)"]
    end
    EGov["External Official Gateways\n(eGov.kz / elicense.kz)"]
    Citizen -- "1. Conversational query (KZ/RU/EN) & filters" --> Platform
    Consultant -- "2. Rapid semantic lookup" --> Platform
    Platform -- "3. Ranked service passports, checklist & next steps" --> Citizen
    Admin -- "4. Statutory catalog updates" --> Platform
    Platform -- "5. Direct routing to official execution URL" --> EGov
```

## 7.2. Use Case Diagram
```mermaid
flowchart LR
    Citizen(["Citizen / Entrepreneur"])
    Admin(["System Administrator"])
    subgraph SystemBoundary["Intelligent Public Services Navigator"]
        UC1("Submit conversational query in KZ / RU / EN")
        UC2("View semantically ranked service passports")
        UC3("Filter catalog by category, applicant type, online status")
        UC4("Inspect required document checklist, fee, and timeline")
        UC5("Browse bundled Life-Situation scenarios")
        UC6("Follow recommended next-step services")
        UC7("Navigate to official eGov.kz / elicense.kz portal")
        UC8("Run Baseline vs Hybrid NLP evaluation benchmark")
        UC1 -. "include" .-> UC2
        UC2 -. "extend" .-> UC4
        UC4 -. "extend" .-> UC6
        UC4 -. "extend" .-> UC7
    end
    Citizen --> UC1
    Citizen --> UC3
    Citizen --> UC5
    Admin --> UC8
```

## 7.3. Component Architecture Diagram (C4 Level 3)
```mermaid
flowchart TB
    subgraph ClientLayer["Presentation Layer (React / Next.js)"]
        SearchUI["Conversational Search Bar & Quick Prompts"]
        FilterUI["Multi-Faceted Filter Panel"]
        PassportUI["Service Passport & Checklist View"]
    end
    subgraph APILayer["Application API Layer (FastAPI)"]
        Router["REST Controllers & Pydantic v2 Validators"]
        CatalogSvc["Catalog & Life-Situation Service"]
        EvalSvc["Benchmark Evaluation Controller"]
    end
    subgraph NLPLayer["Intelligent NLP Layer (Python)"]
        Normalizer["Text Normalizer & Stopword Filter (spaCy)"]
        IntentCls["Domain Intent Classifier (Scikit-learn)"]
        SemanticRanker["Hybrid Semantic & Stem Ranker (Transformers)"]
        NextStepEngine["Life-Situation Next-Step Graph"]
    end
    subgraph DataLayer["Data Persistence Layer (PostgreSQL 16)"]
        PG[("PostgreSQL Database:\nService Passports, Checklists,\nLife Situations, Embeddings")]
    end
    SearchUI --> Router
    FilterUI --> Router
    PassportUI --> Router
    Router --> CatalogSvc
    Router --> Normalizer
    Router --> EvalSvc
    Normalizer --> IntentCls
    Normalizer --> SemanticRanker
    SemanticRanker --> NextStepEngine
    CatalogSvc --> PG
    SemanticRanker --> PG
```

## 7.4. Semantic Search Sequence Diagram
```mermaid
sequenceDiagram
    actor User as Citizen (Browser)
    participant API as FastAPI Gateway
    participant NLP as Hybrid NLP Navigator
    participant DB as PostgreSQL Catalog
    User->>API: POST /api/v1/navigate/search (query, lang, filters)
    API->>API: Validate payload via Pydantic SearchRequest
    API->>NLP: navigate(query, applicant_type, online_only, top_k)
    NLP->>NLP: preprocess_and_extract(query) -> normalized tokens
    NLP->>DB: Fetch candidate service passports matching filters
    DB-->>NLP: Candidate records & keyword/embedding index
    NLP->>NLP: Compute hybrid semantic & stem similarity scores
    NLP->>NLP: Detect primary category & resolve recommended_next_steps
    NLP-->>API: Ranked passports, category, keywords, latency_ms
    API-->>User: 200 OK NavigationResponse JSON
```
