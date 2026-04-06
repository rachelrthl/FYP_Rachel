A1. Problem Definition & Value Proposition
1.1 The Problem & Persona
Persona: Sarah Tan – Demand Generation Representative, AWS Singapore
Sarah is a Demand Generation Representative (DGR) responsible for identifying potential customers and booking qualified meetings for Account Executives. Her performance is measured by sales-qualified meetings (SQMs) created weekly, directly feeding AWS's new business pipeline. Managing a portfolio of 1,200 SMB accounts each representing potential cloud deals of US$10K–100K annually her target is 10 qualified meetings per week.
DGRs operate under severe time constraints. Interviews with eight AWS sales representatives confirmed that only 12 of 40 weekly working hours are allocated to prospecting; the remainder is consumed by internal meetings, CRM updates, and reporting. This leaves Sarah with a structural problem, not a motivational one:
Time inefficiency: Manual research across four disconnected systems takes ~10 minutes per account, limiting her to 72 accounts per week, just 6–7% of her portfolio.
Signal blindness: Prioritisation relies on static internal metrics (revenue tier, past spend, event attendance) rather than dynamic external buying signals such as hiring activity, funding rounds, or leadership changes.
The consequence is significant: approximately 45 high-intent accounts go undetected each week. At an average AWS SMB deal size of US$37,000, this represents an estimated US$1.66M in unrealised annual pipeline per rep — and US$66M across a 40-rep team.

1.2 Current State: Four Disconnected Systems
Sarah’s workflow requires navigating four separate tools to identify potential buying signals, each introducing friction and delay.
Step
Purpose
Limitation
Salesforce (~2 min)
Account history, revenue tier
Reflects past activity rather than current intent
LinkedIn (~3 min)
Hiring trends, leadership changes
Signals often detected 5–7 days late
Google News (~3 min)
Funding announcements, partnerships
Requires manual synthesis
Internal Propensity Scores (~2 min)
AI-generated readiness rankings
40–50% false positives require manual validation

Total research time averages 10 minutes per account, limiting portfolio coverage to approximately 7% per week.
Prioritisation relies on lagging indicators such as revenue tier and past engagement, causing dormant accounts to appear high-value while companies demonstrating recent growth signals may not be surfaced in time. The effective engagement window for many buying signals is approximately 24–48 hours; manual weekly research cycles often result in outreach occurring too late to capture emerging opportunities (Salesmotion, 2024).
The fragmentation of internal and external intelligence creates a structural barrier to timely and consistent prospecting decisions.

1.3 Ideal State & Design Specifications
Analysis of the current workflow shows that the prospecting challenge is driven by structural limitations in how signals are accessed and interpreted, rather than lack of effort. Key constraints include fragmented data sources, reliance on lagging indicators, limited trust in opaque scoring models, and the short 24–48 hour window in which buying signals remain actionable.
In the ideal state, Sarah begins each day with a Signal Intelligence Dashboard that surfaces high-priority accounts, explains why each account is prioritised, and provides relevant context for outreach. Instead of manually consolidating information across multiple platforms, she is presented with a unified view combining internal CRM context with real-time external signals.
Design specifications translate observed workflow constraints into measurable improvements.
Design Specification
Current Baseline
Target
% Improvement
Justification
Portfolio coverage
7% (~72 accounts/week)
60–80%
+757% to +1043%
Automated monitoring scales research across portfolio
Research time per account
10 minutes
30–60 seconds
−90% to −95%
Unified signal view reduces manual verification
Meeting conversion rate
5%
15–20%
+200% to +300%
Higher-intent outreach improves relevance
Signal detection rate
~25%
75–85%
+200% to +240%
Real-time signals surface earlier indicators

Overall, the design increases effective prospecting capacity by approximately 8–10× while improving confidence in prioritisation decisions.

