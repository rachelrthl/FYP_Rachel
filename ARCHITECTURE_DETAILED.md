# RubyChan v2 - Detailed Architecture Documentation

## Executive Summary

RubyChan v2 is a multi-tier microservices architecture that transforms Salesforce account data into actionable sales intelligence using AI-powered analysis. The system aggregates data from multiple sources, enriches it with real-time news and company research, and generates comprehensive business insights with propensity scoring.

## System Architecture Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Frontend Layer                               │
│                         Next.js (Port 3000)                          │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
    ┌───────────────┐ ┌──────────────┐ ┌─────────────┐
    │ Consolidated  │ │ AI Analysis  │ │   Direct    │
    │     API       │ │     API      │ │   API       │
    │  Port 5004    │ │  Port 5005   │ │   Calls     │
    └───────┬───────┘ └──────┬───────┘ └─────────────┘
            │                │
            │                ▼
            │        ┌──────────────┐
            │        │ Consolidated │
            │        │     API      │
            │        │  Port 5004   │
            │        └──────┬───────┘
            │               │
    ┌───────┼───────────────┼───────────────┐
    ▼       ▼               ▼               ▼
┌──────────┐    ┌──────────┐       ┌──────────┐
│ Account  │    │  News    │       │ Research │
│   API    │    │   API    │       │   API    │
│ Port 5001│    │ Port 5002│       │ Port 5003│
└────┬─────┘    └────┬─────┘       └────┬─────┘
     │               │                   │
     ▼               ▼                   ▼
┌────────┐     ┌──────────┐        ┌──────────┐
│ SQLite │     │ DynamoDB │        │ DynamoDB │
│  Local │     │   AWS    │        │   AWS    │
└────────┘     └────┬─────┘        └────┬─────┘
                    │                    │
                    ▼                    ▼
              ┌──────────┐         ┌──────────┐
              │ Bedrock  │         │ Bedrock  │
              │ Claude   │         │  Nova    │
              │ 3.5/Haiku│         │ Premier  │
              └──────────┘         └──────────┘
                    │
                    ▼
              ┌──────────┐
              │NewsAPI.ai│
              │ External │
              └──────────┘
