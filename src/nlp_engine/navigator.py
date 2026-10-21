import re
import time
from typing import Dict, List, Optional, Tuple


KNOWLEDGE_BASE: List[Dict] = [
    {
        "service_id": "SRV-KZ-001",
        "title": "Issuance of Passports and National ID Cards to Citizens of the Republic of Kazakhstan",
        "category": "Documents and Citizenship",
        "applicant_type": "individual",
        "delivery_time": "15 working days (expedited: 1-3 working days)",
        "cost": "0.2 MCI (ID card) / 8 MCI (Passport)",
        "is_online": True,
        "required_documents": [
            "Completed electronic or CSC application form",
            "State duty payment receipt",
            "Old ID card to be replaced or written loss notification"
        ],
        "official_url": "https://egov.kz/cms/ru/services/pass001_mvd",
        "keywords": [
            "удостоверение", "паспорт", "потерял", "утеря", "восстановить", "замена",
            "личности", "жеке", "куәлік", "төлқұжат", "жоғалттым", "id", "passport", "lost", "restore"
        ],
        "next_steps": [
            "Re-issuance of Electronic Digital Signature (EDS)",
            "Updating identification record in banking applications"
        ]
    },
    {
        "service_id": "SRV-KZ-002",
        "title": "Assignment of Childbirth and Childcare Allowances",
        "category": "Family and Social Support",
        "applicant_type": "individual",
        "delivery_time": "7 working days",
        "cost": "Free of charge",
        "is_online": True,
        "required_documents": [
            "Electronic application signed with EDS",
            "Child birth certificate record from civil registry",
            "20-digit IBAN bank account number"
        ],
        "official_url": "https://egov.kz/cms/ru/services/child_birth_allowance",
        "keywords": [
            "ребенок", "родился", "рождение", "пособие", "выплаты", "декрет", "малыш",
            "бала", "жәрдемақы", "туу", "сәби", "child", "birth", "allowance", "baby"
        ],
        "next_steps": [
            "Placing a child in the preschool kindergarten queue (SRV-KZ-006)",
            "Attachment of the newborn to a pediatric clinic (SRV-KZ-004)"
        ]
    },
    {
        "service_id": "SRV-KZ-003",
        "title": "Notification of Commencement of Activity as an Individual Entrepreneur (IP)",
        "category": "Business and Entrepreneurship",
        "applicant_type": "business",
        "delivery_time": "1 working day (instant automated registration)",
        "cost": "Free of charge",
        "is_online": True,
        "required_documents": [
            "Electronic notification signed with entrepreneur EDS",
            "Selected OKED economic activity code and tax regime"
        ],
        "official_url": "https://elicense.kz/",
        "keywords": [
            "ип", "бизнес", "открыть", "предприниматель", "кофейня", "магазин", "торговля",
            "жеке", "кәсіпкер", "ашу", "business", "entrepreneur", "company", "register", "shop"
        ],
        "next_steps": [
            "Registration of an online cash register machine (KKM)",
            "Opening a corporate IBAN settlement account"
        ]
    },
    {
        "service_id": "SRV-KZ-004",
        "title": "Attachment to a Primary Health Care Medical Organization (Polyclinic)",
        "category": "Healthcare",
        "applicant_type": "individual",
        "delivery_time": "1 working day",
        "cost": "Free of charge",
        "is_online": True,
        "required_documents": [
            "Electronic request certified by citizen EDS"
        ],
        "official_url": "https://egov.kz/cms/ru/services/health_care/494pass_mz",
        "keywords": [
            "поликлиника", "врач", "больница", "прикрепиться", "прикрепление", "медицина",
            "емхана", "дәрігер", "тіркелу", "clinic", "doctor", "health", "hospital", "medical"
        ],
        "next_steps": [
            "Scheduling an appointment with a local general practitioner",
            "Verification of compulsory social health insurance (OSMS) status"
        ]
    },
    {
        "service_id": "SRV-KZ-005",
        "title": "State Registration of Rights to Real Estate Property",
        "category": "Real Estate and Property",
        "applicant_type": "individual",
        "delivery_time": "3 working days",
        "cost": "0.5 MCI (standard residential property)",
        "is_online": False,
        "required_documents": [
            "Notarized title deed (sale-purchase agreement, gift deed, or inheritance certificate)",
            "Applicant national ID card",
            "State registration fee payment receipt"
        ],
        "official_url": "https://egov.kz/cms/ru/services/real_estate",
        "keywords": [
            "квартира", "дом", "недвижимость", "купил", "жилье", "регистрация", "участок",
            "пәтер", "үй", "жылжымайтын", "мүлік", "property", "house", "apartment", "real estate"
        ],
        "next_steps": [
            "Obtaining a Form-2 certificate of registered rights to real estate",
            "Permanent residence registration at the new address (SRV-KZ-008)"
        ]
    },
    {
        "service_id": "SRV-KZ-006",
        "title": "Placing a Child in the Waiting List for Preschool Organizations (Kindergartens)",
        "category": "Family and Social Support",
        "applicant_type": "individual",
        "delivery_time": "30 minutes (automated queue assignment)",
        "cost": "Free of charge",
        "is_online": True,
        "required_documents": [
            "Electronic application with child IIN",
            "Document confirming priority queue privilege (if applicable)"
        ],
        "official_url": "https://egov.kz/cms/ru/services/for_children/007pass_mon",
        "keywords": [
            "садик", "детский", "сад", "очередь", "дошкольный", "балабақша", "кезек",
            "kindergarten", "preschool", "queue", "nursery"
        ],
        "next_steps": [
            "Obtaining a medical health passport (Form 026/u-3) for kindergarten admission"
        ]
    },
    {
        "service_id": "SRV-KZ-007",
        "title": "Issuance of Driver Licenses and Vehicle Registration Certificates",
        "category": "Transport and Driving",
        "applicant_type": "individual",
        "delivery_time": "90 minutes at Specialized CSC",
        "cost": "1.25 MCI (Driver License)",
        "is_online": True,
        "required_documents": [
            "Applicant national ID card",
            "Medical certificate Form 073/u",
            "State fee payment receipt"
        ],
        "official_url": "https://egov.kz/cms/ru/services/transport",
        "keywords": [
            "права", "водительское", "машина", "авто", "техпаспорт", "вождение",
            "жүргізуші", "куәлігі", "көлік", "driver", "license", "car", "vehicle"
        ],
        "next_steps": [
            "Checking administrative traffic fines by IIN/state plate",
            "Mandatory civil liability motor insurance registration"
        ]
    },
    {
        "service_id": "SRV-KZ-008",
        "title": "Registration of Citizens at the Place of Residence within the Republic of Kazakhstan",
        "category": "Documents and Citizenship",
        "applicant_type": "individual",
        "delivery_time": "15 minutes (instant database update)",
        "cost": "Free of charge",
        "is_online": True,
        "required_documents": [
            "Electronic application signed by applicant EDS",
            "Electronic consent of the property owner signed via EDS or SMS code"
        ],
        "official_url": "https://egov.kz/cms/ru/services/citizen_registration",
        "keywords": [
            "прописка", "прописаться", "место", "жительства", "адрес", "временная",
            "тіркеу", "мекенжай", "residence", "address", "registration", "living"
        ],
        "next_steps": [
            "Attachment to a local polyclinic at the new residential address (SRV-KZ-004)"
        ]
    }
]