A1.4 Solution Overview
The Signal Intelligence Dashboard integrates multiple data sources into a single decision-support interface that enables representatives to identify and act on buying signals more efficiently.
The system continuously monitors a defined account portfolio and highlights companies demonstrating observable indicators of potential demand, such as hiring growth, funding activity, expansion signals, or increased digital presence. Each prioritisation recommendation is supported by visible evidence, allowing representatives to understand why an account is surfaced.
Rather than replacing human judgement, the system augments it by structuring relevant intelligence into a format aligned with existing prospecting workflows.
Four core capabilities define the solution:
Internal–external signal integration
Internal CRM indicators such as account tier, historical engagement, and pipeline activity are combined with external signals reflecting recent organisational developments. This allows prioritisation decisions to reflect both relationship context and current business momentum.
Unified signal visibility
External signals from multiple public sources are consolidated into a single account-level view, reducing the need to manually search across platforms such as LinkedIn, company websites, and news sources.
Explainable prioritisation with verifiable sources
Observable signals contributing to each recommendation are displayed together with short summaries and cited sources, enabling representatives to quickly verify relevance without additional research.
Workflow-aligned output structure
Insights are presented in a format consistent with existing CRM workflows, allowing representatives to incorporate signal-based intelligence without significantly changing established prospecting routines.
The solution shifts prospecting from a static account review process into a continuously updated prioritisation workflow informed by real-time market signals.

A1.5 Value Proposition: Improving Allocation of Sales Effort
The primary value of the Signal Intelligence Dashboard lies in helping sales representatives allocate limited time towards accounts most likely to convert, by identifying higher-intent opportunities earlier and more consistently across large portfolios.
By combining internal CRM engagement context with real-time external signals, the system identifies accounts demonstrating observable indicators of potential demand, allowing outreach effort to be directed towards opportunities with higher intent.
The value created can be understood across three levels:
Operational value
Increases portfolio coverage within the same time constraint, reducing missed opportunities.
Decision value
Provides prioritisation rationale with cited sources, allowing representatives to quickly verify signals without manual cross-checking, supporting faster and more confident prospecting decisions.
Strategic value
Engaging accounts when there are observable signs of interest increases likelihood of conversion and improves probability of achieving sales targets.
The dashboard therefore improves how representatives allocate attention across large portfolios, increasing the likelihood that outreach effort is focused on higher-intent opportunities.
2.1 Industry Context
In today's digitally connected environment, sales data is abundant but fragmented across multiple platforms. Advances in AI and large language models now make it technically feasible to synthesise these signals into structured insights, enabling intent-driven selling at scale.
Gartner (2024) projects that 75% of B2B organisations will adopt AI-guided selling workflows by 2025. However, leading commercial platforms such as ZoomInfo and 6sense are primarily optimised for North American markets, offering limited coverage of ASEAN SMBs while operating at price points that are difficult to justify for large-scale prospecting portfolios. Internal scoring models address cost constraints but often lack transparency, resulting in low trust and frequent manual verification.
Together, these limitations create a gap between the availability of external buying signals and the ability of sales representatives to confidently act on them within time-constrained workflows.
Internal Validation: Interviews with 8 AWS representatives (3 Scale, 3 Enterprise, 2 Nurture) confirmed: (1) 7% portfolio coverage due to 10-min research time, (2) 6/8 reps manually revalidate AI scores (40-50% false positives), (3) desire for explainable reasoning with citations. (See Appendix A for detailed findings.)

A3. Methodology / Concept Development
The methodology focused on translating key behavioural constraints identified in earlier sections—limited portfolio visibility, low trust in opaque scoring models, and fragmented external signals—into a coherent design approach.
Conceptual Orientation: Human-in-the-Loop Co-Pilot
Early concept exploration contrasted two design directions: full automation, where the system independently prioritises accounts, and a human-in-the-loop co-pilot model that surfaces intelligence while preserving representative judgement.
The co-pilot model was selected as it directly addresses the trust gap identified in the research findings. Interview results showed that 6 of 8 representatives manually verify internally generated scores due to concerns about false positives. Increasing automation without improving transparency would therefore be unlikely to improve adoption.
Positioning the system as a decision-support tool allows signals to be surfaced with visible reasoning, while representatives remain responsible for interpreting relevance and determining outreach actions. This aligns with assisted intelligence principles, where automation enhances human decision-making without replacing it.
Approach Evaluation
Three technical approaches were evaluated against key project constraints: explainability requirements, absence of labelled training data, three-month development timeline, and a <$0.05 per-account cost constraint.
Approach
Data Needs
Explainability
Feasibility
Selection
Rule-based filtering
None
Minimal contextual flexibility
Moderate
❌ Insufficient nuance
Predictive machine learning
High (labelled data)
Low transparency
Low
❌ No dataset available
Generative AI synthesis
Low (zero-shot)
High (cited reasoning)
High
✅ Selected

