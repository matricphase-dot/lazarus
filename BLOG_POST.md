---
title: "Resurrecting Dead Code with Kiro Crew: How We Built Lazarus for Kiroween 2026"
date: 2026-11-13
tags: [kiro, kiroween, hackathon, ai-agents, spec-driven-development, resurrection]
canonical: https://your-blog.example.com/lazarus-kiroween-2026
---

# Resurrecting Dead Code with Kiro Crew: How We Built Lazarus for Kiroween 2026

*Published as part of the Kiroween 2026 hackathon.*

---

## The Idea: What If Dead Code Could Come Back?

Millions of public GitHub repositories are abandoned — outdated dependencies, unpatched CVEs, APIs that no longer exist. They're not useless; they're just dead.

For **Kiroween 2026** (Resurrection category), we asked: what if you could point at a dead repo and have a crew of AI agents bring it back to life? That's **Lazarus**.

## How Kiro Made It Possible

We didn't vibe-code this. We built Lazarus using **spec-driven development in Kiro**, orchestrated by **Kiro Crew** — four custom agents working from a shared spec.

### Kiro IDE, CLI, Web & Crew

We did the heavy lifting in **Kiro IDE**, where every feature started as a spec in `/.kiro/specs/`. Agents were tested in **Kiro Crew**, and we previewed the resurrection dashboard in **Kiro Web**. Switching between them was seamless: the same specs, the same steering docs, the same agents.

### Custom Kiro Crew Agents

| Agent | Role |
|-------|------|
| Archivist | Reads repo tree, README, dependencies, commit history |
| Mortician | Diagnoses cause of death (deprecated deps, CVEs, API breakage) |
| Surgeon | Applies modernization patches mapped to spec sections |
| Embalmer | Adds tests, docs, changelog — preserving original spirit |

Agents communicate through shared artifact files, not fragile prompt chains. That's spec-driven development: each agent reads an input file, writes an output file, and cites the spec section it implements.

### Agent Hooks

Three hooks automate the pipeline:

1. **Pre-resurrection** — validates the target repo is public and abandoned before agents run.
2. **Post-spec** — runs the test suite on the modernization branch; blocks PR creation if tests fail.
3. **PR creation** — verifies the PR body references spec sections and includes the health-score delta.

### Steering Docs

`/.kiro/steering/kiro-crew-steering.md` keeps every agent honest: no secrets, preserve original intent, cite the spec on every response, gothic-but-accessible UI. Without steering, Kiro wanted to do full framework migrations; steering forced targeted modernization — exactly what "resurrection" means.

### MCP

We connected the **GitHub MCP server** so agents can read repo trees, create branches, and open pull requests without leaving Kiro. **Filesystem MCP** handles local spec and artifact reads/writes.

### Property-Based Testing

Using Hypothesis, we PBT-tested the Mortician's dead-vs-active classification across arbitrary repo shapes — catching edge cases unit tests missed (e.g., Dependabot-only commits).

### Kiro Powers

Kiro's bundled best-practices powers shaped our Python project structure, FastAPI route conventions, and frontend WCAG accessibility.

## The Result

Point Lazarus at `github.com/owner/abandoned-repo`, and it:

1. Autopsies the repo (Archivist)
2. Diagnoses cause of death (Mortician)
3. Writes a resurrection spec and applies patches (Surgeon)
4. Adds tests and docs (Embalmer)
5. Runs tests via agent hooks
6. Opens a pull request back to the original repo

Health scores jump from ~2.4 to ~7.9. Four spec sections applied per resurrection.

## Why This Matters

Dead code still solves real problems. Lazarus makes resurrection repeatable, traceable, and open source — all built with Kiro.

Try it: github.com/YOUR_USERNAME/lazarus  
#KiroweenHackathon26 #Kiro #Resurrection
