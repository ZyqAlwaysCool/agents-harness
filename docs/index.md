# Docs Index

This repository uses layered documentation for agent-first work.

## Reading Order

1. `AGENTS.md`
2. `docs/index.md`
3. `configs/agent-harness.yaml`
4. `docs/manifest.yaml`
5. the selected pack entry document under `standards/`
6. relevant files in `docs/current/`

## Control Model

The repository control model has three layers:

- `Base`: repository-level control rules that stay stable across projects. Base defines startup order, docs layering, script entrypoints, verification expectations, and hard repository boundaries.
- `Pack`: stack-specific implementation guidance. A pack decides how code inside `app/` should be organized for a chosen stack.
- `Policy`: project-level switches and governance settings defined in `configs/agent-harness.yaml`.

The current default pack is `python-fastapi`.
The current pack entry document is `standards/python-fastapi/README.md`.

## Layers

- `docs/current/`: current truth
- `docs/adr/`: decision records
- `docs/worklog/`: active discussion and investigation notes
- `docs/archive/`: retired content

## Current Truth Areas

- `docs/current/product/`
- `docs/current/architecture/`
- `docs/current/domain/`
- `docs/current/contracts/`
- `docs/current/runbooks/`

For the harness control model itself, see `docs/current/architecture/harness-model.md`.

## Default Verification

- `./scripts/lint`
- `./scripts/test`
- `./scripts/check`

## Default Skill Registry

See `standards/skills/manifest.yaml`.