Generative AI enables synthesis of fragmented external signals without requiring historical training datasets, while producing citation-supported reasoning that improves transparency and verifiability of prioritisation logic.
This supports the co-pilot design orientation by combining scalable signal aggregation with explainable outputs, allowing representatives to maintain contextual judgement while benefiting from increased visibility across large account portfolios.
A4. Prototype Evolution & System Design
4.1 Prototype Evolution
Between July and October 2024, three prototype iterations were developed to improve how external company signals could be reliably collected and synthesised into actionable sales intelligence. Each iteration tested a different research method, progressing from direct extraction to structured multi-source synthesis.
Prototype
Tech Stack
Method
Key Limitation
Improvement
P1
Selenium + ScrapingBee
Direct website scraping
Blocked by bot protection, unstable page structures
Established feasibility of automated signal collection
P2
DuckDuckGo API + Claude 3.5
Search-based retrieval
General search results often stale and missing hiring signals
Improved reliability and reduced maintenance effort
P3
Perplexity + Tavily + Claude 3.5
Multi-source synthesis
Higher design complexity
Achieved high signal coverage with explainable outputs

P1 → P2: From Direct Extraction to Search-Based Research
The first prototype attempted to extract information directly from company websites using Selenium and ScrapingBee. While websites contain rich company information, 36% deployed bot protection and 28% used dynamic page structures requiring constant maintenance (~5 hours per week). This made scraping operationally unstable.
The second prototype shifted to DuckDuckGo Search API, which retrieves publicly indexed information such as news articles and company mentions. This approach better reflects how human representatives conduct research and improved reliability to 73%, while significantly reducing maintenance requirements.
P2 → P3: From Single-Source Search to Specialised Research Agents
While search APIs improved stability, results were often cached (7–14 days delay), duplicated across sources, and inconsistent in capturing hiring signals from job platforms.
The final prototype adopted a multi-source approach using Perplexity API and Tavily API, supported by Claude 3.5. Instead of relying on one general search source, the system distributes research tasks across specialised “agents”:
• Perplexity retrieves real-time company developments (e.g. funding, partnerships, product launches) with cited sources
• Tavily retrieves structured hiring signals from job postings
• Claude 3.5 synthesises signals into prioritised summaries with supporting citations
This division of research tasks improves signal completeness because each source focuses on a specific information domain, similar to assigning specialised analysts to different research areas.
Result
The final architecture achieved a 96% signal retrieval success rate, average processing time of 48 seconds per account, and cost efficiency of approximately $0.032 per account. The results validate an API-first, multi-source synthesis approach capable of generating scalable and explainable account intelligence.
The prototype evolution demonstrates how methodological improvements in signal retrieval directly enhanced reliability, coverage, and interpretability of outputs, supporting the human-in-the-loop co-pilot design described in Section A3.
4.2 From Problem to Features: Signal Intelligence System Design
The Signal Intelligence System translates the behavioural constraints identified in A1 into a structured multi-agent architecture. Instead of relying on a single data source, the system distributes research tasks across specialised agents, each responsible for detecting a specific category of commercial signal. These signals are then synthesised into a unified account view to support faster and more transparent prioritisation decisions.
Each agent is designed to directly address an observed workflow constraint, ensuring the system solves actual visibility and trust gaps rather than assumed technical problems.

Problem → Agent Mapping
Behavioural Constraint (A1)
Design Requirement
Agent
Function
fragmented internal and external visibility
unified account context
Account Context Agent
integrates Salesforce CRM records as internal reference layer
limited understanding of company activities
structured company-level intelligence
Market Research Agent
builds contextual understanding of company business model, industry focus, hiring activity and technology signals
missed external buying signals
continuous monitoring of company developments
News Signals Agent
detects events such as funding, expansion, partnerships and product launches
low trust in opaque prioritisation logic
explainable reasoning
Synthesis Agent
generates propensity score supported by cited signals
high research time per account
rapid signal interpretation
Synthesis Agent
produces structured summaries interpretable within 60 seconds


Specialised Agent Roles
Account Context Agent (internal signal foundation)
The Account Context Agent synchronises Salesforce CRM records including accounts, contacts, and opportunities into a structured internal dataset. This provides baseline visibility into existing relationships, engagement history, and account ownership, allowing external signals to be interpreted relative to known business context.
Providing a unified internal reference layer addresses the fragmentation issue identified in A1, where representatives previously needed to manually cross-reference CRM records with external research sources.

