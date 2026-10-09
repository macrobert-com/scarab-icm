# Scarab-ICM Overview

Scarab-ICM is an umbrella ICM for software delivery tracking.

## Form

Scarab-ICM uses an umbrella shape with two sibling pipelines:

- `bugs/`
- `stories/`

Each of those pipelines follows the same status progression:

- `01-inbox`
- `02-processing`
- `03-complete`

## Purpose

The scaffold exists to make bug and story definitions:

- easy for humans to inspect
- easy for agents to route into
- consistent across software projects
- editable in plain markdown at every stage

## Core rules

- New bugs and stories start in `01-inbox`.
- New items are created from templates, not from blank files.
- `Status`, `Date`, and `Slug` must be filled in when an item is created.
- `Slug` must match the folder name.
- Stage transitions are performed with `scripts/move-story.py`, not by manual moves.
