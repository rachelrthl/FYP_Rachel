# Signal Intelligence Dashboard for AWS Sales

## A1. PROBLEM DEFINITION & VALUE PROPOSITION

### 1.1 The Problem & Persona

**Persona: Sarah Tan – Demand Generation Representative, AWS (Singapore)**

Sarah is a Demand Generation Representative (DGR) — a front-line outbound sales role responsible for identifying potential customers and booking qualified meetings for Account Executives (AEs). Her performance is measured by the number of "sales-qualified meetings" (SQMs) she creates each week, which directly feeds AWS's new business pipeline.

Sarah manages a portfolio of 1,200 Small and Medium Business (SMB) accounts, each representing potential cloud deals between US$10K–100K annually. Her target is to book 10 qualified meetings per week, converting research and outreach into tangible sales opportunities.

Within AWS's structure, DGRs operate under tight time constraints. Interviews with eight AWS sales representatives show that only 12 out of 40 weekly working hours are typically allocated to prospecting. The remaining time is consumed by internal meetings, pipeline reviews, CRM updates, reporting, and follow-ups — leaving limited bandwidth for deep account research.

**Psychographic Profile:**
Sarah is ambitious, data-driven, and goal-oriented. She enjoys helping companies scale through cloud adoption but is often frustrated by the inefficiency of manual prospecting. Every hour spent researching low-potential accounts feels like a lost opportunity, especially when performance metrics depend on how efficiently she identifies the right leads.

**The Core Problem:** Sarah's challenge is twofold:

1. **Time inefficiency**: Manual research across multiple systems takes roughly 10 minutes per account, limiting her to about 72 accounts per week—only 6–7% of her portfolio.

2. **Signal blindness**: Within that 7%, her prioritization is based largely on static internal metrics (e.g., account revenue, cloud spend, AWS event attendance) rather than dynamic external buying signals (e.g., job postings, funding rounds, or leadership changes).

This means that each week, roughly 45 high-intent accounts go undetected. Assuming an average AWS SMB deal size of US$37,000, these missed opportunities represent an estimated US$1.66M in unrealized annual pipeline per rep.

Sarah's problem is not one of motivation or skill — it is structural. Her tools and processes do not allow her to see which companies are actively evaluating cloud solutions in real time.

### 1.2 Current State – The Productivity & Prioritization Problem

Sarah's current prospecting process depends on four disconnected systems, each introducing friction and delay.

| Step | Purpose | Limitation |
|------|---------|------------|
| Salesforce (≈2 min/account) | Review account history, revenue tier, and past spending trends. | Data often outdated; reflects past usage, not current purchase intent. |
| LinkedIn (≈3 min/account) | Check leadership changes, hiring activity, and technology discussions. | Unscalable across 1,200 accounts; signals are typically 5–7 days old when seen. |
| Google News (≈3 min/account) | Search for funding, expansion, or new partnerships. | Requires manual reading and synthesis; many relevant triggers are missed. |
| Internal Propensity Scores (≈2 min/account) | Identify "ready-to-buy" accounts using AWS's internal AI models. | 40–50% false positives lead to distrust; six of eight interviewed reps revalidate scores manually. |

**Note:** Propensity scores are AI-generated likelihood rankings that predict which accounts are most likely to buy based on past engagement or usage data. However, their lack of explainability — sometimes referred to as a "black-box" problem — makes them difficult for sales reps to trust or act upon confidently.

**Total research time:** ~10 minutes per account  
**Portfolio coverage:** ~7.2% of accounts analyzed weekly

**How accounts are currently prioritized:**
Due to time constraints, Sarah filters accounts primarily by revenue potential, previous AWS event attendance, or past spend. These are lagging indicators of engagement, not leading indicators of intent. Consequently, dormant accounts often appear "high value," while fast-growing companies showing clear external buying signals never reach her outreach list.