```

## Service Layer Details

### 1. Account API (Port 5001)

**Purpose**: Serve Salesforce account data from local SQLite database

**Technology Stack**:
- Flask 2.3-3.1
- Python 3.8+
- SQLite database (local file: `source_data/sfdc.db`)
- No external dependencies

**Data Sources**:
- Excel files converted to SQLite:
  - Account and Contact.xlsx
  - Account and Oppty.xlsx
  - Account and Revenue.xlsx
  - Account.xlsx
  - TopGainer.xlsx

**Database Schema**:
- **Account** table: 18,483 records (accountId, accountName, territory)
- **Contact** table: 64,299 records (contactId, accountId, email, phone, title)
- **Opportunity** table: 44,603 records (opptyId, accountId, stage, totalOppty)
- **TopGainer** table: 303 records (revenue growth metrics)
- **Revenue** table: 28,422 records (monthly revenue data, actual + projected)

**Key Endpoints**:
- `GET /accounts` - All accounts
- `GET /contacts?accountId={id}` - Contacts for account
- `GET /opportunities?accountId={id}` - Opportunities for account
- `GET /topgainers` - Top revenue gainers
- `GET /account/{id}` - Complete account details with all related data

**Performance**:
- Response time: <100ms
- No external API calls
- Direct SQLite queries

**AWS Services**: None (local SQLite only)

---

### 2. News API (Port 5002)

**Purpose**: Generate AI-powered news insights using NewsAPI.ai and AWS Bedrock Claude

**Technology Stack**:
- Flask 2.3-3.1
- Python 3.8+
- AWS SDK (boto3)
- NewsAPI.ai client
- Pydantic for validation

**External Services**:
- **NewsAPI.ai**: Article retrieval and search
- **AWS Bedrock**: Claude 3.5 Sonnet for AI summaries
- **AWS DynamoDB**: News insights storage

**AWS Services Used**:

1. **AWS Bedrock**:
   - Model: `anthropic.claude-3-5-sonnet-20241022-v2:0`
   - Purpose: Generate business insights and AWS opportunities from news articles
   - API: Converse API
   - Token limit: 4096 output tokens
   - Processing time: 7-10 seconds per summary

2. **AWS DynamoDB**:
   - Table: `News`
   - Partition Key: `accountId` (string)
   - Purpose: Cache news insights for fast retrieval
   - No TTL (permanent storage until overwritten)
   - Attributes: accountId, company_name, country, articles (list), news_summary, metadata, timestamp

**Processing Pipeline** (5 steps, 15-20 seconds total):

1. **Build Query** (4-5s): Use Bedrock Claude Haiku to generate optimal NewsAPI.ai query
   - Input: company name, country
   - Output: Keywords array, language codes, search parameters
   - Model: Claude Haiku (fast, cost-effective)

2. **Fetch Articles** (3-5s): Retrieve articles from NewsAPI.ai
   - Search by keywords and language
   - Filter by date range (last 90 days)
   - Return top 10 most relevant articles

3. **Generate Summary** (7-10s): Create AI insights using Bedrock Claude Sonnet
   - Input: Articles array + company context
   - Output: 3-5 sentence business analysis highlighting AWS opportunities
   - Model: Claude 3.5 Sonnet (advanced reasoning)

4. **Create Response** (<1s): Assemble complete response with metadata

5. **Store Data** (1-2s): Persist to DynamoDB for future retrieval

**Key Endpoints**:
- `GET /news/research?company_name={name}&country={country}&account_id={id}` - Generate fresh insights (15-20s)
- `GET /news/{account_id}` - Retrieve cached insights (1-2s)
- `GET /health` - Health check

**Multi-Language Support**:
- ASEAN countries: SG, MY, ID, TH, PH, VN, MM, KH, LA, BN
- Automatic language detection based on country
- English + local language for most countries

**Performance**:
- Fresh generation: 15-20 seconds
- Cached retrieval: 1-2 seconds
- Articles per request: 10 (configurable)

---

### 3. Company Research API (Port 5003)

**Purpose**: Generate comprehensive company intelligence using Amazon Nova Premier with web grounding

**Technology Stack**:
- Flask 3.x
- Python 3.9+
- AWS SDK (boto3 1.42+)
- Pydantic for validation

**AWS Services Used**:

1. **AWS Bedrock**:
   - Model: `us.amazon.nova-premier-v1:0`
   - Purpose: Real-time web grounding for company research
   - API: Converse API with tool use (web search)
   - Token limits: 
     - Business Profile: 2400 tokens
     - Hiring Intelligence: 1200 tokens
     - Technology Adoption: 1800 tokens
   - Processing time: 30-40 seconds (parallel queries)

2. **AWS DynamoDB**:
   - Table: `CompanyOverview`
   - Partition Key: `accountId` (string)
   - Purpose: Cache research results
   - No TTL (permanent storage)
   - Attributes: accountId, company_name, country, analysis (nested), metadata, timestamp

**Processing Pipeline** (4 steps, 30-40 seconds total):

1. **Build Queries** (<0.01s): Create 3 specialized prompts
   - Business Profile query
   - Hiring Intelligence query
   - Technology Adoption query

2. **Execute Searches** (30-40s): Parallel Bedrock API calls with web grounding
   - 3 concurrent Nova Premier invocations
   - Each query searches web in real-time
   - Extracts content + citations from web sources
   - Returns structured analysis with source URLs

3. **Process Results** (<0.01s): Clean and structure responses
   - Remove `<thinking>` tags from AI responses
   - Extract citations (url, domain, title)
   - Structure into analysis sections

4. **Assemble Response** (<0.01s): Combine all sections
   - Add metadata (timing, tokens, model)
   - Store in DynamoDB

**Analysis Sections**:
- **Business Profile**: Revenue models, core activities, products (500-800 chars, 3 citations)
- **Hiring Intelligence**: Job postings, recruitment trends (300-500 chars, 1 citation)
- **Technology Adoption**: Cloud platforms, AI/ML tools, digital initiatives (400-600 chars, 2 citations)

**Key Endpoints**:
- `GET /research/?company_name={name}&country={country}&accountId={id}` - Generate fresh research (30-40s)
- `GET /research/{accountId}` - Retrieve cached research (1-2s)
- `GET /health` - Health check

**Performance**:
- Fresh generation: 30-40 seconds
- Cached retrieval: 1-2 seconds
- Web grounding: Real-time search during generation

---

### 4. Consolidated API (Port 5004)

**Purpose**: Unified orchestration service aggregating data from account-api, news-api, and research-api

**Technology Stack**:
- Flask 3.x
- Python 3.8+
- AWS SDK (boto3)
- Concurrent execution (ThreadPoolExecutor)

**AWS Services Used**:

1. **AWS DynamoDB**:
   - Table: `ConsolidatedInfo`
   - Partition Key: `accountId` (string)
   - Purpose: Cache consolidated responses
   - TTL: 24 hours (configurable via `CACHE_TTL_HOURS`)
   - Attributes: accountId, data (nested), metadata, timestamp, ttl

**Two-Tier Caching Strategy**:

**Tier 1 - Consolidated Cache** (DynamoDB):
- Stores final aggregated response
- 24-hour freshness window
- Fast retrieval: <500ms

**Tier 2 - Individual API Caches**:
- News API cache (DynamoDB - News table)
- Research API cache (DynamoDB - CompanyOverview table)
- Account API cache (SQLite database)

**Processing Modes**:

**Mode 1: Cached Retrieval** (`GET /consolidated/{id}`):
1. Check ConsolidatedInfo DynamoDB table
2. If fresh (< 24h) → return immediately (<500ms)
3. If stale/missing:
   - Parallel calls to cached endpoints (8s timeout each):
     - `GET /account/{id}` (SQLite)
     - `GET /news/{id}` (DynamoDB)
     - `GET /research/{id}` (DynamoDB)
   - Returns 404 if ANY data missing (no partial responses)
   - Store in DynamoDB if all data available
   - Response time: 1-3 seconds

**Mode 2: Force Refresh** (`GET /consolidated/generate?accountId={id}`):
1. Get account data from account-api (8s timeout)
2. Extract company_name from accountName field
3. Extract country from territory field (e.g., "ASEAN-SG" → "Singapore")
4. Parallel generation calls:
   - `GET /news/research` (90s timeout) - generates fresh from NewsAPI.ai + Bedrock
   - `GET /research/` (300s timeout) - generates fresh from Bedrock Nova Premier
5. Assemble response (includes partial data if some services fail)
6. Store in DynamoDB (overwrites existing cache)
7. Response time: 90-300 seconds

**Key Endpoints**:
- `GET /consolidated/{accountId}` - Fast cached retrieval (<500ms cached, 1-3s miss)
- `GET /consolidated/generate?accountId={id}` - Force complete refresh (90-300s)
- `GET /health` - Health check with dependency status

**Data Completeness Tracking**:
```json
{
  "data_completeness": {
    "account_data": true,
    "news_data": true,
    "research_data": false,
    "overall_score": 0.67,
    "sources_successful": 2,
    "sources_attempted": 3
  }
}
```

**Optimization Features**:
- Redundancy stripping: Removes duplicate accountId fields from nested objects
- Parallel execution: News and research calls run simultaneously
- Graceful degradation: Returns partial data on force refresh
- Timeout management: Different timeouts for cached vs generation endpoints

**Performance**:
- Cached retrieval: <500ms (DynamoDB hit), 1-3s (cache miss)
- Force refresh: 90-300 seconds (fresh generation from external sources)
- Concurrent requests: 10+ supported

---

### 5. AI Analysis API (Port 5005)

**Purpose**: Transform consolidated data into structured business intelligence using AWS Bedrock AI models

**Technology Stack**:
- Flask 3.x
- Python 3.8+
- AWS SDK (boto3)
- Concurrent execution (ThreadPoolExecutor)

**AWS Services Used**:

1. **AWS Bedrock** (Two Models):
   
   **Model 1: Claude Haiku** (`us.anthropic.claude-haiku-4-5-20251001-v1:0`):
   - Purpose: Consolidated analysis (data transformation)
   - Max tokens: 12,000
   - Processing time: ~30 seconds
   - Use case: Fast, cost-effective JSON formatting
   - Prompt template: `consolidated_info_prompt.txt` (~18KB)
   
   **Model 2: Claude Sonnet** (`us.anthropic.claude-sonnet-4-5-20250929-v1:0`):
   - Purpose: Propensity scoring (complex reasoning)
   - Max tokens: 5,000
   - Processing time: ~15 seconds
   - Use case: Advanced reasoning, pattern recognition
   - Prompt template: `propensity_score_prompt.txt` (~5KB)

2. **AWS DynamoDB** (Three Tables):
   
   **Table 1: AIConsolidatedInfo**:
   - Partition Key: `accountId`
   - Purpose: Store consolidated analysis results
   - Content: Structured business intelligence (knowTheCustomer, pursueStrategy)
   
   **Table 2: AIPropensityScore**:
   - Partition Key: `accountId`
   - Purpose: Store propensity scoring results
   - Content: Overall score + factor breakdown
   
   **Table 3: AccountResearchData**:
   - Partition Key: `accountId`
   - Purpose: Store combined results (all analyses + metadata)
   - Content: Complete analysis package for fast retrieval

**Processing Pipeline** (45-60 seconds total):

1. **Data Retrieval** (1-2s):
   - Fetch consolidated data from Consolidated API (port 5004)
   - Extract account information

2. **Account Extraction** (<1s):
   - Parse account details from consolidated data
   - Prepare for AI analysis

3. **Parallel AI Analysis** (40-55s):
   
   **Analysis 1: Consolidated Analysis** (Claude Haiku, ~30s):
   - Input: Consolidated data + comprehensive prompt template
   - Output: Structured business intelligence
   - Sections:
     - knowTheCustomer: Company overview, stakeholders, initiatives, technology, pain points, engagement history
     - pursueStrategy: Who/what/how to pursue, executive summary, next steps
   
   **Analysis 2: Propensity Scoring** (Claude Sonnet, ~15s):
   - Input: Consolidated data + propensity scoring prompt
   - Output: Multi-factor propensity score
   - Factors:
     - AWS Usage Patterns (30% weight)
     - Engagement Signals (30% weight)
     - Technology Readiness (20% weight)
     - Market Momentum (20% weight)
   - Overall score: 0-100

4. **Storage** (1-2s):
   - Store in AIConsolidatedInfo table
   - Store in AIPropensityScore table
   - Store combined results in AccountResearchData table

5. **Response Assembly** (<1s):
   - Combine all results into unified response
   - Add metadata (completion rate, timestamps)

**Key Endpoints**:
- `GET /analyze/{accountId}` - Generate fresh AI analysis (45-60s)
- `GET /results/{accountId}` - Retrieve stored analysis (<500ms)
- `GET /health` - Health check

**Analysis Output Structure**:

**Consolidated Analysis**:
- Company overview (profile, locations, financial health)
- Key stakeholders (name, designation, contact info)
- Business initiatives (priority, timeline)
- Technology overview (infrastructure, cloud adoption)
- Pain points (description, impact, urgency)
- Engagement history (opportunities, relationship health)
- Pursue strategy (who/what/how, next steps)

**Propensity Score**:
- Overall score (0-100)
- Factor breakdown with weights
- Detailed explanation
- Calculation timestamp

**Performance**:
- Fresh analysis: 45-60 seconds
- Cached retrieval: <500ms
- Parallel processing: Both AI models run simultaneously
- Concurrent requests: 5+ supported

---

## AWS Services Summary

### DynamoDB Tables

| Table Name | Service | Partition Key | Purpose | TTL |
|------------|---------|---------------|---------|-----|
| `News` | News API | accountId | Cache news insights | None |
| `CompanyOverview` | Research API | accountId | Cache company research | None |
| `ConsolidatedInfo` | Consolidated API | accountId | Cache consolidated data | 24h |
| `AIConsolidatedInfo` | AI Analysis API | accountId | Store consolidated analysis | None |
| `AIPropensityScore` | AI Analysis API | accountId | Store propensity scores | None |
| `AccountResearchData` | AI Analysis API | accountId | Store combined AI results | None |

### Bedrock Models

| Model | Service | Purpose | Token Limit | Processing Time |
|-------|---------|---------|-------------|-----------------|
| Claude 3.5 Sonnet | News API | News summary generation | 4096 | 7-10s |
| Claude Haiku | News API | Query optimization | 2048 | 4-5s |
| Nova Premier | Research API | Company research with web grounding | 2400-1800 | 30-40s |
| Claude Haiku | AI Analysis API | Consolidated analysis | 12000 | ~30s |
| Claude Sonnet | AI Analysis API | Propensity scoring | 5000 | ~15s |

### External APIs

| API | Service | Purpose | Rate Limits |
|-----|---------|---------|-------------|
| NewsAPI.ai | News API | Article retrieval | Per API key |

---

## Data Flow Diagrams

### Complete User Journey

```
User Request (Frontend)
         ↓
    [Choose Path]
         ↓
    ┌────┴────┐
    │         │
    ▼         ▼
