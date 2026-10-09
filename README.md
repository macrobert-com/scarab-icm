# Scarab-ICM

Scarab-ICM is a reusable ICM-style scaffold for software delivery work.

It adds one subfolder inside an existing workspace and installs two sibling pipelines:

- `bugs/`
- `stories/`

Each pipeline contains staged folders, templates, and a workflow contract. The scaffold also includes `scripts/move-story.py`, which agents should use for all bug and story stage transitions.

## Skill contents

- `SKILL.md` - installation and operating behavior for the skill
- `assets/templates/workspace-root/` - starter routing files for workspace root
- `assets/templates/scarab/` - scaffold files for the Scarab umbrella and its two pipelines
- `references/` - supporting notes on shape, routing, and agent behavior

## Intended result in a user workspace

A Scarab installation adds a subfolder containing:

- `README.md`
- `CONTEXT.md`
- `bugs/`
- `stories/`
- `scripts/`

The workspace root should route into this structure through `AGENTS.md` or `CLAUDE.md`, with both pointing to the workspace-root `CONTEXT.md`.
