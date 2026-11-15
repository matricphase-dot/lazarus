# Lazarus — Resurrect Dead Code with Kiro Crew

**Kiroween 2026 • Resurrection Category**  
Bring your favorite dead technology back to life.

Lazarus is a working software application that resurrects abandoned, "dead" GitHub repositories using Kiro (IDE, CLI, Web, and Kiro Crew). Submit a URL to a dead repo, and a crew of Kiro agents analyzes it, writes a resurrection spec, modernizes the code, and opens a pull request — all while you watch on a haunted, polished dashboard.

> Built during the Kiroween 2026 Submission Period (Oct 30 – Dec 4, 2026).  
> New project. Built with Kiro. Open source (MIT).

## 🎃 What It Does

1. **Ingest** — Paste a public GitHub repo URL that appears abandoned (no recent commits, outdated dependencies, open issues).
2. **Autopsy** — Kiro Crew agents (Archivist, Mortician, Surgeon, Embalmer) perform a multi-agent post-mortem: read the code, dependency tree, open issues, and README to determine cause of death.
3. **Spec-Driven Resurrection Plan** — The crew writes a Kiro spec (`/.kiro/specs/`) describing exactly what to fix: dependency upgrades, security patches, API migrations, test scaffolding.
4. **Surgery** — Agents apply the spec, run tests via agent hooks, and push a modernization branch with a pull request back to the original repo.
5. **Dashboard** — A live, gothic-polished UI shows resurrection progress, before/after health scores, and the generated PR diff.

## 🛠 Tech Stack

- **Kiro IDE / CLI / Web** — Primary development environment. Every feature was spec-driven in Kiro.
- **Kiro Crew** — Multi-agent orchestration (see `/.kiro/agents/`).
- **Agent Hooks** — Automate test runs and PR creation on spec approval (see `/.kiro/hooks/`).
- **Steering Docs** — Guide Kiro's responses throughout the build (see `/.kiro/steering/`).
- **MCP** — GitHub MCP server for repo read/write; Filesystem MCP for local spec/artifact management.
- **Backend:** Python + Flask
- **Frontend:** Vanilla JS + HTML/CSS (no build step, deployable anywhere)
- **License:** MIT (visible in GitHub About section)

## 📁 Repository Structure

```
lazarus/
├── .kiro/                          # REQUIRED by Kiroween rules
│   ├── specs/                      # Spec-driven development artifacts
│   ├── hooks/                      # Agent hooks (automation)
│   ├── steering/                   # Steering documents for Kiro
│   └── agents/                     # Kiro Crew agent definitions
├── app/                            # Flask backend
├── frontend/                       # Deployable static UI
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
└── DEMO_VIDEO_SCRIPT.md
```

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/lazarus.git
cd lazarus

# Backend
cd app
pip install -r requirements.txt
gunicorn main:app --host 0.0.0.0 --port \$PORT

# Frontend
cd ../frontend
# Open index.html directly or serve with any static server
python -m http.server 8000
```

Then open `http://localhost:8000/frontend/index.html`, paste a dead GitHub repo URL, and watch Lazarus resurrect it.

## 🧠 How Kiro Was Used (Judging Write-Up)

### Kiro IDE, CLI, Web & Crew
The entire project was developed in **Kiro IDE**. We used **Kiro Crew** with four custom agents:
- **Archivist** — Ingests repo metadata, README, dependency files.
- **Mortician** — Determines cause of death (deprecated deps, CVEs, broken APIs).
- **Surgeon** — Writes code patches and modernization diffs.
- **Embalmer** — Preserves the original spirit while adding tests and docs.

Agents were tried in Kiro IDE (spec-driven) and Kiro Web (dashboard preview). Crew coordination happened through shared specs in `/.kiro/specs/`.

### Custom Agents
All four agents are defined in `/.kiro/agents/` with steering from `/.kiro/steering/`. They differ by role: Archivist reads, Mortician diagnoses, Surgeon operates, Embalmer documents. They communicate through the shared resurrection spec, not via fragile prompt chaining.

### Agent Hooks
- `pre-resurrection hook`: Validates the target repo is public and appears abandoned before any work begins.
- `post-spec hook`: Runs the test suite on the modernization branch; blocks PR creation if tests fail.
- `pr-creation hook`: Formats the PR body with resurrection summary, health-score delta, and Kiro attribution.

### Spec-Driven Development
We wrote the spec first (`/.kiro/specs/resurrection-spec.md`), then had Kiro implement against it. This replaced "vibe coding" — every change traces to a spec section, and agents self-correct by re-reading the spec before editing.

### Steering Docs
`/.kiro/steering/kiro-crew-steering.md` enforces: no secret keys in code, all PRs must reference the spec, all user-facing text must be gothic-themed but accessible, and every agent response must cite which spec section it implements.

### MCP
Connected the **GitHub MCP server** so agents can read repo trees, read file contents, create branches, and open PRs without leaving Kiro. Also used **Filesystem MCP** to read/write spec and artifact files locally.

### Property-Based Testing (PBT)
Used PBT (via `hypothesis`) to generate arbitrary repo shapes and confirm the Mortician agent consistently classifies "dead" vs "active" repos — catching edge cases unit tests missed (e.g., repos with only dependabot commits).

### Kiro Powers
Leveraged Kiro's bundled best-practices powers for Python project structure, FastAPI route conventions, and frontend accessibility (WCAG contrast ratios for the gothic theme).

## 🎯 Categories & Bonus Prizes

- **Primary:** Resurrection (dead tech = abandoned GitHub repos / dead code)
- **Bonus Blog Prize:** See `BLOG_POST.md` (publish during Submission Period)
- **Social Blitz Prize:** See `SOCIAL_POST.md` (post with `#KiroweenHackathon26`)
- **Best Demo:** Demo video script in `DEMO_VIDEO_SCRIPT.md` (under 3 minutes)

## 📋 Submission Checklist

See `SUBMISSION_CHECKLIST.md` for every Devpost requirement.

## 📄 License

MIT License. See `LICENSE`.

---

**Built for Kiroween 2026 by [Your Name/Team].**  
Deadline: Friday, December 4, 2026 at 2:00 PM Pacific Time.
