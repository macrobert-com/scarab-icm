# Scarab-ICM Context

Scarab-ICM is an umbrella structure for software delivery work inside this workspace.

## Purpose

This folder organizes two sibling pipelines:

- `bugs/` - track software defects through inbox, processing, and complete
- `stories/` - track software stories through inbox, processing, and complete

## Routing

- For bug work, read `bugs/WORKFLOW.md`
- For story work, read `stories/WORKFLOW.md`
- For stage transitions, use `scripts/move-story.py`

## Working rule

Create new bugs and stories from templates in the relevant `_templates/` folder. New items start in `01-inbox/` and must include synchronized `Status`, `Date`, and `Slug` header fields.