Market Research Agent (company context and growth indicators)
The Market Research Agent builds a structured understanding of what each company does and how it operates. Using web-grounded research, the agent identifies key information including business model, industry positioning, product offerings, geographic presence, and indicators of organisational growth such as hiring activity.
Hiring signals are included within this agent because recruitment patterns often reflect expansion initiatives, investment in technical capabilities, or preparation for increased operational scale.
By combining company profile information with observable growth indicators, the agent provides representatives with clearer context on why a company may require cloud infrastructure or digital solutions, improving relevance of outreach decisions.

News Signals Agent (company development triggers)
The News Signals Agent retrieves recent company-related news, capturing observable developments such as funding announcements, acquisitions, partnerships, product launches, and regional expansion activity.
These signals often indicate moments of organisational change where companies are more likely to evaluate new technology solutions. Continuous monitoring improves visibility into time-sensitive opportunities that may not yet be reflected in internal CRM data.

Synthesis Agent (signal integration and prioritisation logic)
The Synthesis Agent consolidates signals from all upstream agents and transforms fragmented information into a structured account summary. Instead of presenting isolated data points, signals are synthesised into a propensity score supported by cited reasoning explaining why an account may represent a higher likelihood opportunity.
Embedding citations directly within the output ensures prioritisation logic remains transparent and verifiable, addressing the trust gap identified in A1 where representatives reported manually validating opaque scoring outputs.
The agent also standardises output into a consistent structure interpretable by the front-end dashboard, enabling representatives to quickly assess relevance without manually aggregating information across sources.
Example structured output:
overall_score: 78

company_context:
Provides logistics automation solutions across Southeast Asia

key_signals:
• hiring for cloud infrastructure engineers
• recent regional expansion announcement
• partnership integration requiring data infrastructure scaling

reasoning:
Observed expansion activity and technical hiring suggest increased likelihood of near-term cloud infrastructure needs.

sources:
company website, LinkedIn, TechCrunch

Design Implication
Separating research responsibilities across specialised agents improves both completeness and interpretability of account intelligence. The Market Research Agent provides foundational understanding of company context, while the News Signals Agent identifies time-sensitive developments that may trigger buying needs.
The Synthesis Agent integrates these signals into prioritised insights that remain transparent to the user, supporting the human-in-the-loop co-pilot model established in A3.
By structuring intelligence generation around behavioural constraints rather than technical components, the Signal Intelligence System reduces manual research effort while improving confidence in account prioritisation decisions.
4.3 Prioritisation Logic and Propensity Scoring
The Signal Intelligence System converts fragmented company signals into a structured propensity score indicating likelihood of near-term technology purchasing needs. Scoring logic is grounded in both practitioner decision heuristics identified in A1 interviews and observable market indicators linked to digital infrastructure adoption.
Interview findings showed that representatives assess account priority based on observable indicators of organisational change. Commonly cited signals included hiring for technical roles, expansion into new markets, product launches, and recent funding events. Six of eight representatives indicated that hiring activity for engineering or data roles often signals preparation for infrastructure scaling, while company announcements relating to partnerships or acquisitions frequently trigger outreach prioritisation.
These practitioner heuristics are consistent with broader market findings. Gartner (2024) reports that over 70% of digital transformation initiatives involve cloud infrastructure investment, while CB Insights (2024) finds that companies typically increase software spending within 6–12 months following funding events. Hiring growth has also been shown to correlate with expansion activity, particularly for firms scaling digital capabilities (LinkedIn Economic Graph, 2023).
Based on these behavioural and market indicators, signals identified by upstream agents are grouped into four evaluation dimensions:
• company fit – alignment with target customer characteristics such as industry relevance and operational scale
• growth activity – indicators of organisational expansion including hiring activity, market entry, and product development
• technology readiness – observable investment in digital capabilities such as technical hiring and infrastructure-related initiatives
• market momentum – time-sensitive developments including funding announcements, acquisitions, and strategic partnerships
Signals across these dimensions are synthesised into a weighted propensity score. Weighting reflects relative predictive relevance of each signal category rather than simple frequency counts. For example, hiring activity for cloud engineering roles contributes more strongly to technology readiness than general company news mentions.
Each score is accompanied by cited reasoning explaining how specific signals contributed to prioritisation. This ensures transparency of decision logic and allows representatives to validate recommendations before taking action, addressing the trust deficit identified in A1 where opaque scoring systems required manual verification.
Example scoring structure:
overall_score: 78

