# Start Here — AI Automation Engineering Academy

Do not read the entire repository before beginning. Follow this sequence.

## 1. Read the operating rules (15–20 minutes)

Read:

- [How to Use This Academy](HOW-TO-USE.md)
- [Self-Study Operating System](SELF_STUDY_SYSTEM.md)
- [Parallel Study & Prerequisite Gates](PARALLEL_STUDY.md)
- [Roadmap](ROADMAP.md) — scan only
- [AI Assistance Policy](AI_ASSISTANCE_POLICY.md)

Keep [LAB_MAP.md](LAB_MAP.md) bookmarked. It maps every phase to its controlled executable practice environment.

## 2. Create your own workspace

Keep your workflows, code, notes, client simulations, assessment evidence, and progress outside the canonical curriculum repository. Copy [PROGRESS_TEMPLATE.md](PROGRESS_TEMPLATE.md) into your own private or public learning repo.

Suggested structure:

```text
my-automation-learning/
├── progress.md
├── workflows/
├── python/
├── projects/
├── assessments/
└── case-studies/
```

Never commit real credentials, API keys, client data, or private webhook secrets.

## 3. Begin Phase 0

Open **[00-automation-thinking/README.md](00-automation-thinking/README.md)**. Complete the diagnostic even if you already know n8n or another workflow tool. The first capability is understanding work well enough to automate it safely.

When a phase reaches its build/debug work, open the matching lab in **[LAB_MAP.md](LAB_MAP.md)**. Work on a copy in your own learning repository; do not turn this canonical curriculum into your answer repository.

## 4. Use this loop

**learn → predict → build → inspect → inject failure → recover → explain → prove**

If you get stuck, use the escalation order in [SELF_STUDY_SYSTEM.md](SELF_STUDY_SYSTEM.md) instead of opening random tutorials immediately.

For API/integration work, build from documentation rather than only following templates.

## 5. Respect the gates

A workflow that works once is not necessarily client-grade. Pass the phase assessment and executable evidence gate before advancing. Do not promise a commercial outcome until you can pass the corresponding reliability and delivery gate.

If a software-engineering prerequisite is missing, follow [PARALLEL_STUDY.md](PARALLEL_STUDY.md) and repair it instead of copying code you cannot explain.

## Core rule

A workflow that succeeds once is a demo. An automation that handles repeat runs, bad inputs, API failures, retries, state, logging, recovery, and handover is engineering.

**Begin:** [Phase 0 — Automation Thinking](00-automation-thinking/README.md)
