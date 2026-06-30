# AI Agent Identity Governance System

A Python-based IAM system that governs access for AI agents (Non-Human Identities) — applying enterprise IAM principles like RBAC, audit logging, and human-in-the-loop approval to autonomous AI agents.

## Problem
As companies deploy AI agents (Copilots, AutoGPTs, LangChain bots), there's no standard way to govern what these agents can access. This project treats AI agents like users — giving each one an identity, role-based permissions, and an audit trail.

## Features
- **Agent Registry** — Each AI agent gets a unique identity with a role and owner team
- **RBAC Engine** — Role-based permission evaluation (read_only, writer, admin)
- **Human-in-the-Loop Approval** — High-risk actions (delete, export) require manager approval, even for admin-level agents
- **Immutable Audit Log** — Every access decision is logged with agent ID, action, outcome, and timestamp

## Tech Stack
Python

## How It Works
1. Agent requests an action (e.g., "delete")
2. RBAC engine checks if the role allows it
3. If allowed but high-risk → request goes into the Pending Approval queue
4. Manager approves or rejects the request
5. Every decision is written to the audit log

## Files
- `rbac.py` — Permission engine
- `agent.py` — Agent registry and access logic
- `audit.py` — Audit logging system
- `approval.py` — Human-in-the-loop approval workflow

## Run It
\`\`\`
python agent.py
\`\`\`

## Author
Abhinav Kumar Mittal
