# 4. Existing System Comparison

We evaluate 5 existing government and commercial platforms against 8 functional, linguistic, and technical criteria.

## 4.1. Multi-Criteria System Comparison Matrix
| Evaluation Criterion | 1. eGov.kz Standard Search | 2. eGov Mobile / Kenesshi Bot | 3. Banking SuperApps (Kaspi / Halyk Gov) | 4. Gov.uk Navigation Portal | 5. General-Purpose LLMs (ChatGPT / Claude) | **Proposed System (GovNav KZ)** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Conversational Query Understanding (NLP)** | Low (requires exact statutory keywords) | Medium (button trees & basic intent rules) | Low (short title substring filter) | Medium (curated aliases, limited deep NLP) | High (strong semantic comprehension) | **High (Hybrid Python NLP: spaCy + Scikit-learn + Transformers)** |
| **2. Zero Legal Hallucinations** | Yes (official portal) | Yes (official app) | Yes (bank-integrated services) | Yes (for UK law only) | **No** (fabricates fees, deadlines, and rules) | **Yes (100% verified passports retrieved from PostgreSQL)** |
| **3. Coverage of RK Public Services** | Full statutory catalog | Partial (mobile-adapted subset) | Narrow (top 30 retail services) | None for RK | Unstructured & unverified | **Comprehensive structured catalog of RK services** |
| **4. Life-Situation Bundling & Next Steps** | Static text rubrics | Minimal | None (flat list) | High (step-by-step life guides) | Ad-hoc text only | **Automated sequential `recommended_next_steps` graph** |
| **5. Multi-Faceted Catalog Filtering** | Complex agency hierarchy | Minimal | None | Department & topic filters | None (chat only) | **Instant filtering by Category, Applicant Type, Online status** |
| **6. Trilingual Support (KZ / RU / EN)** | Full (but search fails on mixed queries) | KZ / RU | KZ / RU | EN only | Weak on Kazakh legal terms | **Unified cross-lingual semantic search (KZ / RU / EN)** |
| **7. Standardized Actionable Checklists** | Low (long legal text walls) | Medium | High | High | Unstructured prose | **Structured JSON/UI passport: Docs, Time, Fee, Online flag, URL** |
| **8. Response Latency & Ergonomics** | High cognitive load (3-5 clicks) | Mobile-locked | Locked inside banking ecosystem | Fast & accessible | Slow streaming (3-8 seconds) | **Sub-500 ms REST API & clean Next.js web interface** |

## 4.2. Competitive Advantage of the Proposed System
Our platform combines the **natural language comprehension** of modern AI with the **strict legal determinism** of official government registries, providing sub-second structured answers and life-situation routing without requiring users to know bureaucratic terminology.