**Result:**
- Hours spent researching low-intent or inactive accounts.
- Missed engagement with active buyers exhibiting early-stage purchase signals.
- Lost opportunities as the optimal 24–48 hour engagement window closes before detection.

### 1.3 Ideal State and Design Specifications

In the ideal state, Sarah starts her day with a real-time intent dashboard that automatically prioritizes her 1,200 accounts based on buying signals integrated from both internal AWS systems and external market intelligence.

**How it works:**
The system processes 1,000+ accounts daily, continuously monitoring hiring activity, funding rounds, executive updates, and event participation. Each account score includes transparent reasoning and source citations, allowing reps to see why an account is prioritized — addressing the trust deficit in current black-box models.

| Design Specification | Current Baseline | Target (Achievable Ideal) | Justification |
|---------------------|------------------|---------------------------|---------------|
| Portfolio coverage | 7% (~72 accounts/week) | 60–80% (~720–960 accounts/week) | Automated signal detection increases visibility 5–8×. |
| Research time per account | 10 minutes | 30–60 seconds | Unified data reduces manual effort by ~90%. |
| Meeting conversion rate | 5% (cold outreach) | 15–20% (signal-based outreach) | Based on Gartner (2023) benchmarks for intent-driven sales. |
| Signal detection rate | ~25% of total signals identified | 75–85% | API integrations enable near real-time monitoring. |

**Note:** See Appendix A for detailed explanations and data assumptions for "Achievable Ideal" targets.

Sarah now spends 90% of her time engaging high-intent buyers instead of manually researching cold accounts — turning data overload into focused selling.

### 1.4 The Gap – Why Current Cannot Become Ideal

Six barriers prevent transformation:

1. **Human cognitive limits**: Monitoring 1,200 accounts requires >100 hours/day—hiring scales headcount, not efficiency
2. **Strategic blindness**: Prioritization relies on lagging indicators (revenue, events), not live intent signals
3. **Missing infrastructure**: No AWS tool consolidates external ASEAN signals; ZoomInfo/6sense cover <20% (ZoomInfo, 2024)
4. **Trust deficit**: 40-50% false positives + black-box models undermine confidence
5. **Economic mismatch**: Commercial platforms cost $50K-200K annually vs. <$0.05/account target
6. **Temporal mismatch**: Manual weekly research misses 24-48 hour signal windows; conversion drops 3-4× (Salesmotion, 2024)

Data exists but cannot be surfaced fast or credibly enough to guide action.

### 1.5 Business Impact – The Cost of Inaction

The cost of inaction compounds across dimensions:

- **Per-rep**: $1.66M unrealized annual pipeline from undetected signals
- **Team-level (40 reps)**: $66M missed pipeline yearly
- **Operational**: 30% of rep time on low-yield research = 12 FTEs performing non-selling tasks
- **Competitive**: AI-guided competitors engage within 48 hours vs. AWS's 5-7 days, reducing conversion 3-4× (Salesmotion, 2024)
- **Strategic**: As ASEAN cloud market reaches $45B by 2025 (Gartner, 2024), AWS risks underpenetrating despite product leadership

This project bridges time inefficiency and signal blindness through scalable, ASEAN-optimized, explainable AI.

### 1.6 Solution Overview

This project introduces a GenAI-powered Signal Intelligence Dashboard designed to improve both the coverage and accuracy of account research. It addresses the six identified barriers through a three-layer architecture comprising automated data ingestion, AI-driven signal analysis, and an explainable user interface.

![Dashboard Interface](images/Dashboard-v1.png)
*Figure 1: Signal Intelligence Dashboard Interface*

<details>
<summary>Click to view additional dashboard screenshots</summary>

![Company Overview](images/company-overview.png)
*Company Profile Overview*

![Talking Points](images/talking-points.png)
*AI-Generated Talking Points*

</details>

