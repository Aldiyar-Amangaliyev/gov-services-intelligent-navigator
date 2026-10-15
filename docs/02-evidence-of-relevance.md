# 2. Evidence of Relevance and User Research

To validate the practical necessity of the system, process observations and 5 structured interviews were conducted with representative target users in Astana.

## 2.1. Structured Summary of User Interviews
| Interview ID | Respondent Profile | Real-World Scenario | Observed Search Query Used | Key Pain Points & Quantified Impact |
| :--- | :--- | :--- | :--- | :--- |
| **INT-1** | University Student (20 y.o., Astana) | Lost national ID card and needed urgent replacement before exams | *"потерял удостоверение личности как быстро восстановить"* | Standard portal search returned 18 archival legal decrees instead of the direct service passport; spent 25 minutes locating fee and document rules. |
| **INT-2** | Young Parent (29 y.o., Astana) | Birth of first child: registering birth, applying for allowances, and queuing for kindergarten | *"бала туу бойынша жәрдемақы және балабақша кезегі"* | User did not know that 4 separate services must be executed sequentially; missed the optimal sequence and had to re-submit forms. |
| **INT-3** | Individual Entrepreneur (35 y.o., SME Owner) | Opening a neighborhood coffee shop (IP notification, cash register, sanitary permit) | *"как открыть кофейню какие разрешения нужны ип"* | Official nomenclature uses *"Notification of commencement of activity as an individual entrepreneur"*; conversational query yielded zero matches. |
| **INT-4** | Senior Citizen (62 y.o., Retiree) | Registering property ownership rights after purchasing an apartment | *"купил квартиру как оформить на себя документы"* | Deep department-based menu hierarchy caused navigation fatigue; user abandoned online search after 3 failed clicks and visited a physical center. |
| **INT-5** | Front-Office Consultant (25 y.o., Public Service Center) | Consulting 40+ citizens daily on document checklists and state duties | *Internal lookup across statutory regulations* | Over 60% of physical visits happen solely because citizens cannot translate their everyday life problem into the exact statutory title. |

## 2.2. Verified Empirical Findings
1. **Lexical Gap Between Citizens and Statutes:** Citizens describe *events and problems* ("lost wallet", "baby born", "open cafe"), whereas government catalogs index *administrative actions* ("Issuance of identity documents", "Assignment of social payment").
2. **Four-Field Information Priority:** Across all 5 interviews, users stated they need four immediate data points before clicking apply: (a) exact list of required documents, (b) official processing time, (c) exact state fee in MCI, and (d) whether the service is available 100% online.
3. **Sequential Service Dependencies:** Completing one public service frequently triggers the need for 2-3 follow-up services within the same life event.

## 2.3. Engineering Assumptions to Validate
| Assumption ID | Hypothesis Statement | Validation Method | Target Metric |
| :--- | :--- | :--- | :--- |
| **ASM-01** | Combining subword semantic embeddings with domain stem matching will resolve colloquial vocabulary mismatch across KZ, RU, and EN. | Benchmark evaluation on 200 conversational citizen queries against SQL lexical baseline. | Recall@3 >= 0.88 and MRR >= 0.80 |
| **ASM-02** | Displaying automated `recommended_next_steps` alongside each service passport will cover multi-service life events without manual re-searching. | User acceptance testing across 5 multi-step life scenarios. | >= 40% reduction in search session time |
