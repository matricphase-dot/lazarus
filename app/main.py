from flask import Flask, request, jsonify
from flask_cors import CORS
import uuid
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)

RESURRECTIONS = {}

@app.route("/")
def root():
    return jsonify({
        "name": "Lazarus",
        "tagline": "Resurrect dead code with Kiro Crew.",
        "hackathon": "Kiroween 2026 � Resurrection Category",
        "docs": "/docs"
    })

@app.route("/health")
def health():
    return jsonify({"status": "alive", "kiro_crew": "ready"})

@app.route("/resurrect", methods=["POST"])
def resurrect():
    data = request.get_json()
    repo_url = data.get("repo_url", "")
    
    if not repo_url or not repo_url.startswith("https://github.com/"):
        return jsonify({"error": "Only GitHub repository URLs are supported"}), 400
    
    parts = repo_url.replace("https://github.com/", "").split("/")
    if len(parts) < 2 or not parts[0] or not parts[1]:
        return jsonify({"error": "Invalid GitHub repository URL"}), 400
    
    owner, name = parts[0], parts[1]
    resurrection_id = f"res-{uuid.uuid4().hex[:12]}"
    now = datetime.now(timezone.utc).isoformat()
    
    record = {
        "resurrection_id": resurrection_id,
        "repo_url": repo_url,
        "owner": owner,
        "name": name,
        "status": "ingested",
        "cause_of_death": [],
        "health_score_before": 0.0,
        "health_score_after": 0.0,
        "spec_sections_applied": [],
        "pr_url": None,
        "created_at": now,
        "updated_at": now,
        "kiro_agents_used": ["Archivist", "Mortician", "Surgeon", "Embalmer"]
    }
    RESURRECTIONS[resurrection_id] = record
    
    return jsonify({
        "resurrection_id": resurrection_id,
        "status": "ingested",
        "message": f"Resurrection pipeline started for {owner}/{name}. Kiro Crew agents have been dispatched."
    }), 202

@app.route("/resurrect/<resurrection_id>")
def get_resurrection(resurrection_id):
    record = RESURRECTIONS.get(resurrection_id)
    if not record:
        return jsonify({"error": "Resurrection not found"}), 404
    return jsonify(record)

@app.route("/resurrects")
def list_resurrections():
    return jsonify(sorted(RESURRECTIONS.values(), key=lambda r: r["created_at"], reverse=True))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
