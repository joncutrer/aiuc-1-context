# CLAUDE.md

This file provides guidance for AI assistants (Claude and others) working in this repository.

## Repository Overview

**Repository:** `joncutrer/aiuc-1-context`
**Status:** Freshly initialized — no source code has been committed yet.

This repository was created on 2026-03-05 and is configured for development on the branch `claude/add-claude-documentation-JtxRd`. As the codebase grows, update this file to reflect the project's actual structure, conventions, and workflows.

---

## Codebase Structure

> Update this section once source files are added.

```
aiuc-1-context/
├── CLAUDE.md          # This file
└── (no source files yet)
```

---

## Development Workflow

### Branching Strategy

- The default development branch used by Claude agents is prefixed with `claude/` and ends with a session ID (e.g., `claude/add-claude-documentation-JtxRd`).
- **Never push directly to `main` or `master`** without explicit permission.
- Always confirm the target branch before pushing:
  ```bash
  git branch --show-current
  ```

### Making Changes

1. Ensure you are on the correct feature branch before starting work.
2. Make focused, atomic commits — one logical change per commit.
3. Write descriptive commit messages in the imperative mood (e.g., `Add authentication module`, `Fix null pointer in user service`).
4. Push with upstream tracking:
   ```bash
   git push -u origin <branch-name>
   ```

### Git Push Retry Policy

If a push fails due to a network error (not a 403 authorization error), retry with exponential backoff:
- Attempt 1: immediate
- Attempt 2: wait 2s
- Attempt 3: wait 4s
- Attempt 4: wait 8s
- Attempt 5: wait 16s

A **403 error** indicates a branch name or permission issue — do not retry; investigate instead.

---

## Conventions

> These are defaults to follow until project-specific conventions are established.

### Code Style

- Follow the idioms of the language in use (PEP 8 for Python, `gofmt` for Go, Prettier defaults for JavaScript/TypeScript, etc.).
- Prefer explicit over implicit.
- Avoid over-engineering: only add complexity the current task requires.

### Comments

- Only add comments where the logic is non-obvious.
- Do not add docstrings or type annotations to code you did not change.

### Security

- Never commit secrets, API keys, or credentials. Use environment variables or a secrets manager.
- Validate all external input at system boundaries (user input, external APIs).
- Follow OWASP top-10 guidance; avoid introducing SQL injection, XSS, command injection, etc.

### File Management

- Prefer editing existing files over creating new ones.
- Do not create documentation files (e.g., `*.md`) unless explicitly requested.
- Delete unused code rather than commenting it out.

---

## Running Tests

> Update this section with actual test commands once a project is initialized.

```bash
# Example — replace with actual commands
npm test          # Node.js projects
pytest            # Python projects
go test ./...     # Go projects
cargo test        # Rust projects
```

---

## Environment Setup

> Update this section with actual setup steps once dependencies are defined.

1. Clone the repository.
2. Install dependencies (commands TBD once a package manager is chosen).
3. Copy `.env.example` to `.env` and fill in required values (TBD).
4. Run the development server (command TBD).

---

## AI Assistant Guidelines

- **Read before modifying.** Always read a file before editing it.
- **Scope changes narrowly.** Only modify what is directly required by the task.
- **Confirm destructive actions.** Before deleting files, force-pushing, or dropping data, confirm with the user.
- **Do not retry blocked tool calls.** If a tool call is denied, ask the user why before trying again.
- **Keep this file current.** After significant structural changes, update `CLAUDE.md` to reflect the new state.
- **One task at a time.** Mark a `TodoWrite` task as completed immediately after finishing it; do not batch completions.

---

*Last updated: 2026-03-05*
