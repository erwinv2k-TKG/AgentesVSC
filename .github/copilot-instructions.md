# Autonomous Development Mode (VS Code)

This workspace runs in autonomous mode by default.

## Core behavior

1. Execute end-to-end when feasible: analyze, plan, implement, validate, and summarize.
2. Do not stop at analysis-only unless the user explicitly asks for brainstorming only.
3. Ask for confirmation only when an operation is destructive, risky, or ambiguous.
4. Prefer direct action over long proposals.

## Delivery workflow

1. Clarify objective and constraints quickly.
2. For medium/large work, produce a concise task plan.
3. Implement incrementally with minimal, focused edits.
4. Run relevant checks (tests/lint/build) when available.
5. Report findings first: risks, regressions, and remaining gaps.

## Quality and safety

- Avoid unrelated refactors.
- Reuse existing patterns before creating new structures.
- If tests cannot be executed, state it explicitly.
- Never fabricate validation results.

## Repository convention

- Keep imported packs as reference.
- Put VS Code specific derivations in packs/vscode-local-overrides/.
- Register local operational changes in packs/vscode-local-overrides/docs/CHANGELOG_LOCAL.md.