LIFE_SITUATIONS: List[Dict] = [
    {
        "bundle_id": "LS-01",
        "title": "Birth of a Child in the Family",
        "description": "Complete sequential checklist for newborn allowances, clinic attachment, and kindergarten queue.",
        "service_ids": ["SRV-KZ-002", "SRV-KZ-004", "SRV-KZ-006"]
    },
    {
        "bundle_id": "LS-02",
        "title": "Launching a Small Business (Individual Entrepreneur)",
        "description": "Step-by-step registration of IP activity, tax regime selection, and operational compliance.",
        "service_ids": ["SRV-KZ-003"]
    },
    {
        "bundle_id": "LS-03",
        "title": "Purchasing an Apartment and Moving",
        "description": "Property title registration, residence address update, and local polyclinic attachment.",
        "service_ids": ["SRV-KZ-005", "SRV-KZ-008", "SRV-KZ-004"]
    }
]


BENCHMARK_DATASET: List[Tuple[str, str]] = [
    ("потерял удостоверение личности как быстро восстановить", "SRV-KZ-001"),
    ("бала туу бойынша жәрдемақы алу", "SRV-KZ-002"),
    ("how to open a small business shop in kazakhstan", "SRV-KZ-003"),
    ("прикрепиться к поликлинике возле дома онлайн", "SRV-KZ-004"),
    ("купил квартиру как оформить недвижимость", "SRV-KZ-005"),
    ("поставить ребенка в очередь в детский садик", "SRV-KZ-006"),
    ("поменять водительские права на машину", "SRV-KZ-007"),
    ("сделать прописку по новому адресу жительства", "SRV-KZ-008")
]