dimension_scores:
company_fit: 18
growth_activity: 20
technology_readiness: 24
market_momentum: 16

reasoning:
Company expanding technical team and integrating newly acquired systems, indicating potential near-term infrastructure scaling needs.

sources:
LinkedIn hiring data, TechCrunch acquisition coverage
By structuring prioritisation logic around observable commercial indicators supported by both field insight and market research, the system balances automation efficiency with human judgement. Representatives retain decision control while benefiting from systematic visibility across large account portfolios, improving both speed and confidence of outreach prioritisation decisions.

4.4 Workflow Integration and User Interaction Design
The Signal Intelligence System is designed to integrate directly into the existing workflow of AWS representatives by reducing the need to manually gather account intelligence across multiple platforms. Instead of switching between Salesforce, LinkedIn, and news search tools, representatives access pre-synthesised intelligence through a structured dashboard interface.
The workflow follows a sequential decision flow, allowing representatives to move from portfolio-level prioritisation to account-level strategy development.

Step 1: Portfolio Prioritisation (Account List View)
Representatives begin by filtering their account portfolio based on territory, country, or account owner. The Account List View ranks accounts using the propensity score (0–100), allowing representatives to quickly identify high-priority opportunities within their assigned region.
Priority tier filters (High, Medium-High, Medium) enable rapid segmentation of accounts requiring immediate attention. Data quality indicators also signal confidence levels of external intelligence coverage.
This replaces the manual triage process described in A1, where representatives previously searched across Salesforce, LinkedIn, and Google News individually, requiring approximately 10 minutes per account.


Step 2: Company Understanding (Account Detail View)
Selecting an account opens the Account Detail View, which provides a unified company profile combining internal CRM data with AI-generated external intelligence.
The view includes:
• company business description
• operating markets and regions
• financial and organisational signals
• recent developments identified through external research
• cited sources supporting each insight
This provides the “single pane of glass” identified as the primary unmet need in A1, allowing representatives to understand company context without conducting separate research.



Step 3: Stakeholder Identification (Organisation Structure View)
The Organisation Structure & Stakeholders View maps key decision makers, influencers, and potential champions within each account. Role classifications (Critical / High / Medium) help representatives identify relevant stakeholders prior to outreach.
Stakeholder visibility was highlighted in A1 interviews as an important factor influencing outreach confidence, particularly when entering unfamiliar accounts.


Step 4: Opportunity Framing (Propensity Score & Pain Points View)
The Propensity Score & Pain Points View presents a breakdown of weighted scoring factors:
• AWS usage signals
• engagement signals
• technology readiness
• market momentum
An impact-urgency matrix highlights identified business challenges inferred from external signals, allowing representatives to understand why an account is prioritised and what potential needs may exist.
Providing transparent reasoning addresses the trust deficit identified in A1, where representatives reported manually validating opaque scoring outputs before taking action.


Step 5: Outreach Preparation (Pursue Strategy View)
The Pursue Strategy View generates contextualised talking points and outreach angles anchored to detected company signals. Suggested messaging references observable developments such as hiring expansion, acquisitions, or regional growth initiatives.
Representatives can adapt suggested messaging to align with their communication style while maintaining relevance to account context.
Pilot feedback indicated this feature reduced preparation time for territory planning and increased confidence in outreach relevance.


A5. Testing
5.1 Purpose of Testing
Testing addressed two sequential questions corresponding to the project's two phases:
Problem validation (July–August 2024): How do sales representatives currently prospect, and what barriers prevent scale and accuracy?
Solution validation (October 2024–present): Does RubyChan v2 improve research efficiency, and do users trust and adopt explainable AI-driven prioritisation?

5.2 Problem Validation Methods
Test
Purpose
Methodology
Key Findings
User Interviews (n=8)
Understand workflow pain points
Semi-structured interviews across Scale, Enterprise, Nurture segments
Confirmed 7% portfolio coverage; 6/8 reps manually revalidate AI scores due to 40–50% false positives
Contextual Observation
Observe prospecting in real settings
Shadowed 3 Scale reps for one hour each across CRM, LinkedIn, Google News
Identified repetitive system-switching; confirmed 8–10 min average per account
Manual Benchmark
Evaluate automated research feasibility
Compared AI-generated summaries with manual research for 10 accounts
AI synthesis reduced research time by ~90% with comparable accuracy