**1. Data Ingestion Layer**
Automates the collection of external data across 1,000+ accounts daily using APIs such as Perplexity and Tavily. It is optimized for ASEAN-specific and multilingual sources, overcoming the cognitive and infrastructural limits of manual research. This layer expands portfolio visibility from 7% to near-complete monitoring without additional headcount.

**2. Signal Analysis Layer**
Powered by Claude 3.5 Sonnet, this layer extracts structured insights, applies weighted intent scoring (e.g., hiring 40%, funding 30%, executive updates 20%, events 10%), and produces transparent natural-language reasoning with cited evidence. This explainability directly addresses the trust deficit in prior black-box models, allowing representatives to understand why an account is prioritized and to verify each insight against its source.

**3. Dashboard Interface**
Displays ranked accounts (0–100) with signal breakdowns, citations, and AI-generated talking points. By integrating explainable reasoning within the interface, representatives can validate insights before outreach, fostering confidence and adoption.

## A2. MARKET CONTEXT & VALIDATION

### 2.1 Industry Context

In today's digitally connected environment, sales data is abundant but fragmented. With the advancement of AI and LLMs, it has finally become technically and economically feasible to synthesize these streams into actionable intelligence—for the first time, the cost structure exists to make intent-driven selling at scale achievable.

Gartner (2024) projects 75% of B2B organizations will adopt AI-guided selling by 2025, yet commercial platforms (ZoomInfo, 6sense) cost $50-200/account and cover <20% of ASEAN SMBs—leaving a critical gap for AWS Scale teams targeting <$0.05/account economics.

**Competitive Gap:**

| Solution | Automation | ASEAN Coverage | Explainability | Economics |
|----------|------------|----------------|-----------------|-----------|
| ZoomInfo, 6sense | ✅ | ❌ <20% | ❌ Black-box | ❌ $50-200/account |
| AWS Internal Models | ✅ | ✅ | ❌ 40-50% false positives | ✅ |
| This Project | ✅ | ✅ | ✅ Cited sources | ✅ $0.032/account |

**Internal Validation:** Interviews with 8 AWS representatives (3 Scale, 3 Enterprise, 2 Nurture) confirmed: (1) 7% portfolio coverage due to 10-min research time, (2) 6/8 reps manually revalidate AI scores (40-50% false positives), (3) desire for explainable reasoning with citations. (See Appendix A for detailed findings.)

## A3. METHODOLOGY / CONCEPT DEVELOPMENT

The methodology centered on translating the identified barriers—limited visibility, low accuracy, and lack of trust—into a coherent design concept.

**Conceptual Orientation: Human-in-the-Loop Co-Pilot**

Early exploration contrasted full automation (autonomous prioritization and outreach) with a human-in-the-loop co-pilot model that assists representatives while preserving their judgment.

The latter was adopted because it directly addresses the trust deficit in Section 1.4: automation surfaces insights with transparent reasoning, but users remain responsible for interpretation and action. This reframes AI as a decision-support tool, not a decision-maker, ensuring transparency and user adoption.

**Approach Evaluation**

Three approaches were evaluated against project constraints (explainability, no training data, 3-month timeline, <$0.05/account cost):

| Approach | Data Needs | Explainability | Feasibility | Selection |
|----------|------------|----------------|-------------|-----------|
| Rule-Based | None | Minimal | Moderate | ❌ Fails contextual nuance |
| Predictive ML | High (labeled data) | None (black-box) | Low | ❌ No dataset exists |
| Generative AI | Low (zero-shot) | High (cited reasoning) | High | ✅ Selected |

**Justification**
Generative AI (Claude 3.5) provides explainable, citation-based reasoning without requiring training datasets, aligning with all project constraints while addressing both coverage (scales to 1,000 accounts) and trust (cited sources enable verification). This operationalizes "assisted intelligence" where automation scales data visibility and humans retain contextual judgment.

## A4. FABRICATION OF SPECIMENS/PROTOTYPES

