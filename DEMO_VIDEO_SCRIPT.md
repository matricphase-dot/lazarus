# Demo Video Script — Lazarus

**Kiroween 2026 • Resurrection Category**  
**Target length:** Under 3 minutes (judges stop watching at 3:00)  
**Platform:** YouTube (public) — link goes in Devpost submission form

---

## Structure (0:00 – 3:00)

| Time | Section | What to show / say |
|------|---------|--------------------|
| 0:00–0:20 | Hook | Gothic title card: "Lazarus — Resurrect Dead Code." Quick cut of a dead repo → living PR. |
| 0:20–0:45 | The problem | Show an abandoned GitHub repo: last commit 2 years ago, deprecated deps, open issues. Say: "Millions of repos are dead. Lazarus brings them back." |
| 0:45–1:10 | The product | Paste the repo URL into Lazarus dashboard. Click "Resurrect." Show the Kiro Crew pipeline running (Archivist → Mortician → Surgeon → Embalmer). |
| 1:10–1:40 | The result | Show the health score jump (2.4 → 7.9). Show the spec sections applied (S1, S2, S4, S5). Show the diff of modernized code. |
| 1:40–2:10 | Kiro under the hood | Screen-record Kiro IDE showing `/.kiro/specs/`, `/.kiro/hooks/`, `/.kiro/steering/`. Narrate: spec-driven development, agent hooks, steering docs. |
| 2:10–2:35 | The PR | Show the GitHub PR opened by Lazarus with the resurrection summary template. Click through to the actual diff. |
| 2:35–3:00 | Close | "Built with Kiro for Kiroween 2026. Resurrect dead code at [github]." End card. |

---

## Narrator Script (approx. 450 words ≈ 3 minutes)

[0:00–0:20]  
"(On screen: a foggy graveyard of old commit logos, then a spark.)  
'What happens to code when everyone walks away? Millions of GitHub repositories sit abandoned — outdated dependencies, unpatched CVEs, broken APIs. Dead technology.  
Meet Lazarus. We resurrect dead code with Kiro Crew agents.'"

[0:20–0:45]  
"(Show a real abandoned repo: last commit 2023, `requirements.txt` with Django 1.11, 47 open issues.)  
'This repository is dead. But it solved a real problem once. So we give it to Lazarus.'  
(Paste URL into the dashboard. Click Resurrect.)  
'Lazarus dispatches a crew of four Kiro agents: the Archivist reads the repo, the Mortician diagnoses the cause of death, the Surgeon applies targeted patches, and the Embalmer adds tests and docs.'"

[0:45–1:10]  
"(Screen-record the dashboard pipeline animating: Archivist → Mortician → Surgeon → Embalmer.)  
'This isn't vibe coding. Every agent works from a spec in `/.kiro/specs/` — spec-driven development. Agent hooks run tests before any pull request is created. Steering docs keep the agents honest: no secrets, preserve original intent, cite the spec on every change.'"

[1:10–1:40]  
"(Show before/after health scores: 2.4 → 7.9. Show spec sections S1, S2, S4, S5 applied. Show a diff of a dependency bump and a security patch.)  
'The health score jumps from 2.4 to 7.9. Four spec sections applied: dependency upgrade, security patch, test scaffolding, documentation. The original project's spirit is preserved — only modernized.'"

[1:40–2:10]  
"(Switch to Kiro IDE. Open `/.kiro/specs/resurrection-spec.md`, `/.kiro/hooks/post-spec-hook.md`, `/.kiro/steering/kiro-crew-steering.md`.)  
'We built this in Kiro IDE, orchestrated the crew in Kiro Crew, and previewed the dashboard in Kiro Web. We connected the GitHub MCP server so agents can read repos and open pull requests directly from Kiro. We even used property-based testing to make sure the Mortician classifies dead repos correctly — catching edge cases unit tests missed.'"

[2:10–2:35]  
"(Show the GitHub PR: 'Lazarus Resurrection' with cause of death, spec sections, health delta.)  
'Lazarus opens a pull request back to the original repo — with the full resurrection summary, health-score delta, and Kiro attribution. The dead code lives again.'"

[2:35–3:00]  
"'Lazarus. Resurrect dead code with Kiro Crew. Built for Kiroween 2026 — Resurrection Category.  
GitHub: github.com/YOUR_USERNAME/lazarus'  
(End card: Kiroween 2026 logo, #KiroweenHackathon26, MIT License.)"

---

## Production Notes

- **Record on the device it was built for** (Kiro IDE + browser), per Kiroween rules.
- **Keep under 3 minutes.** Judges are not required to watch beyond three minutes.
- **No copyrighted music.** Use silence or royalty-free audio only.
- **No third-party trademarks** unless you have permission. Blur the GitHub logo if needed, or use it nominatively (permitted).
- **Upload to YouTube, make public**, and paste the URL in the Devpost submission form.
