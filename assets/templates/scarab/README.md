# Scarab-ICM Workspace

This subfolder contains a reusable software delivery management structure based on ICM.

## Pipelines

- `bugs/` - software defect tracking
- `stories/` - feature and implementation story tracking
- `scripts/` - workflow support scripts

## How to route

1. Read `CONTEXT.md` in this folder.
2. Read the relevant pipeline `WORKFLOW.md`.
3. Read the target bug or story `description.md`.

## Important rule

Use `scripts/move-story.py` for all bug and story stage transitions. Do not move folders manually.
