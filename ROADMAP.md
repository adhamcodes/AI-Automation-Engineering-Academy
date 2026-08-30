# AI Automation Engineering Roadmap — v1.0

**Target:** reliable automation engineer who can turn business processes into operated systems. **Pacing:** designed for ~2–3 focused hours/day; commercial tests can begin before the academy ends.

| Phase | Typical effort | Capability outcome | Gate |
|---|---:|---|---|
| 0 Automation Thinking | ~1 week | map processes, bottlenecks, decisions, handoffs and automation risks | Process Mapper |
| 1 HTTP, APIs & Webhooks | ~2 weeks | integrate unfamiliar APIs with auth, pagination, rate/error handling | Integration Fundamentals |
| 2 Workflow Engineering / n8n | 2–3 weeks | build modular workflows with triggers, branching, credentials, retries and debugging | **Useful Workflow Builder** |
| 3 Python Automation | 3–4 weeks | create custom clients, CLI/file pipelines and small FastAPI services | Code-Assisted Builder |
| 4 Data & Persistent Systems | 2–3 weeks | SQL/state/idempotency/queues/concurrency for reliable repeat execution | **Reliable Integration Builder** |
| 5 JavaScript for Automation | 1–2 weeks | write focused JS/async/custom workflow logic | Custom Logic Ready |
| 6 AI-Powered Automation | 3–4 weeks | add LLM classification/extraction/RAG/tool use with evals and human review | **Monetization Ready** |
| 7 Business Automation Systems | 3–4 weeks | translate messy operational problems into client-grade architectures | **Client-Grade Builder** |
| 8 Browser & Document Automation | 2–4 weeks | automate browser/file/document work safely when APIs are insufficient | Multi-Channel Builder |
| 9 Agentic Automation | 3–5 weeks | bounded agents with tools, state, approvals, recovery and evals | Agentic Automation Ready |
| 10 Production Reliability & Security | 3–4 weeks | deploy/operate systems with Docker, logs, monitoring, backups and security | **Automation Engineer** |
| 11 Commercial Engineering | continuous later | discover, scope, demo, price, deliver, hand over and support work | Commercial Delivery Ready |
| 12 Automation Products | open-ended | extract repeated solutions into reusable systems/products | Product/System Builder |

## Architecture rule
Prefer **deterministic logic when possible → AI when ambiguity requires it → human approval when consequence or uncertainty demands it**.

## Phase progression

### 0. Automation Thinking
Learn process mapping, automation opportunity filtering, failure/handoff analysis and precise workflow specifications. The first skill is understanding work—not dragging nodes.

### 1. HTTP, APIs & Webhooks
Client/server, HTTP methods/headers/status codes, JSON, REST documentation, API keys/bearer/OAuth concepts, pagination, rate limits, retries/backoff, webhooks vs polling, idempotency, error handling and Postman exploration.

### 2. Workflow Engineering / n8n
Execution data, expressions, mapping, branching, batching/loops/waits, triggers/schedules/webhooks, credentials/configuration, subworkflows, error/retry/recovery patterns, debugging, documentation and monitoring. Assessment: integrate an unfamiliar practice API without a step-by-step tutorial.

### 3. Python Automation
HTTP clients, JSON/CSV/filesystem, configuration/env vars, CLI tools, logging, retry/client design, validation/transformation, FastAPI services, background-work boundaries, testing, and n8n↔Python hybrid architecture.

### 4. Data & Persistent Systems
Relational modelling, SQL CRUD/joins/aggregates, transactions/indexes, PostgreSQL, workflow state machines, deduplication/idempotency, queues/workers, concurrency/race conditions. Project: restart-safe, database-backed automation.

### 5. JavaScript for Automation Engineers
Objects/arrays/functions/modules, map/filter/reduce, async/await/promises, fetch/HTTP, errors/validation and n8n Code-node logic. No frontend detour.

### 6. AI-Powered Automation
When AI is appropriate, model APIs, instructions, structured outputs, classification/routing, extraction/document processing, summarization, embeddings/RAG, tool calling, evaluation, exception queues/human review, cost/latency/privacy. This is the first serious monetization gate—not an income promise.

### 7. Business Automation Systems
CRM/leads, onboarding, support, approvals, reporting, synchronization, admin/document workflows, requirements discovery, scope and acceptance criteria. Capstone: convert a vague business complaint into a documented system.

### 8. Browser & Document Automation
API-first decision, Playwright, locators, sessions/auth, uploads/downloads, scraping boundaries, spreadsheets/PDFs/docs, OCR/email-attachment awareness. Use browser automation only when an API is unavailable or inappropriate.

### 9. Agentic Automation
Workflow vs agent/hybrid, tools, state, approvals, memory, MCP, deterministic guardrails, retries/recovery, trajectory evaluation and n8n agent patterns. Avoid autonomous complexity without measurable benefit.

### 10. Production Reliability & Security
Docker/Compose, Linux/VPS fundamentals, TLS/reverse-proxy awareness, secrets, logging/monitoring, n8n operation, scaling/queue concepts, backups/disaster recovery, API/webhook security, AI/agent security, testing/releases and incident response. Boss fight: survive injected failures.

### 11. Commercial Engineering
Problem discovery, choosing problem categories, discovery conversations, scoping/acceptance criteria, demos, pricing models, platform licensing/ownership, security responsibility, documentation/handover, support boundaries, case studies, distribution/outreach and applications.

### 12. Automation Products
Learn when repetition justifies productization: reusable templates/components, custom connectors/nodes, vertical systems, platform/licensing alternatives, multi-tenant awareness, support/operations and an advanced product capstone.

## Commercial progression
Do not wait for “graduation.” After the Monetization Ready gate, begin low-risk market tests: publish proof, apply for relevant roles/contracts, help agencies, talk to businesses, or package a narrowly scoped service. Keep learning and improving reliability in parallel.
