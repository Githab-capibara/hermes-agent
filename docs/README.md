# Hermes Agent Documentation

<p align="center">
  <a href="https://github.com/NousResearch/hermes-agent"><img src="https://img.shields.io/github/stars/NousResearch/hermes-agent?style=for-the-badge&logo=github&color=FFD700" alt="GitHub stars"></a>
  <a href="https://github.com/NousResearch/hermes-agent/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://discord.gg/NousResearch"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://hermes-agent.nousresearch.com"><img src="https://img.shields.io/badge/website-hermes--agent.nousresearch.com-FFD700?style=for-the-badge" alt="Website"></a>
</p>

## 🎯 Master Index

Welcome to the **Hermes Agent** documentation hub. This index provides quick access to all documentation across the project — from architecture decisions to user guides, governance policies to API contracts.

### Quick Navigation

| Section | For | Start Here |
|---------|-----|------------|
| 🚀 **Start here** | New users | [Quickstart](user-guide/README.md) |
| 📁 **Directory map** | Everyone | See all 20 documentation folders |
| 🔗 **Key entry points** | By role | Find your path below |
| 📜 **Governance** | Contributors | [Contributing guide](governance/02-contributing.md) |

---

## 🚀 Start here

| Guide | Purpose |
|-------|---------|
| [Quickstart](user-guide/README.md) | First engagement in ~5 minutes |
| [Getting Started](setup/README.md) | Install and initial configuration |
| [Contributing](governance/02-contributing.md) | How to contribute to Hermes |
| [Security Policy](governance/03-security-policy.md) | Vulnerability reporting and trust model |

## Directory map

| Directory | Description |
|-----------|-------------|
| [adr/](adr/) | Architecture Decision Records |
| [architecture/](architecture/) | Core system architecture |
| [api/](api/) | API contracts |
| [design/](design/) | Design proposals |
| [developer-guide/](developer-guide/) | Developer onboarding and standards |
| [gateway/](gateway/) | Gateway platforms and messaging |
| [governance/](governance/) | Project governance |
| [integration/](integration/) | Integration guides |
| [kanban/](kanban/) | Kanban system |
| [middleware/](middleware/) | Plugin middleware contract |
| [observability/](observability/) | Telemetry and monitoring |
| [operations/](operations/) | Operations and deployment |
| [plugins/](plugins/) | Plugin documentation |
| [rfcs/](rfcs/) | Request for Comments |
| [security/](security/) | Security guides |
| [setup/](setup/) | Setup guides |
| [skills/](skills/) | Skills documentation |
| [tools/](tools/) | Tools documentation |
| [troubleshooting/](troubleshooting/) | Troubleshooting guides |
| [user-guide/](user-guide/) | End-user guides |

## ADR Index

| # | Title | Status |
|---|---|---|
| [01](adr/01-plugin-manager-state-scoping.md) | Plugin manager state scoping by Hermes home | Accepted |

> Full index with lifecycle rules: [adr/README.md](adr/README.md)

## Key entry points

### For Contributors
→ [Development Guide](governance/01-agents-development-guide.md)
→ [Contributing](governance/02-contributing.md)
→ [Security Policy](governance/03-security-policy.md)

### For Architects
→ [ADR Index](adr/README.md)
→ [Session Lifecycle](architecture/01-session-lifecycle.md)
→ [Profile Routing](architecture/02-profile-routing.md)

### For Operators
→ [Network Egress Isolation](security/01-network-egress-isolation.md)
→ [Multi-Gateway Deployment](kanban/01-multi-gateway.md)
→ [Chronos Managed Cron](api/02-chronos-managed-cron-contract.md)

### For Plugin Authors
→ [Middleware Contract](middleware/README.md)
→ [Plugin Architecture Lessons](rfcs/01-plugin-architecture-lessons.md)

### For Newcomers (mechanisms)
→ [Gateway Overview](gateway/01-overview.md) · [Skills](skills/01-overview.md) · [Plugins](plugins/01-overview.md)
→ [Cron Scheduler](architecture/05-cron-scheduler.md) · [Memory & State Store](architecture/06-memory-state-store.md)
→ [Subagents & Delegation](architecture/07-subagent-delegation.md) · [MCP Integration](integration/02-mcp-integration.md)
→ [Terminal Backends](developer-guide/02-terminal-backends.md) · [Toolsets](tools/03-toolsets-distribution.md) · [TUI](user-guide/02-tui-overview.md)

## Component documentation

READMEs that live next to the code they describe (kept in place by convention):

| Component doc | Purpose |
|---------------|---------|
| [ui-tui/README.md](../ui-tui/README.md) | Terminal UI application |
| [web/README.md](../web/README.md) | Web dashboard |
| [apps/desktop/README.md](../apps/desktop/README.md) | Desktop app |
| [native/fts5_cjk/README.md](../native/fts5_cjk/README.md) | CJK tokenizer for FTS5 |
| [scripts/toolperf_abeval/README.md](../scripts/toolperf_abeval/README.md) | Toolperf harness runner |
| [tests/stress/README.md](../tests/stress/README.md) | Stress test suites |

## Governance

| Document | Description |
|----------|-------------|
| [Development Guide](governance/01-agents-development-guide.md) | Intent layer for contributors |
| [Contributing](governance/02-contributing.md) | Setup, code style, PR process |
| [Security Policy](governance/03-security-policy.md) | Trust model, vulnerability reporting |
| [Code of Conduct](governance/07-code-of-conduct.md) | Community standards |
