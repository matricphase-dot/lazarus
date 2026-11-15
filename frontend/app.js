// Lazarus frontend — vanilla JS module
// Calls the FastAPI backend at /resurrect and renders the dashboard.

const API_BASE = "https://lazarus-backend-md0x.onrender.com"; // same-origin by default
const form = document.getElementById("resurrect-form");
const repoInput = document.getElementById("repo-url");
const messageEl = document.getElementById("form-message");
const grid = document.getElementById("dashboard-grid");

function showMessage(text, type = "info") {
  messageEl.textContent = text;
  messageEl.className = type === "error" ? "error-msg" : "success-msg";
}

function setLoading(loading) {
  const btn = document.getElementById("submit-btn");
  if (btn) {
    btn.disabled = loading;
    btn.textContent = loading ? "Resurrecting…" : "Resurrect";
  }
}

function escapeHtml(unsafe) {
  if (!unsafe) return "";
  return unsafe
    .toString()
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function statusLabel(status) {
  const labels = {
    ingested: "Ingested",
    autopsied: "Autopsied",
    surgery: "Surgery",
    testing: "Testing",
    "pr-opened": "PR Opened",
    failed: "Failed",
  };
  return labels[status] || status;
}

function renderCard(record) {
  const prLink = record.pr_url
    ? `<a href="${escapeHtml(record.pr_url)}" target="_blank" rel="noopener" class="btn btn-outline" style="font-size:0.8rem;padding:0.5rem 1rem;">View Pull Request</a>`
    : "";

  return `
    <article class="card" id="card-${escapeHtml(record.resurrection_id)}">
      <div class="card-header">
        <h3>${escapeHtml(record.owner)}/${escapeHtml(record.name)}</h3>
        <span class="status-pill ${record.status}">${statusLabel(record.status)}</span>
      </div>
      <div class="repo">${escapeHtml(record.repo_url)}</div>
      <div class="health-row">
        <div class="health-item">
          <div class="label">Health before</div>
          <div class="value before">${record.health_score_before.toFixed(1)} / 10</div>
        </div>
        <div class="health-item">
          <div class="label">Health after</div>
          <div class="value after">${record.health_score_after.toFixed(1)} / 10</div>
        </div>
      </div>
      <div class="spec">
        <span class="label">Spec sections:</span>
        ${(record.spec_sections_applied || [])
          .map((s) => `<span class="badge">${escapeHtml(s)}</span>`)
          .join("")}
      </div>
      ${prLink}
    </article>
  `;
}

async function fetchDashboard() {
  try {
    const res = await fetch(`${API_BASE}/resurrects`);
    if (!res.ok) throw new Error("Failed to load dashboard");
    const records = await res.json();
    grid.innerHTML = records.map(renderCard).join("") || `
      <p class="empty-dashboard">No resurrections yet. Start one above.</p>
    `;
  } catch (err) {
    console.error(err);
    grid.innerHTML = `<p class="empty-dashboard error-msg">Dashboard unavailable — is the backend running?</p>`;
  }
}

async function handleSubmit(e) {
  e.preventDefault();
  const url = repoInput.value.trim();
  if (!url) return;

  setLoading(true);
  showMessage("");

  try {
    const res = await fetch(`${API_BASE}/resurrect`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ repo_url: url }),
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.detail || `HTTP ${res.status}`);
    }

    const data = await res.json();
    showMessage(
      `Resurrection started: ${data.resurrection_id} — ${data.message}`,
      "success"
    );
    repoInput.value = "";
    await fetchDashboard();
  } catch (err) {
    showMessage(err.message || "Something went wrong.", "error");
  } finally {
    setLoading(false);
  }
}

form.addEventListener("submit", handleSubmit);

// Initial load
fetchDashboard();