Fast Path   Deep Path
(Cached)    (Fresh)
    │         │
    ▼         ▼
Consolidated  Consolidated
API (cached)  API (generate)
    │         │
    ↓         ↓
DynamoDB     Account API
Cache        (SQLite)
    │         │
    │         ▼
    │    Extract company
    │    name & country
    │         │
    │         ▼
    │    Parallel Calls:
    │    ├─ News API
    │    │  (NewsAPI.ai +
    │    │   Bedrock Claude)
    │    │
    │    └─ Research API
    │       (Bedrock Nova
    │        Premier)
    │         │
    │         ▼
    │    Store in
    │    DynamoDB
    │         │
    └─────────┴─────────┐
                        ▼
                   AI Analysis API
                        │
                        ▼
                   Parallel AI:
                   ├─ Haiku
                   │  (Business Intel)
                   │
                   └─ Sonnet
                      (Propensity)
                        │
                        ▼
                   Store in 3
                   DynamoDB Tables
                        │
                        ▼
                   Return to
                   Frontend
```

### Caching Strategy

```
Request Flow:

1. Frontend → Consolidated API
              ↓
2. Check ConsolidatedInfo (DynamoDB)
   ├─ Hit (< 24h) → Return immediately (<500ms)
   └─ Miss → Continue
              ↓