### 4.1 Prototype Evolution Overview

From July to October 2024, four prototypes validated the API-First + GenAI architecture through systematic iteration. Each prototype addressed a specific limitation discovered in the previous, forming cumulative design logic rather than isolated experiments.

| Prototype | Technology Stack | Success Rate | Critical Learning |
|-----------|------------------|--------------|-------------------|
| P1 | Selenium + ScrapingBee | 32-68% | Official sites accurate but scraping architecturally unsound (36% bot blocks) |
| P2 | DuckDuckGo API + Claude 3.5 | 73% | Search APIs reliable but lack structure; missing hiring signals |
| P4 | Perplexity + Tavily + Claude 3.5 | 96% | Specialized APIs + LLM synthesis achieves production-grade performance |

### 4.2 Why Each Transition Mattered

**P1 → P2: Bot Detection Problem (July-August)**

P1 Hypothesis: Official company websites contain the richest data—direct scraping should yield best results.

Reality: Modern websites actively block automation:
- 36% deployed Cloudflare challenges
- 28% used dynamic CSS selectors that break static scrapers
- Required 5 hours/week maintenance to update selectors

Key Decision: Abandon scraping entirely. Bot detection is an architectural barrier, not a technical challenge—fighting it is unsustainable.

P2 Solution: Use DuckDuckGo Search API to retrieve indexed content about companies (titles, snippets, URLs), then feed to Claude 3.5 for synthesis. This mimics human research (Googling a company) while avoiding bot detection.

Result: 73% success rate (+41 percentage points), zero maintenance overhead.

**P2 → P4: Missing Signal Structure (August-October)**

P2 Limitation: Search APIs returned unstructured text snippets that often:
- Duplicated information across results
- Missed recent hiring activity (job boards not well-indexed by DuckDuckGo)
- Lacked recency (cached search results 7-14 days old)

Key Insight: AI reasoning quality depends on input data quality. Claude synthesized well, but "garbage in, garbage out"—it needed structured, real-time signals.

P4 Solution: Dual-API architecture with specialized sources:
- **Perplexity API**: Real-time news/company intelligence across 100+ curated sources with citations (addresses recency + credibility)
- **Tavily API**: Structured job board aggregation with parsed metadata (addresses hiring signal gap)
- **Claude 3.5**: Synthesizes both into explainable scores with natural-language reasoning

Why This Works:
- Perplexity provides timestamped, cited content (e.g., "Posted 3 days ago [TechCrunch]")
- Tavily structures hiring data (role titles, post dates, URLs) vs. unstructured snippets
- Claude combines signals into coherent narrative: "Company X posted 3 cloud roles [Tavily], raised $2M [Perplexity] → 87/100 intent score"

Result: 96% success rate (+23 percentage points), 48-second average processing time, $0.032 cost per account.

### 4.3 Technical Validation

**P4 Architecture:**
Perplexity + Tavily + NewsAPI → Claude 3.5 (AWS Bedrock) → PostgreSQL (profiles) + DynamoDB (raw API responses) → Dashboard UI

**Testing (10 Singapore SMBs, Oct 1-12):**
- ✅ 96% complete profile retrieval (10/10 accounts)
- ✅ Manual benchmark: outputs matched human-researched accuracy across company description, hiring activity, recent news, AWS service fit
- ✅ Processing: 48s average (87% faster than 10-min manual baseline)
- ✅ Cost: $0.032/account (36% below $0.05 viability threshold)

### 4.4 Core Design Principle Validated

**Hypothesis:** API-first access + LLM synthesis outperforms scraping in reliability, transparency, and scalability.

**Evidence:**
- **Reliability**: 32-68% (scraping) → 96% (APIs) crosses production threshold (>90%)
- **Transparency**: APIs provide source URLs + timestamps; Claude generates cited reasoning
- **Scalability**: Zero maintenance (APIs handle bot detection/parsing); parallel calls enable 1,000-account daily processing

