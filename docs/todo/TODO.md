# Documentation Audit TODO — Hermes Agent

## Phase 1: Move docs from root into /docs
- [x] 1. Move `apps/desktop/DESIGN.md` → `docs/design/02-desktop-design-system.md`
- [x] 2. Move `apps/desktop/AGENTS.md` → `docs/governance/08-desktop-engineering-guide.md`
- [x] 3. Move `optional-skills/DESCRIPTION.md` → `docs/skills/02-optional-skills.md`
- [x] 4. Delete `gateway/platforms/ADDING_A_PLATFORM.md` (redundant redirect)
- [x] 5. Update cross-links in moved files and root README

## Phase 2: Fix H1 title casing (lower-case per rule #10)
- [x] 6. Fix H1 casing in all non-README docs under /docs

## Phase 3: Fix numbering mismatch in architecture/
- [x] 7. Fix 05-cron-scheduler.md: `# 06.` → `# 05.`
- [x] 8. Fix 06-memory-state-store.md: `# 07.` → `# 06.`
- [x] 9. Fix 07-subagent-delegation.md: `# 08.` → `# 07.`

## Phase 4: Rewrite templates to match document type
- [x] 10. Rewrite `docs/api/template.md` — Contract/Reference template
- [x] 11. Rewrite `docs/architecture/template.md` — Reference/Architecture template
- [x] 12. Rewrite `docs/design/template.md` — Design Proposal template
- [x] 13. Rewrite `docs/developer-guide/template.md` — Developer Guide template
- [x] 14. Rewrite `docs/gateway/template.md` — Gateway reference template
- [x] 15. Rewrite `docs/governance/template.md` — Governance/Policy template
- [x] 16. Rewrite `docs/integration/template.md` — Integration guide template
- [x] 17. Rewrite `docs/kanban/template.md` — Kanban system template
- [x] 18. Rewrite `docs/middleware/template.md` — Middleware contract template
- [x] 19. Rewrite `docs/observability/template.md` — Observability template
- [x] 20. Rewrite `docs/operations/template.md` — Operations guide template
- [x] 21. Rewrite `docs/plugins/template.md` — Plugin guide template
- [x] 22. Rewrite `docs/rfcs/template.md` — RFC template
- [x] 23. Rewrite `docs/security/template.md` — Security guide template
- [x] 24. Rewrite `docs/setup/template.md` — Setup guide template
- [x] 25. Rewrite `docs/skills/template.md` — Skills guide template
- [x] 26. Rewrite `docs/tools/template.md` — Tools reference template
- [x] 27. Rewrite `docs/troubleshooting/template.md` — Troubleshooting template
- [x] 28. Rewrite `docs/user-guide/template.md` — User guide template

## Phase 5: Improve docs/README.md
- [x] 29. Add badges (license, stars, discord, website) to docs/README.md
- [x] 30. Add ADR index table to docs/adr/README.md

## Phase 6: Improve sub-folder READMEs
- [x] 31. Expand short READMEs: design, kanban, plugins, skills, troubleshooting

## Phase 7: Update root README.md
- [x] 32. Add placeholder for benchmark donut chart section
- [x] 33. Update any broken internal links to moved files

## Phase 8: Final validation
- [x] 34. Verify all file names are lowercase kebab-case
- [x] 35. Verify all directories have README.md + template.md
- [x] 36. Verify all documents have numbered prefix in filename matching H1
- [x] 37. Final check — no "report"/"отчёт" in titles
