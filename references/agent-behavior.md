# Agent Behavior

## Creating a new story

- Create the folder in `stories/01-inbox/`.
- Start from the correct story template.
- Create `description.md` from the template.
- Fill `Status`, `Date`, and `Slug` immediately.
- Keep `Slug` synchronized with the folder name.

## Creating a new bug

- Create the folder in `bugs/01-inbox/`.
- Start from the bug template.
- Create `description.md` from the template.
- Fill `Status`, `Date`, and `Slug` immediately.
- Keep `Slug` synchronized with the folder name.

## Moving items between stages

- Do not move folders by hand.
- Use `scripts/move-story.py` for all bug and story stage transitions.

## Reading items for implementation

Read in this order:

1. root `AGENTS.md` or `CLAUDE.md`
2. workspace-root `CONTEXT.md`
3. Scarab subfolder `CONTEXT.md`
4. pipeline `WORKFLOW.md`
5. target `description.md`

This keeps routing small and lets the work item definition hold the detailed implementation context.
