# AI Automation Engineering Academy

**Free • self-guided • build-first • commercially aware**

A complete learning path for turning messy real-world processes into **reliable automated systems** using APIs, workflow platforms, Python, databases, AI where appropriate, browser/document automation, agents, and production engineering.

The target is not “become an n8n user.” The target is an **automation engineer who can own the outcome**.

> **understand the process → design → build → break it → recover → operate → document → prove value**

## Start in 60 seconds

1. Open **[START-HERE.md](START-HERE.md)**.
2. Read the **[Self-Study Operating System](SELF_STUDY_SYSTEM.md)** once before Phase 0.
3. Begin with Automation Thinking even if you have used workflow tools before.
4. Use the matching executable challenge from **[LAB_MAP.md](LAB_MAP.md)** as you progress.
5. Keep your own workflows/code/progress outside the canonical curriculum repository; start from **[PROGRESS_TEMPLATE.md](PROGRESS_TEMPLATE.md)**.
6. Do not sell a capability you cannot pass at the corresponding commercial gate.

## Roadmap at a glance

| Phase | Outcome | Typical effort |
|---|---|---:|
| [0 — Automation Thinking](00-automation-thinking/README.md) | map work, bottlenecks, handoffs, risks | ~1 week |
| [1 — HTTP, APIs & Webhooks](01-http-apis-webhooks/README.md) | integrate unfamiliar APIs reliably | ~2 weeks |
| [2 — Workflow Engineering](02-workflow-engineering/README.md) | modular workflows, errors, debugging, monitoring | 2–3 weeks |
| [3 — Python Automation](03-python-automation/README.md) | custom clients, services, testing, n8n↔Python systems | 3–4 weeks |
| [4 — Data & Persistent Systems](04-data-persistent-systems/README.md) | SQL, state, idempotency, queues, concurrency | 2–3 weeks |
| [5 — JavaScript for Automation](05-javascript-automation/README.md) | focused JS/async/custom workflow logic | 1–2 weeks |
| [6 — AI-Powered Automation](06-ai-powered-automation/README.md) | structured AI, RAG, evals, human review | 3–4 weeks |
| [7 — Business Automation Systems](07-business-systems/README.md) | client-grade architectures from vague requirements | 3–4 weeks |
| [8 — Browser & Document Automation](08-browser-document-automation/README.md) | reliable browser/file/document pipelines | 2–4 weeks |
| [9 — Agentic Automation](09-agentic-automation/README.md) | bounded agents, tools, state, approvals, recovery | 3–5 weeks |
| [10 — Production Reliability & Security](10-production-reliability/README.md) | deploy, monitor, secure, back up, recover | 3–4 weeks |
| [11 — Commercial Engineering](11-commercial-engineering/README.md) | discover, scope, price, deliver, hand over, support | continuous later |
| [12 — Automation Products](12-automation-products/README.md) | turn repeated solutions into reusable systems | open-ended |

Full detail: **[ROADMAP.md](ROADMAP.md)** · curriculum map: **[CURRICULUM_MAP.md](CURRICULUM_MAP.md)** · executable labs: **[LAB_MAP.md](LAB_MAP.md)**

## The architecture rule

> **Deterministic logic when possible → AI when ambiguity requires it → human approval when consequence or uncertainty demands it.**

## What makes this an academy

The repository contains native lessons, curated resources, integration exercises, failure-injection/debugging work, realistic business projects, assessments, mastery gates, production/security material, commercial-readiness gates, and a controlled executable lab layer.

The labs include local API failure simulation, idempotency debugging, persistent-state design, AI evaluation, browser fixtures, bounded-agent policy checks, and an actual production fault injector. They are deliberately stable so the core course does not depend on random external websites.

## Quality gates

This repository validates its phase structure, local links, and executable lab smoke tests on both Linux and Windows through GitHub Actions.

Run the same checks locally:

```bash
python scripts/validate_academy.py
python scripts/run_smoke_tests.py
```

## Monetization philosophy

Commercial activity starts **before** the technical curriculum ends, but only after capability gates. The academy teaches problem discovery, scoping, demos, pricing, delivery boundaries, licensing/ownership, security responsibility, handover, support, case studies, and productization. It does **not** promise income on a calendar.

## Study with a friend

Use the same curriculum while keeping separate implementation/progress repositories. Build key exercises independently first, then review one another's architecture, failure handling, documentation, and alternative solutions.

## Platform independence

The academy uses n8n as a primary workflow platform because it is practical and current, but concepts come first. You should be able to transfer API, state, reliability, orchestration, and business-process skills to other platforms.

## License & contributions

Educational content is CC BY 4.0; code examples are MIT-licensed. See **[LICENSE.md](LICENSE.md)** and **[CONTRIBUTING.md](CONTRIBUTING.md)**.

> Start here: **[START-HERE.md](START-HERE.md)**
