# 8. UX Wireframes and REST API Prototype

## 8.1. User Interface Wireframes

### Screen 1: Conversational Discovery Hub & Life Situations
```text
+---------------------------------------------------------------------------------------+
| [GovNav KZ]          Catalog       Life Situations       API Benchmark   [KZ | RU | EN]|
+---------------------------------------------------------------------------------------+
|                                                                                       |
|          INTELLIGENT NAVIGATION SYSTEM FOR PUBLIC SERVICES OF KAZAKHSTAN              |
|       Describe your life situation in everyday words — get an exact checklist         |
|                                                                                       |
|  +---------------------------------------------------------------------------------+  |
|  | Query: "потерял удостоверение личности как быстро восстановить"   [Find Service]|  |
|  +---------------------------------------------------------------------------------+  |
|  Quick Examples: [Lost ID Card]  [Childbirth Allowance]  [Open Coffee Shop / IP]      |
|                                                                                       |
|  POPULAR LIFE-SITUATION BUNDLES:                                                      |
|  +-------------------------+ +-------------------------+ +-------------------------+  |
|  | [LS-01] Birth of Child  | | [LS-02] Start Business  | | [LS-03] Buy Apartment   |  |
|  | 3 sequential services   | | IP, KKM & permits       | | Title registration      |  |
|  +-------------------------+ +-------------------------+ +-------------------------+  |
+---------------------------------------------------------------------------------------+
```

### Screen 2: Semantic Search Results & Actionable Service Passport
```text
+---------------------------------------------------------------------------------------+
| Detected Category: Documents and Citizenship  | Keywords: потерял, удостоверение      |
+---------------------------------------------------------------------------------------+
| FILTERS:              | #1 [SRV-KZ-001] Issuance of Passports and National ID Cards   |
| [x] Individual        |    Semantic Match Score: 0.96  |  Online & CSC  |  15 days    |
| [ ] Business / IP     |    Fee: 0.2 MCI (ID Card) / 8 MCI (Passport)                  |
| [x] Online Available  |    REQUIRED DOCUMENTS CHECKLIST:                              |
|                       |      [v] Completed electronic or CSC application form         |
|                       |      [v] State duty payment receipt                           |
|                       |      [v] Old ID card or written loss notification             |
|                       |    [Proceed to Official Service on eGov.kz ->]                |
|                       |                                                               |
|                       |    RECOMMENDED NEXT STEPS IN THIS SITUATION:                  |
|                       |      1. Re-issue Electronic Digital Signature (EDS)           |
|                       |      2. Update identification record in banking apps          |
+---------------------------------------------------------------------------------------+
```

## 8.2. REST API Endpoints Implemented in MVP (`src/backend/main.py`)
| HTTP Method | Endpoint Path | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Returns service health, version tag (`pre-defense-1`), and catalog size. |
| `GET` | `/api/v1/services` | Filters public service passports by `category`, `applicant_type`, and `online_only`. |
| `GET` | `/api/v1/life-situations` | Returns bundled multi-step life-situation scenarios (`LS-01` to `LS-03`). |
| `POST` | `/api/v1/navigate/search` | Executes hybrid NLP semantic search, intent detection, and next-step recommendation. |
| `GET` | `/api/v1/evaluate/benchmark` | Runs live evaluation comparing Hybrid NLP against the Exact-Match Baseline. |
