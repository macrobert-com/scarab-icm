# Bug Workflow

Bugs are tracked as project folders inside `bugs/`, which contains three stage folders:

```
bugs/
|-- 01-inbox/         <- newly identified bugs awaiting triage
|-- 02-processing/    <- bugs actively being investigated or fixed
`-- 03-complete/      <- bugs that have been fixed and verified
```

## Folder naming convention

Each bug is a folder created inside `bugs/01-inbox/` using this pattern:

```
YYMMDDXX-slug
```

| Part | Description |
|------|-------------|
| `YY` | Two-digit year |
| `MM` | Two-digit month |
| `DD` | Two-digit day |
| `XX` | Two-digit sequence number for the day, starting at `01` |
| `slug` | File-system-safe kebab-case label describing the bug |

**Example**: `26042901-login-redirect-loop`

## Templates

Bug templates live in:

```
bugs/_templates/
```

Use this file when creating or refining bug descriptions:

- `bugs/_templates/bug-template_v1.md`

Treat this template as the default reference point for bug structure and content.

## Contents

Each bug folder must contain a `description.md` file. This file describes the bug and accumulates notes on investigation and resolution as work progresses.

When creating a new `description.md`:

- start from `bugs/_templates/bug-template_v1.md`
- adapt the template as needed to fit the bug
- preserve the core workflow fields and sections unless there is a clear reason not to
- expand the Investigation and Resolution sections as the bug moves through the workflow

The file must include a `**Status**` field in its header that reflects the bug's current stage.

The file should also include a `**Slug**` field whose value matches the bug folder name. If the folder slug is edited or the folder is renamed, update the `**Slug**` value in the header to keep it synchronized.

| Stage folder     | Status value  |
|------------------|---------------|
| `01-inbox/`      | `Inbox`       |
| `02-processing/` | `Processing`  |
| `03-complete/`   | `Complete`    |

## Recommended bug description structure

Use `bugs/_templates/bug-template_v1.md` as the starting point.

```markdown
# Bug: {Short title}

**Status**: {Inbox|Processing|Complete}
**Date**: YYYY-MM-DD
**Slug**: YYMMDDXX-slug

## Description

{Describe the defect in plain language.}

## Steps to Reproduce

1. {Step one}
2. {Step two}
3. {Observed failure}

## Expected Behaviour

{Describe the correct behaviour.}

## Actual Behaviour

{Describe what currently happens instead.}

## Notes

{Capture context, scope, screenshots, suspected causes, constraints, or affected areas.}

## Investigation

_To be completed during processing._

## Resolution

_To be completed on fix._
```

Optional sections such as `Investigation Notes`, `Root Cause Hypothesis`, `Proposed Implementation Plan`, `Recommended Fix Notes`, `Affected Views`, and similar supporting detail may be added when helpful.

Keep the `**Slug**` header value synchronized with the bug folder name whenever the folder slug is edited or the folder is renamed.

## Lifecycle

1. **Identified** - create the folder in `bugs/01-inbox/` with a `description.md` based on the bug template; set `**Status**: Inbox`
2. **Taken on board** - move the folder to `bugs/02-processing/` and update `**Status**: Processing`
3. **Complete** - move the folder to `bugs/03-complete/` and update `**Status**: Complete`

## Rules

- New bugs start in `01-inbox/`.
- Create new bug descriptions from the template rather than from a blank file.
- Keep `Status`, `Date`, and `Slug` filled in.
- Use `scripts/move-story.py` for stage transitions rather than moving bug folders manually.

## Committing a Bug Description

When committing a `description.md` file for a bug, use the following commit message format:

```
bugs/<folder-name> <plain English description>
```

**Example**:
- `bugs/26042901-login-redirect-loop Fix infinite redirect loop after login`