These methods consistently surfaced three themes: time inefficiency, signal blindness, and lack of explainability which directly shaped the design requirements in A4.
5.3 Usability Evaluation (System Usability Scale)
Usability of the dashboard was evaluated using the System Usability Scale (SUS). One participating sales representative completed the questionnaire after interacting with the five main views (Account List, Account Detail, Organisation Structure, Propensity Score, Pursue Strategy).
SUS score: 80, indicating strong perceived usability.
The main friction point related to initial setup complexity due to local deployment requirements rather than interface design. Once operational, users found navigation intuitive, particularly the ranked account list and priority filters. Some uncertainty was observed in interpreting the weighting logic behind the propensity score, suggesting explanation clarity can be further improved in future iterations.
Full SUS instrument is provided in Appendix G.

5.4 Solution Validation: Pilot Field Survey
Following onboarding of 20 DGRs and CSRs, a 38-question survey was administered to evaluate perceived usefulness and workflow fit (n=2; directional findings).
Both respondents rated the 3-tab workflow (Propensity Score, Know the Customer, Pursue Strategy) 5/5 for intuitiveness, with information retrieval speed also rated 5/5, supporting the 48-second benchmark observed in pilot testing.
Understanding of propensity score logic showed mixed clarity: one respondent rated usefulness 5/5, while the other rated usefulness 3/5 and factor understanding 2/5, highlighting that weighting logic is not immediately intuitive. One respondent noted that greenfield accounts may be penalised due to lack of engagement history, suggesting potential scoring bias.
The Pursue Strategy view was identified as the most valuable feature, particularly the WHAT, HOW, and WHO components. Likelihood of using AI-generated talking points averaged 4.5/5.
Perceived accuracy averaged 4.5/5, freshness 4/5, and integration of internal and external signals 5/5. Both respondents rated likelihood to close more deals and recommend the tool 5/5, with overall satisfaction 4/5.
Full survey instrument provided in Appendix G.
A6. Analysis
6.1 System Design Insight
The prototype progression demonstrates that effective AI-based sales research depends on structuring how information is retrieved before applying LLM synthesis.
Initial approaches showed that simply increasing access to data sources does not guarantee useful insights. Direct scraping produced unreliable outputs due to bot protection and unstable page structures, while early search-based approaches often returned generic or incomplete information when queries were not sufficiently targeted. These iterations revealed that LLM output quality is highly dependent on the relevance and structure of input data.
The final design addressed this by structuring the research workflow into specialised agents aligned to specific signal categories. The News Agent retrieves recent company developments, the Research Agent performs grounded search to identify company context, technology signals, and hiring activity, while the Account Agent retrieves internal CRM data. These signals are synthesised by the Consolidation Agent into a structured company profile and propensity score.
Assigning each agent a clearly defined task improves data relevance by ensuring that retrieved information aligns with predefined analytical objectives. Instead of relying on a single model to determine what information may be important, the system guides retrieval according to specific signal types required for sales evaluation.
A key learning is that LLMs produce more useful insights when applied to structured and relevant inputs rather than broad unfiltered data. The multi-agent architecture therefore functions as a data quality control layer, ensuring that signals provided to the synthesis model are aligned with decision-making needs. Performance improvements observed in the final prototype reflect improved data structuring rather than model capability alone.