Each prototype isolated one variable:
- P1→P2: Data access method (scraping vs. API)
- P2→P4: Data source quality (generic search vs. specialized APIs)

Systematic progression proved that structured, real-time API data + explainable AI reasoning solves the dual problems of coverage (automates 1,000 accounts) and trust (cited sources enable verification).

## A5. TESTING

### 5.1 Purpose of Testing

Testing in this project aimed to investigate two key questions derived from the problem statement:

1. **Problem validation**: How do sales representatives currently prospect, and what barriers prevent them from achieving both scale and accuracy?
2. **Solution validation**: Can explainable automation improve research efficiency and user trust compared to manual prospecting methods?

### 5.2 Methods Used

| Test / Investigation | Purpose | Methodology | Key Findings |
|---------------------|---------|-------------|--------------|
| User Interviews (8 AWS Representatives) | Understand everyday pain points and workflow constraints | Semi-structured interviews across Scale, Enterprise, and Nurture segments | Confirmed 7% portfolio coverage and widespread distrust in automated scores. Six of eight manually revalidate all predictions. |
| Contextual Observation | Observe how representatives prospect in real settings | Shadowed 3 Scale reps performing CRM, LinkedIn, and Google News research for one hour each | Identified repetitive switching between systems and inconsistent prioritisation; average 8–10 minutes spent per account. |
| Manual Benchmark Test (Perplexity API) | Evaluate feasibility of automated research | Compared AI-generated company summaries with manual research for 10 sample accounts | AI synthesis reduced research time by ~90% while maintaining comparable relevance and contextual accuracy. |

### 5.3 Key Insights

Across all methods, findings consistently highlighted time inefficiency, low accuracy in targeting, and lack of trust as the core issues, not resistance to automation itself.

Representatives were receptive to AI assistance provided that it was transparent and verifiable.

Preliminary prototype tests further supported that explainable GenAI reasoning can significantly reduce research time while maintaining or improving decision confidence.

These insights guided the prioritisation of explainability, regional coverage, and efficiency as central design features in the final prototype.

## A6. ANALYSIS

### 6.1 Key Findings

**Finding 1: API-First Architecture Solves Reliability Bottleneck**
Success rate: 32-68% (scraping) → 96% (API-based). Modern websites deploy bot detection (Cloudflare: 36%, dynamic selectors: 28%); P1-P2 required 5 hours/week maintenance, P4 requires zero. Manual benchmark (n=10 accounts) confirmed 100% profile retrieval accuracy.

**Finding 2: Automation Enables Portfolio-Scale Monitoring**
Processing time: 48 seconds vs. 10 minutes manual (87% reduction). Extrapolated: daily monitoring of 100% portfolio vs. current 7.2% weekly. Section 1.1 estimated ~45 high-intent signals/week go undetected; full coverage captures these opportunities ($1.66M annual unrealized pipeline/rep). Critical: signals decay within 48-72 hours—daily refresh enables Day 1-2 engagement vs. manual Day 7+ discovery.

**Finding 3: Explainable Reasoning Addresses Trust Deficit**
P4 outputs include source citations (e.g., "Posted 3 cloud engineer roles [LinkedIn Jobs, Oct 5]"). Section 1.2 found 6/8 reps manually revalidate AI scores due to 40-50% false positives; transparent reasoning makes AI logic auditable, aligning with Gartner's projection that explainability drives 75% AI adoption by 2025.

### 6.2 Validation Status

**Validated:** Technical feasibility (10/10 accounts, 96% success), processing speed (48s), cost ($0.032/account)

**Unvalidated:** User adoption (no rep testing), scale (10 accounts tested, 1,000 needed), revenue impact (industry benchmarks, not actual conversions), ASEAN coverage (Singapore only)

### 6.3 Business Case

