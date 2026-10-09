# Install and Routing

Scarab-ICM is installed into an existing workspace, not as a replacement for the whole workspace.

## Install model

1. Choose a subfolder path inside the target workspace.
2. Copy the scaffold from `assets/templates/scarab/` into that subfolder.
3. Ensure the workspace root contains:
   - `AGENTS.md`
   - `CLAUDE.md`
   - `CONTEXT.md`
4. Route `AGENTS.md` and `CLAUDE.md` to the workspace-root `CONTEXT.md`.
5. Add the Scarab subfolder location to the workspace-root `CONTEXT.md`.
6. Use the Scarab subfolder `CONTEXT.md` as the map for the installed umbrella.

## File ownership

- Workspace-root `AGENTS.md` and `CLAUDE.md` are routing files.
- Workspace-root `CONTEXT.md` is the top-level map.
- Scarab subfolder `CONTEXT.md` is the umbrella map for bugs and stories.
- Each pipeline `WORKFLOW.md` defines the rules of that pipeline.

## Merge rule

If root routing files already exist, merge conservatively. Do not overwrite existing content blindly.