6.2 User Workflow Insight
User feedback suggests that the primary value of the system lies in reducing the effort required for representatives to evaluate account context and prioritise outreach decisions.
Sales representatives often operate under time constraints when reviewing large account portfolios, requiring them to piece together signals from multiple fragmented sources such as LinkedIn, company websites, news articles, and CRM data. By consolidating internal and external signals into a single structured profile, the system provides a clearer starting point for determining which accounts warrant further investigation.
In one pilot example, a representative filtered for high-propensity accounts within their territory and reviewed a company demonstrating hiring expansion and recent business developments surfaced by the Research Agent. Using the consolidated company profile and suggested talking points from the Pursue Strategy view, the representative initiated outreach via phone referencing the surfaced insights. The interaction progressed into a Sales Qualified Meeting (SQM). While this example does not establish causal proof of improved conversion performance, it illustrates how structured signal visibility can support faster transition from research to engagement preparation.
An additional insight is that the system supports territory planning workflows, even though this was not an explicitly defined design objective. One CSR noted that the system “helps me in my territory planning in a way no existing tool does.” Representatives indicated that reviewing accounts through a ranked portfolio view improved their ability to identify which accounts require deeper evaluation and how effort should be allocated across their territory.
This emergent use suggests that unified internal and external account intelligence addresses a broader workflow need beyond immediate lead prioritisation. Rather than replacing user judgement, the system supports decision-making by reducing cognitive effort required to interpret fragmented signals.
Overall, findings indicate that AI provides the greatest value when it structures relevant signals into interpretable context that supports prioritisation decisions and outreach preparation.
A7 Fulfilment of Deliverables
7.1 Delivery of Intended System Capability
The primary project objective was to develop an AI-assisted research system capable of consolidating fragmented internal and external company signals into structured insights supporting account prioritisation decisions.
This objective was achieved through the development of a functional dashboard application implementing a multi-agent research architecture. The system retrieves company context, hiring signals, technology indicators, and recent developments, and synthesises these signals into structured company profiles and propensity scores. These outputs support representatives in evaluating account relevance and preparing outreach strategies.
The implemented workflow demonstrates that structured signal retrieval combined with LLM synthesis can produce interpretable company intelligence aligned with sales decision-making needs.

7.2 Integration into Sales Research Workflow
The delivered application was deployed within a real sales environment involving DGR and CSR roles, enabling evaluation under practical workflow conditions using actual account data.
User interactions indicate that consolidating internal CRM information with external company intelligence reduces the need to manually search across multiple fragmented sources such as LinkedIn, company websites, and news articles. Structured company profiles provide a clearer starting point for understanding account context, while propensity scoring supports prioritisation across large account portfolios.
An emergent observation is that the system also supports territory planning activities by improving visibility into account-level signals across a representative’s portfolio. This suggests that unified internal-external intelligence addresses broader workflow needs beyond initial lead evaluation.

7.3 Extent of Deliverable Realisation
The project progressed beyond conceptual prototyping into deployment within an operational sales environment, enabling evaluation under real workflow conditions. This allowed assessment not only of technical feasibility, but also of practical usability in supporting account research and prioritisation activities.
Findings presented in Section A5 indicate that users are able to interpret and apply the generated insights within their existing research process. While longer-term commercial impact such as influence on conversion outcomes requires extended observation, the implementation of a working internal tool demonstrates that the intended deliverable of improving access to structured account intelligence has been realised in practice.

A8. Awareness of Shortcomings
8.1 Major Shortcomings
1. Cloud Deployment Blocked by Data Governance Policy
The most significant production barrier is an internal AWS policy preventing deployment of applications handling customer account data on non-approved infrastructure. This forces users to run RubyChan v2 locally via command line — a setup process that creates a prohibitive barrier for non-technical business personas. Of the 20 onboarded users, several required assisted setup, and broader rollout beyond the initial cohort is effectively blocked until this is resolved. This shortcoming was not anticipated at interim stage; it emerged as a direct consequence of attempting real deployment with real customer data, and represents the highest-priority item for production readiness.
Resolution: Engage AWS IT and legal teams to obtain approval for an internally hosted deployment on approved AWS infrastructure. Given that the system already runs entirely on AWS services (Bedrock, DynamoDB, EC2), the technical lift is minimal — the bottleneck is approval, not engineering. Estimated timeline: 4–6 weeks pending internal review.
2. No Bidirectional Salesforce Integration
RubyChan v2 currently ingests Salesforce data via static export rather than live API sync. This means account data requires manual refresh, and AI-generated insights cannot be written back to CRM records — forcing reps to manually copy talking points and scores into Salesforce. Export functionality was the most frequently requested feature enhancement in pilot feedback, confirming this as a user-validated friction point rather than anticipated technical debt.
The resolution path has two dependencies that are outside the project's direct control. First, cloud deployment approval (Shortcoming 1) must be secured before a stable API endpoint exists. Second, Salesforce MCP server access requires internal IT and security permissions within AWS — an approval process governed by enterprise data governance policy rather than engineering capacity. Both dependencies mean this shortcoming cannot be resolved on a fixed timeline regardless of technical readiness.
Resolution: Submit formal request for Salesforce MCP server access in parallel with cloud deployment approval. Technical implementation (bidirectional sync and CRM field population) is estimated at 3 weeks once both approvals are obtained. Recommended as a post-graduation handoff item to the AWS sales operations team if approvals extend beyond the project timeline.