3. Parallel calls to individual caches:
   ├─ Account API (SQLite) - <100ms
   ├─ News API (DynamoDB) - 1-2s
   └─ Research API (DynamoDB) - 1-2s
              ↓
4. Store in ConsolidatedInfo
              ↓
5. Return to Frontend (1-3s total)

Force Refresh Flow:

1. Frontend → Consolidated API (generate)
              ↓
2. Get Account Data (SQLite)
              ↓
3. Extract company_name & country
              ↓
4. Parallel generation:
   ├─ News API → NewsAPI.ai + Bedrock (15-20s)
   └─ Research API → Bedrock Nova (30-40s)
              ↓
5. Store in ConsolidatedInfo (overwrites cache)
              ↓
6. Return to Frontend (90-300s total)
```

---

## Performance Characteristics

### Response Time Summary

| Endpoint | Cache Hit | Cache Miss | Fresh Generation |
|----------|-----------|------------|------------------|
| Account API | N/A | <100ms | N/A |
| News API | 1-2s | N/A | 15-20s |
| Research API | 1-2s | N/A | 30-40s |
| Consolidated API | <500ms | 1-3s | 90-300s |
| AI Analysis API | <500ms | N/A | 45-60s |

### Timeout Configuration

| Service | Cached Endpoint | Generation Endpoint |
|---------|----------------|---------------------|
| Account API | 8s | N/A |
| News API | 8s | 90s |
| Research API | 8s | 300s |
| Consolidated API | 8s (per service) | 90s (news), 300s (research) |
| AI Analysis API | 8s (consolidated) | 300s (Bedrock) |

### Concurrent Request Capacity

| Service | Concurrent Requests | Bottleneck |
|---------|-------------------|------------|
| Account API | 50+ | SQLite read locks |
| News API | 10+ | NewsAPI.ai rate limits |
| Research API | 10+ | Bedrock quotas |
| Consolidated API | 10+ | Downstream services |
| AI Analysis API | 5+ | Bedrock quotas |

---

## Security & Authentication

### AWS Credentials

**Configuration Methods**:
1. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
2. AWS credentials file (`~/.aws/credentials`)
3. IAM role (recommended for production)

**Required Permissions**:

**DynamoDB**:
```json
{
  "Effect": "Allow",
  "Action": [
    "dynamodb:GetItem",
    "dynamodb:PutItem",
    "dynamodb:Query",
    "dynamodb:Scan"
  ],
  "Resource": [
    "arn:aws:dynamodb:*:*:table/News",
    "arn:aws:dynamodb:*:*:table/CompanyOverview",
    "arn:aws:dynamodb:*:*:table/ConsolidatedInfo",
    "arn:aws:dynamodb:*:*:table/AIConsolidatedInfo",
    "arn:aws:dynamodb:*:*:table/AIPropensityScore",
    "arn:aws:dynamodb:*:*:table/AccountResearchData"
  ]
}
```

**Bedrock**:
```json
{
  "Effect": "Allow",
  "Action": [
    "bedrock:InvokeModel",
    "bedrock:InvokeTool",
    "bedrock:ListFoundationModels"
  ],
  "Resource": [
    "arn:aws:bedrock:*::foundation-model/anthropic.claude-*",
    "arn:aws:bedrock:*::foundation-model/us.amazon.nova-*"
  ]
}
```

### API Security

- No authentication currently implemented (internal tool)
- CORS enabled for frontend access
- Input validation using Pydantic models
- Environment-based configuration (no hardcoded credentials)
- Bearer token authentication for Bedrock (company-research-api)

---

## Deployment Architecture

### Service Management

**Start/Stop Scripts**:
- `start_services.sh` - Starts all 5 services in order
- `stop_services.sh` - Stops all services gracefully

**Service Startup Order**:
1. Account API (port 5001) - No dependencies
2. News API (port 5002) - Requires AWS credentials
3. Company Research API (port 5003) - Requires AWS credentials
4. Consolidated API (port 5004) - Requires all above services
5. AI Analysis API (port 5005) - Requires Consolidated API

**Health Monitoring**:
- Each service has `/health` endpoint
- Consolidated API checks all dependencies
- AI Analysis API checks Consolidated API + AWS services

### Environment Configuration

**Account API**:
- No environment variables required
- SQLite database path: `source_data/sfdc.db`

**News API**:
```bash
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
NEWSAPI_KEY=xxx
DYNAMODB_TABLE_NAME=News
NEWS_API_PORT=5002
```

**Company Research API**:
```bash
AWS_REGION=us-east-1
AWS_BEARER_TOKEN_BEDROCK=xxx
BEDROCK_MODEL_ID=us.amazon.nova-premier-v1:0
DYNAMODB_TABLE_NAME=CompanyOverview
API_PORT=5003
```

**Consolidated API**:
```bash
ACCOUNT_API_URL=http://localhost:5001
NEWS_API_URL=http://localhost:5002
RESEARCH_API_URL=http://localhost:5003
AWS_REGION=us-east-1
DYNAMODB_TABLE_NAME=ConsolidatedInfo
CACHE_TTL_HOURS=24
CONSOLIDATED_API_PORT=5004
```

**AI Analysis API**:
```bash
CONSOLIDATED_API_URL=http://localhost:5004
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
AI_CONSOLIDATED_TABLE=AIConsolidatedInfo
AI_PROPENSITY_TABLE=AIPropensityScore
ACCOUNT_RESEARCH_TABLE=AccountResearchData
BEDROCK_MODEL_ID=us.anthropic.claude-sonnet-4-5-20250929-v1:0
BEDROCK_HAIKU_MODEL_ID=us.anthropic.claude-haiku-4-5-20251001-v1:0
AI_ANALYSIS_API_PORT=5005
```

---

## Cost Optimization

### AWS Service Costs

**DynamoDB**:
- On-demand pricing: $1.25 per million write requests, $0.25 per million read requests
- Storage: $0.25 per GB-month
- Estimated monthly cost: $10-50 (depending on usage)

**Bedrock**:
- Claude 3.5 Sonnet: $3 per million input tokens, $15 per million output tokens
- Claude Haiku: $0.25 per million input tokens, $1.25 per million output tokens
- Nova Premier: $2 per million input tokens, $8 per million output tokens
- Estimated monthly cost: $50-200 (depending on usage)

**Total AWS Monthly Cost**: $60-250

### Optimization Strategies

1. **Caching**: 24-hour cache reduces Bedrock calls by ~95%
2. **Model Selection**: Haiku for speed, Sonnet for reasoning
3. **Parallel Processing**: Reduces total processing time
4. **DynamoDB On-Demand**: Pay only for actual usage
5. **Token Limits**: Constrain output to reduce costs

---

## Monitoring & Observability

### Key Metrics

**Service Health**:
- Uptime percentage
- Response time percentiles (p50, p95, p99)
- Error rates by endpoint
- Dependency health status

**AWS Services**:
- DynamoDB read/write latencies
- Bedrock invocation success rates
- Token usage per model
- API throttling events

**Business Metrics**:
- Cache hit rates
- Data completeness scores
- Analysis success rates
- User request patterns

### Logging

**Log Locations**:
- Account API: Console only
- News API: `logs/news-api.log`
- Research API: `logs/company-research-api.log`
- Consolidated API: Console + file (configurable)
- AI Analysis API: Console + file (configurable)

**Log Levels**: INFO, WARNING, ERROR

---

## Disaster Recovery

### Backup Strategy

**SQLite Database** (Account API):
```bash
cp database/sfdc.db database/sfdc_backup_$(date +%Y%m%d).db
```

**DynamoDB Tables**:
- Enable point-in-time recovery (PITR)
- On-demand backups before major changes
- Cross-region replication (optional)

### Recovery Procedures

**Service Failure**:
1. Check health endpoint
2. Review service logs
3. Restart individual service
4. Verify dependencies

**Data Corruption**:
1. Stop affected service
2. Restore from backup
3. Verify data integrity
4. Restart service

**AWS Service Outage**:
1. Monitor AWS status dashboard
2. Enable graceful degradation
3. Return partial data where possible
4. Queue requests for retry

---

## Future Enhancements

### Planned Features

1. **Authentication & Authorization**:
   - API key authentication
   - Role-based access control
   - Rate limiting per user

2. **Advanced Caching**:
   - Redis for distributed caching
   - Cache warming strategies
   - Intelligent cache invalidation

3. **Scalability**:
   - Kubernetes deployment
   - Auto-scaling based on load
   - Load balancing

4. **Monitoring**:
   - CloudWatch integration
   - Custom dashboards
   - Alerting and notifications

5. **Data Pipeline**:
   - Automated data refresh
   - Incremental updates
   - Data quality checks

---

## Appendix

### Port Assignments

| Service | Port | Protocol |
|---------|------|----------|
| Frontend | 3000 | HTTP |
| Account API | 5001 | HTTP |
| News API | 5002 | HTTP |
| Research API | 5003 | HTTP |
| Consolidated API | 5004 | HTTP |
| AI Analysis API | 5005 | HTTP |

### Technology Stack Summary

**Backend**:
- Python 3.8-3.9+
- Flask 2.3-3.x
- boto3 (AWS SDK)
- Pydantic (validation)
- SQLite (local database)

**AWS Services**:
- DynamoDB (6 tables)
- Bedrock (5 models)
- IAM (permissions)

**External APIs**:
- NewsAPI.ai

**Frontend**:
- Next.js
- React
- TypeScript

### Document Version

- Version: 1.0
- Last Updated: December 2024
- Author: RubyChan v2 Team

