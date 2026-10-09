---
name: scarab-icm
description: Add a reusable ICM-style software delivery subfolder to an existing workspace, with sibling bugs and stories pipelines, workflow docs, templates, and the move-story.py transition script. Use when the user wants a portable bug/story management structure that an LLM can route through via AGENTS.md or CLAUDE.md, or wants agents to operate consistently inside that structure after it is installed.
---

# Scarab-ICM

Scarab-ICM is an umbrella ICM for software delivery work. It installs one subfolder inside an existing workspace and gives that subfolder two sibling pipelines:

- `bugs/`
- `stories/`

Each pipeline uses the same staged lifecycle:

- `01-inbox/`
- `02-processing/`
- `03-complete/`
- `_templates/`

Scarab-ICM does two jobs:

1. **Scaffold the structure** into a user-chosen location inside an existing workspace.
2. **Standardize agent behavior** once the structure exists, so new bugs and stories are created consistently and moved only through the supplied transition script.

## When to use this skill

Use Scarab-ICM when the user wants to:

- add a reusable bugs-and-stories management system to an existing software workspace
- install a generic workflow that is not tied to any one project or codebase
- make bug and story definitions legible to Codex, Claude Code, or similar harnesses through root routing files
- formalize how agents create, read, and move bug/story records over time

## Relationship to ICM Architect

Scarab-ICM follows the **umbrella over sibling pipelines** pattern described by `skills/icm-architect/`.

- The Scarab subfolder is the umbrella root.
- `bugs/` is one pipeline.
- `stories/` is one pipeline.
- The root workspace routing files point into the workspace `CONTEXT.md`, which in turn points to the Scarab subfolder map.

Read these references when shaping or installing the scaffold:

- `references/overview.md`
- `references/install-and-routing.md`
- `references/agent-behavior.md`

## Install behavior

When asked to set up Scarab-ICM in a workspace, do this:

1. **Confirm the target workspace and subfolder path.**
   - Scarab-ICM adds one subfolder inside an existing workspace.
   - Ask where the user wants that subfolder placed if the path is not already clear.

2. **Inspect the workspace root before writing.**
   - Check whether `AGENTS.md`, `CLAUDE.md`, and `CONTEXT.md` already exist at the workspace root.
   - Never overwrite them blindly.

3. **Install the Scarab subfolder.**
   - Copy the structure from `assets/templates/scarab/` into the chosen workspace subfolder.
   - This includes:
     - `README.md`
     - `CONTEXT.md`
     - `bugs/` pipeline
     - `stories/` pipeline
     - `scripts/move-story.py`

4. **Hook the workspace routing into Scarab.**
   - If workspace-root `AGENTS.md` does not exist, create it from `assets/templates/workspace-root/AGENTS.md`.
   - If workspace-root `CLAUDE.md` does not exist, create it from `assets/templates/workspace-root/CLAUDE.md`.
   - If workspace-root `CONTEXT.md` does not exist, create it from `assets/templates/workspace-root/CONTEXT.md` and map the Scarab subfolder inside it.
   - If these files already exist, update them conservatively so that:
     - `AGENTS.md` and `CLAUDE.md` route through the workspace-root `CONTEXT.md`
     - the workspace-root `CONTEXT.md` points to the Scarab subfolder `CONTEXT.md`

5. **Preserve genericity.**
   - Do not inject project-specific product language, codebase assumptions, or vendor names into the scaffold.
   - Scarab-ICM is reusable for any software project.

## Operating behavior after install

Once Scarab-ICM exists in a workspace, agents should follow these rules.

### Adding a new story

When asked to add a story:

1. Create the story folder in `stories/01-inbox/`.
2. Start from the correct template in `stories/_templates/`.
   - use the epic template for epic stories
   - use the conventional template for standalone or child stories
3. Create `description.md` from that template.
4. Fill the required header fields:
   - `Status`
   - `Date`
   - `Slug`
5. Keep `Slug` equal to the story folder name.
6. If the folder slug is renamed later, update the `Slug` field in `description.md` to match.

### Adding a new bug

When asked to add a bug:

1. Create the bug folder in `bugs/01-inbox/`.
2. Start from the template in `bugs/_templates/`.
3. Create `description.md` from that template.
4. Fill the required header fields:
   - `Status`
   - `Date`
   - `Slug`
5. Keep `Slug` equal to the bug folder name.
6. If the folder slug is renamed later, update the `Slug` field in `description.md` to match.

### Moving a bug or story between stages

- Do **not** move folders manually.
- Use `scripts/move-story.py` for **all** stage transitions for both bugs and stories.
- The script is responsible for the folder move and for synchronizing linked metadata such as epic links and child-story table entries.

### Reading for implementation

When asked to work on an existing bug or story:

1. Read the workspace routing file (`AGENTS.md` or `CLAUDE.md`) if needed.
2. Read the workspace-root `CONTEXT.md`.
3. Read the Scarab subfolder `CONTEXT.md`.
4. Read the relevant pipeline `WORKFLOW.md`.
5. Read the target item's `description.md`.
6. Follow any links from the item into related epic, child story, or supporting notes before implementation.

The goal is that a single agent can recurse from workspace root to umbrella map to pipeline contract to item definition without guessing where the work lives.

## Guardrails

- Do not overwrite existing workspace routing files without reviewing and merging intentionally.
- Do not replace an existing bug/story system unless the user explicitly asks for migration.
- Do not move bug/story folders by hand when the transition script should be used.
- Do not leave a newly created bug/story without `Status`, `Date`, and `Slug` filled in.
- Do not let the `Slug` field drift from the folder name.

## References

- `references/overview.md` - what Scarab-ICM is and how the umbrella shape works
- `references/install-and-routing.md` - how to install and route the scaffold into an existing workspace
- `references/agent-behavior.md` - operating rules for creating, reading, and moving work items
- `assets/templates/` - copyable scaffold files and routing starters