8.2 Prioritisation
Shortcoming
Timeline
Priority
Rationale
Cloud deployment approval
4–6 weeks
Critical
Blocks all further onboarding and production use
Salesforce bidirectional sync
3 weeks post-deployment
Critical
User-validated as primary workflow friction point

A9. Impact & Visibility
9.1 Immediate Impact: AWS Singapore Sales Team
The system is currently used within the AWS Singapore Scale sales team to support account research using real customer data. It helps representatives quickly understand company context by combining internal CRM information with external signals such as hiring activity, company developments, and technology indicators in one place.
This reduces the need to manually search across multiple sources such as LinkedIn, company websites, and news articles within the short 24–48 hour engagement window identified in A1.
An additional outcome observed during usage is support for territory planning. Representatives reported that having a structured overview of account signals makes it easier to review their portfolio and decide which accounts require deeper focus. Previously, this required manually gathering information across different tools.
This suggests the system may support both prospect research and broader account planning workflows.

9.2 Organisational Potential
The system is designed so that data sources can be adjusted for different markets, making it possible to apply the same workflow structure across other sales teams.
Estimated operating cost is approximately $384 per representative per year, suggesting that the system can be maintained at relatively low cost compared to the potential value of improved account prioritisation.
There has already been interest from teams in other regions including APJ, France, and Canada, indicating that the challenge of fragmented account research is not unique to a single geography.
Further testing across additional teams would help determine how consistently the workflow benefits can be observed.

9.3 Industry Relevance
The problem of fragmented account intelligence is common across B2B sales environments where useful information is spread across multiple tools.
This project demonstrates how AI can be used to structure internal and external signals into a single view that helps users understand account context more efficiently.
Rather than replacing decision-making, the system supports users by organising relevant information in a clearer format. The observed use in territory planning suggests that structured signal consolidation may also support broader account strategy workflows beyond the initial scope of lead research.

REFERENCES (APA style)
Arrieta, A. B., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A., García, S., Gil-López, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020). Explainable artificial intelligence (XAI): Concepts, taxonomies, opportunities and challenges toward responsible AI. Information Fusion, 58, 82–115.
https://www.sciencedirect.com/science/article/abs/pii/S1566253519308103
Bangor, A., Kortum, P., & Miller, J. (2009). Determining what individual SUS scores mean: Adding an adjective rating scale. Journal of Usability Studies, 4(3), 114–123.
Brooke, J. (1996). SUS: A quick and dirty usability scale. In P. Jordan, B. Thomas, B. Weerdmeester, & I. McClelland (Eds.), Usability Evaluation in Industry. London: Taylor & Francis.
Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319–340.
https://www.researchgate.net/publication/200085965
Forrester Research. (2023). B2B buyer journey benchmark report 2023.
https://www.forrester.com/press-newsroom/2023-forrester-b2b-buyers-journey/
Gartner. (2024a). Forecast analysis: Public cloud services, worldwide, 2024.
https://www.gartner.com/en/newsroom/press-releases/2024-05-20-gartner-forecasts-worldwide-public-cloud-end-user-spending-to-surpass-675-billion-in-2024
Gartner. (2024b). Predicts 2025: AI-guided selling becomes the new standard for B2B sales.
https://www.gartner.com/en/newsroom/press-releases/gartner-predicts-75--of-b2b-sales-organizations-will-augment-tra
Salesforce Research. (2023). State of Sales (5th ed.).
https://media.bitpipe.com/io_32x/io_322542/item_2864478/SALES_TrendsinSales_PDF_V3_Sales%20Cloud.pdf
Salesmotion. (2024). Case studies: Incredible Health and Analytic Partners.
https://salesmotion.io/customer-story-incredible-health
ZoomInfo Technologies Inc. (2024). Customer Impact Report.
https://downloads.ctfassets.net/kyld7105l6mt/6RwJmVrDvEqjUUgz8fZmud/2c2fd86f4172552f42a1ee4d2f5fc36e/ZoomInfo-Customer-Impact-Report-2024.pdf