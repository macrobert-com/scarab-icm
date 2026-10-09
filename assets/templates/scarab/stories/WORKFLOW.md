# Stories Workflow

User stories are tracked as project folders inside `stories/`, which contains three stage folders:

```
stories/
|-- 01-inbox/         <- newly identified stories awaiting triage
|-- 02-processing/    <- stories actively being developed
`-- 03-complete/      <- stories that have been implemented and verified
```

## Folder naming convention

Each story is a folder created inside `stories/01-inbox/` using this pattern:

```
YYMMDDXX-slug
```

| Part | Description |
|------|-------------|
| `YY` | Two-digit year |
| `MM` | Two-digit month |
| `DD` | Two-digit day |
| `XX` | Two-digit sequence number for the day, starting at `01` |
| `slug` | File-system-safe kebab-case label describing the story |

**Example**: `26042901-user-can-reset-password`

## Templates

Story templates live in:

```
stories/_templates/
```

Use these files when creating or refining story descriptions:

- `stories/_templates/epic-story-template_v1.md`
- `stories/_templates/conventional-story-template_v1.md`

Treat these templates as the default reference point for story structure and content.

## Contents

Each story folder must contain a `description.md` file. This file describes the story and accumulates notes as work progresses.

When creating a new `description.md`:

- use the epic template for epic stories
- use the conventional template for standalone stories
- use the conventional template for child stories, keeping the `**Epic**` link
- adapt the template as needed while preserving the core workflow fields and sections

The file must include a `**Status**` field in its header that reflects the story's current stage.

The file should also include a `**Slug**` field whose value matches the story folder name. If the folder slug is edited or the folder is renamed, update the `**Slug**` value in the header to keep it synchronized.

| Stage folder     | Status value  |
|------------------|---------------|
| `01-inbox/`      | `Inbox`       |
| `02-processing/` | `Processing`  |
| `03-complete/`   | `Complete`    |

## Lifecycle

1. **Identified** - create the folder in `stories/01-inbox/` with a `description.md` based on the appropriate template; set `**Status**: Inbox`
2. **Taken on board** - move the folder to `stories/02-processing/` and update `**Status**: Processing`
3. **Complete** - move the folder to `stories/03-complete/` and update `**Status**: Complete`

## Epic Stories

An epic is a story that is too large to implement as a single unit of work. It acts as a container for a collection of related child stories that together deliver the full feature.

### Epic `description.md` structure

Use `stories/_templates/epic-story-template_v1.md` as the starting point.

```markdown
# {Title} (Epic)

**Status**: {Inbox|Processing|Complete}
**Date**: YYYY-MM-DD
**Slug**: YYMMDDXX-slug
**Type**: Epic

## Summary

{Brief description of the feature goal.}

## Child Stories

| ID | Story | Status |
|----|-------|--------|
| [YYMMDDXX](../or-../../{stage-folder}/{story-folder}/description.md) | Child Story Title | Inbox |

## Notes

{Any notes relevant to the epic as a whole.}
```

### Child story `description.md` structure

Use `stories/_templates/conventional-story-template_v1.md` as the starting point.

```markdown
# {Title}

**Status**: {Inbox|Processing|Complete}
**Date**: YYYY-MM-DD
**Slug**: YYMMDDXX-slug
**Epic**: [{epic-id} {Epic Title}](../or-../../{epic-folder}/description.md)

## Summary

{Brief description of this story's scope.}

## Acceptance Criteria

_To be defined._

## Notes

{Implementation notes.}
```

### Conventional standalone story `description.md` structure

Use `stories/_templates/conventional-story-template_v1.md` as the starting point and remove the `**Epic**` line when the story does not belong to an epic.

### Rules

- The epic's Child Stories table must be updated whenever a new child story is added.
- The `**Epic**` link in child stories must use a relative path to the parent epic's `description.md`.
- Child story statuses in the epic's Child Stories table must be kept in sync with the actual child story status.
- When a child story moves to a new stage folder, update the relative path to that child in the epic's Child Stories table to reflect its new location.
- When a child story moves to a new stage folder, update the `**Epic**` relative path in the child story's `description.md` to reflect the epic's current location.
- When the epic itself moves to a new stage folder, update the `**Epic**` relative path in every child story's `description.md` to reflect the epic's new location.
- Use the templates as the default reference, but allow story-specific Notes subsections and supporting detail to grow as the story evolves.
- Keep the `**Slug**` header value synchronized with the story folder name whenever the folder slug is edited or the folder is renamed.
- Use `scripts/move-story.py` for stage transitions rather than moving story folders manually.

## Committing a Story Description

When committing a `description.md` file for a story, use the following commit message format:

```
stories/<folder-name> <plain English description>
```

**Example**:
- `stories/26042901-user-can-reset-password Allow a user to request a password reset email`
