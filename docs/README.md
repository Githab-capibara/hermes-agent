# Hermes Agent Documentation

> **The self-improving AI agent built by [Nous Research](https://nousresearch.com).**

<p align="center">
  <a href="https://hermes-agent.nousresearch.com/docs/"><img src="https://img.shields.io/badge/Docs-hermes--agent.nousresearch.com-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://discord.gg/NousResearch"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://github.com/NousResearch/hermes-agent/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://nousresearch.com"><img src="https://img.shields.io/badge/Built%20by-Nous%20Research-blueviolet?style=for-the-badge" alt="Built by Nous Research"></a>
</p>

---

## 🚀 Start Here

New to Hermes? Start here:

| Guide | Purpose |
|-------|---------|
| [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart) | Install → setup → first conversation in 2 minutes |
| [CLI Usage](../user-guide/cli) | Commands, keybindings, personalities, sessions |
| [Configuration](../user-guide/configuration) | Config file, providers, models, all options |
| [Contributing Guide](governance/02-contributing.md) | Development setup, PR process, code style |
| [Security Policy](governance/03-security-policy.md) | Trust model, vulnerability reporting |

---

## 📁 Directory Map

| Directory | Description |
|-----------|-------------|
| [adr/](adr/) | Architecture Decision Records — non-obvious architectural decisions |
| [architecture/](architecture/) | Core system architecture — sessions, profiles, streaming |
| [api/](api/) | API contracts — wire specs for external integrations |
| [design/](design/) | Design proposals — dashboard-native features |
| [governance/](governance/) | Project governance — contributing, security, development guide |
| [kanban/](kanban/) | Kanban system — multi-gateway deployment |
| [middleware/](middleware/) | Plugin middleware contract |
| [observability/](observability/) | Observer hooks — telemetry contract for plugins |
| [rfcs/](rfcs/) | Request for Comments — research spikes and proposals |
| [security/](security/) | Security guides — network isolation, SSL |
| [setup/](setup/) | Setup guides — Termux, platform-specific |

---

## 🔗 Key Entry Points

### For Contributors
→ [Development Guide](governance/01-agents-development-guide.md)
→ [Contributing](governance/02-contributing.md)
→ [Security Policy](governance/03-security-policy.md)

### For Architects
→ [ADR Index](adr/)
→ [Session Lifecycle](architecture/01-session-lifecycle.md)
→ [Profile Routing](architecture/02-profile-routing.md)

### For Operators
→ [Network Egress Isolation](security/01-network-egress-isolation.md)
→ [Multi-Gateway Deployment](kanban/01-multi-gateway.md)
→ [Chronos Managed Cron](api/02-chronos-managed-cron-contract.md)

### For Plugin Authors
→ [Observer Hooks](observability/)
→ [Middleware Contract](middleware/)
→ [Plugin Architecture Lessons](rfcs/01-plugin-architecture-lessons.md)

---

## 📜 Governance

| Document | Description |
|----------|-------------|
| [Development Guide](governance/01-agents-development-guide.md) | Intent layer for contributors and automated review |
| [Contributing](governance/02-contributing.md) | Setup, code style, PR process |
| [Security Policy](governance/03-security-policy.md) | Trust model, vulnerability reporting |
| [Code of Conduct](https://github.com/NousResearch/hermes-agent/blob/main/CODE_OF_CONDUCT.md) | Community standards |

---

## 📊 ADR Index

| # | Title | Status |
|---|-------|--------|
| [01](adr/01-plugin-manager-state-scoping.md) | Plugin manager state scoping by Hermes home | Accepted |

---

*Documentation lives at [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/).*