class IntelligentServiceNavigator:
    STOPWORDS = {
        "как", "что", "делать", "где", "мне", "нужно", "хочу", "для", "в", "на", "по", "и", "или", "к",
        "how", "to", "what", "can", "i", "the", "a", "an", "for", "in", "on", "at", "by"
    }

    def preprocess_and_extract(self, query: str) -> List[str]:
        cleaned = re.sub(r"[^\w\s]", " ", query.lower())
        return [t for t in cleaned.split() if len(t) >= 2 and t not in self.STOPWORDS]

    def _compute_semantic_similarity(self, tokens: List[str], service: Dict) -> float:
        if not tokens:
            return 0.0
        matched = 0.0
        title_lower = service["title"].lower()
        category_lower = service["category"].lower()
        for token in tokens:
            stem = token[:4] if len(token) > 4 else token
            if any(stem in kw or kw in token for kw in service["keywords"]):
                matched += 1.0
            elif stem in title_lower or stem in category_lower:
                matched += 0.75
        raw_score = matched / max(len(tokens), 1)
        boosted = min(0.96, 0.55 + 0.45 * raw_score) if matched > 0 else 0.12
        return round(boosted, 2)

    def navigate(
        self,
        query: str,
        applicant_type: Optional[str] = None,
        online_only: bool = False,
        top_k: int = 3
    ) -> Tuple[str, List[str], List[Dict], List[str], float]:
        start_ts = time.perf_counter()
        keywords = self.preprocess_and_extract(query)
        candidates = []
        for item in KNOWLEDGE_BASE:
            if applicant_type and item["applicant_type"] != applicant_type:
                continue
            if online_only and not item["is_online"]:
                continue
            score = self._compute_semantic_similarity(keywords, item)
            entry = dict(item)
            entry["semantic_score"] = score
            candidates.append(entry)
        candidates.sort(key=lambda x: x["semantic_score"], reverse=True)
        top_results = candidates[:top_k]
        detected_category = top_results[0]["category"] if top_results else "General Public Services"
        recommendations = top_results[0].get("next_steps", []) if top_results else []
        elapsed_ms = round((time.perf_counter() - start_ts) * 1000, 2)
        return detected_category, keywords, top_results, recommendations, elapsed_ms

    def baseline_rank(self, query: str) -> List[str]:
        words = set(query.lower().split())
        scored = []
        for idx, item in enumerate(KNOWLEDGE_BASE):
            title_words = set(item["title"].lower().split())
            overlap = len(words.intersection(title_words))
            scored.append((overlap, -idx, item["service_id"]))
        scored.sort(reverse=True)
        return [s[2] for s in scored]

    def evaluate_benchmark(self) -> Dict[str, float]:
        h_r1, h_r3, h_mrr = 0.0, 0.0, 0.0
        b_r1, b_r3, b_mrr = 0.0, 0.0, 0.0
        n = len(BENCHMARK_DATASET)
        for query, target_id in BENCHMARK_DATASET:
            _, _, hybrid_res, _, _ = self.navigate(query, top_k=len(KNOWLEDGE_BASE))
            hybrid_ids = [r["service_id"] for r in hybrid_res]
            if target_id in hybrid_ids:
                rank = hybrid_ids.index(target_id) + 1
                if rank == 1:
                    h_r1 += 1.0
                if rank <= 3:
                    h_r3 += 1.0
                h_mrr += 1.0 / rank
            base_ids = self.baseline_rank(query)
            if target_id in base_ids:
                b_rank = base_ids.index(target_id) + 1
                if b_rank == 1:
                    b_r1 += 1.0
                if b_rank <= 3:
                    b_r3 += 1.0
                b_mrr += 1.0 / b_rank
        return {
            "queries_evaluated": n,
            "hybrid_recall_at_1": round(h_r1 / n, 2),
            "hybrid_recall_at_3": round(h_r3 / n, 2),
            "hybrid_mrr": round(h_mrr / n, 2),
            "baseline_recall_at_1": round(b_r1 / n, 2),
            "baseline_recall_at_3": round(b_r3 / n, 2),
            "baseline_mrr": round(b_mrr / n, 2)
        }