**Revenue Model:** 45 signals/week × 52 weeks × 15% conversion × 20% close × $50K = $3.5M/rep  
**Cost:** $384/year per rep ($0.032/account)  
**ROI:** 9,115:1 (breaks even with 1 deal/year)

Validation requires 6-month pilot (Section 9) to track actual meeting bookings and closed revenue.

## A7. FULFILMENT OF DELIVERABLES

### 7.1 Intended Deliverables

A Signal Intelligence Dashboard that automates account research, reducing time from 10 minutes to <1 minute per account while providing explainable AI-driven prioritization.

### What Was Delivered

Functional prototype system consisting of:

1. Data ingestion pipeline (Perplexity + Tavily + NewsAPI → Claude 3.5)
2. PostgreSQL database storing company profiles and signals
3. Web dashboard with account rankings, explainable scores, and AI-generated recommendations

**Validated performance (n=10 test accounts):**
- 96% data retrieval success rate
- 48 seconds average processing time (vs 10 minutes manual)
- $0.032 cost per account (below $0.05 target)

### Assessment

Core technical objectives met: the system successfully automates research with 87% time savings at viable cost.

**Remaining work for production deployment:**
- Scale testing (10 accounts → 1,000 accounts)
- User validation with sales reps
- Salesforce integration

System demonstrates good potential to meet intended deliverables pending pilot deployment (Section 9).

## A8. AWARENESS OF SHORTCOMINGS

### 8.1 Major Shortcomings

1. **Limited Scale Validation (10 accounts)**: System unproven at 1,000-account scale. Resolution: Load testing with 100-account dataset, optimize database queries, validate 2-hour daily refresh window (3 weeks).

2. **No User Validation**: Dashboard designed from interviews but untested with actual reps. Resolution: Deploy to 3 pilot reps, collect feedback, measure adoption rate >80% (4 weeks).

3. **Singapore-Only Coverage**: System untested across ASEAN markets (Indonesia, Malaysia, Thailand, Vietnam) with different languages/data sources. Resolution: Test 20 accounts per market, add region-specific sources where gaps identified (12 weeks, post-pilot).

4. **No Salesforce Integration**: Dashboard standalone; reps manually copy insights to CRM. Resolution: Build bidirectional API sync, auto-populate CRM fields (3 weeks).

### 8.2 Prioritization

| Shortcoming | Timeline | Priority | Rationale |
|-------------|----------|----------|-----------|
| Scale validation | 3 weeks | Critical | Blocks production deployment |
| User validation | 4 weeks | Critical | Validates core value proposition |
| Revenue validation | 6 months | Medium | Long timeline; runs in background |
| Salesforce integration | 3 weeks | Medium | Reduces friction but system usable without |
| ASEAN expansion | 12 weeks | Low | Defer until Singapore validated |

Next semester focus: Complete scale testing → pilot with reps → iterate based on feedback → Salesforce integration. ASEAN expansion deferred to post-graduation or handoff to AWS team.

## A9. PROJECT PLAN

Now that the system works, the next goal is to scale it from prototype to production deployment through pilot testing, iteration, and integration into AWS workflows.

![Project Timeline](images/gantt-chart.png)
*Figure 2: Project Execution Timeline*

### 9.2 Execution Plan

| Phase | Weeks | Key Milestones | Deliverable |
|-------|-------|----------------|-------------|
| Pilot Testing | 1-8 | Week 3: 1,000-account load test<br>Week 6: Deploy to 3 reps<br>Week 8: Usage data collected | Real-world validation |
| Iteration | 9-12 | Week 10: Signal quality improved<br>Week 12: UI refined | False positives <20% |
| Evaluation | 11-13 | Week 13: A/B test results | Productivity comparison |
| Integration | 13-16 | Week 14: Salesforce sync<br>Week 16: 10-rep rollout | Production system |

**Expected Outcome (Week 16):** Fully operational system embedded in AWS sales workflow, validated through real rep usage, with recommendation for regional expansion.
