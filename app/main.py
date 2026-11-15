"""Lazarus backend — FastAPI application.

Resurrects abandoned GitHub repositories using Kiro Crew agents.
Built for Kiroween 2026 — Resurrection Category.
"""

import os
import uuid
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI(
    title="Lazarus",
    description="Resurrect dead code with Kiro Crew agents.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------
class ResurrectRequest(BaseModel):
    repo_url: HttpUrl = Field(..., description="Public GitHub repository URL")
    force: bool = Field(False, description="Force resurrection even if active")


class ResurrectResponse(BaseModel):
    resurrection_id: str
    status: str
    message: str


class ResurrectionRecord(BaseModel):
    resurrection_id: str
    repo_url: str
    owner: str
    name: str
    status: str
    cause_of_death: List[str] = []
    health_score_before: float = 0.0
    health_score_after: float = 0.0
    spec_sections_applied: List[str] = []
    pr_url: Optional[str] = None
    created_at: str
    updated_at: str
    kiro_agents_used: List[str] = [
        "Archivist", "Mortician", "Surgeon", "Embalmer"
    ]


# ---------------------------------------------------------------------------
# In-memory store (replace with a DB in production)
# ---------------------------------------------------------------------------
RESURRECTIONS: Dict[str, ResurrectionRecord] = {}


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.get("/")
def root() -> Dict[str, str]:
    return {
        "name": "Lazarus",
        "tagline": "Resurrect dead code with Kiro Crew.",
        "hackathon": "Kiroween 2026 — Resurrection Category",
        "docs": "/docs",
    }


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "alive", "kiro_crew": "ready"}


@app.post("/resurrect", response_model=ResurrectResponse, status_code=202)
async def resurrect(
    request: ResurrectRequest,
    background_tasks: BackgroundTasks,
) -> ResurrectResponse:
    """Start a resurrection pipeline for a GitHub repository.

    This endpoint validates the repo, then queues the Kiro Crew agents
    (Archivist -> Mortician -> Surgeon -> Embalmer) via background tasks.
    """
    repo_url = str(request.repo_url).rstrip("/")

    # Validate it's a github.com URL
    if not repo_url.startswith("https://github.com/"):
        raise HTTPException(
            status_code=400, detail="Only GitHub repository URLs are supported"
        )

    # Simple GitHub URL parse: https://github.com/owner/repo
    parts = repo_url.replace("https://github.com/", "").split("/")
    if len(parts) < 2 or not parts[0] or not parts[1]:
        raise HTTPException(status_code=400, detail="Invalid GitHub repository URL")

    owner, name = parts[0], parts[1]
    resurrection_id = f"res-{uuid.uuid4().hex[:12]}"

    now = datetime.now(timezone.utc).isoformat()

    record = ResurrectionRecord(
        resurrection_id=resurrection_id,
        repo_url=repo_url,
        owner=owner,
        name=name,
        status="ingested",
        created_at=now,
        updated_at=now,
    )
    RESURRECTIONS[resurrection_id] = record

    background_tasks.add_task(run_resurrection_pipeline, resurrection_id)

    return ResurrectResponse(
        resurrection_id=resurrection_id,
        status="ingested",
        message=(
            f"Resurrection pipeline started for {owner}/{name}. "
            "Kiro Crew agents have been dispatched."
        ),
    )


@app.get("/resurrect/{resurrection_id}", response_model=ResurrectionRecord)
def get_resurrection(resurrection_id: str) -> ResurrectionRecord:
    record = RESURRECTIONS.get(resurrection_id)
    if not record:
        raise HTTPException(status_code=404, detail="Resurrection not found")
    return record


@app.get("/resurrects", response_model=List[ResurrectionRecord])
def list_resurrections() -> List[ResurrectionRecord]:
    return sorted(
        RESURRECTIONS.values(),
        key=lambda r: r.created_at,
        reverse=True,
    )


# ---------------------------------------------------------------------------
# Background pipeline (mocked for the submission scaffold; wire to real
# Kiro Crew / GitHub MCP in production)
# ---------------------------------------------------------------------------
async def run_resurrection_pipeline(resurrection_id: str) -> None:
    """Simulate the Kiro Crew resurrection pipeline.

    In a full deployment this drives the actual agents defined in
    /.kiro/agents/. For the hackathon scaffold we advance the record
    through the defined stages so the dashboard is demonstrable.
    """
    import asyncio

    record = RESURRECTIONS[resurrection_id]

    stages: List[str] = [
        "autopsied",
        "surgery",
        "testing",
        "pr-opened",
    ]

    for stage in stages:
        await asyncio.sleep(2)  # simulate agent work
        record.status = stage
        record.updated_at = datetime.now(timezone.utc).isoformat()

        if stage == "autopsied":
            record.cause_of_death = ["deprecated_deps", "abandonment"]
            record.health_score_before = 2.4
        elif stage == "surgery":
            record.spec_sections_applied = ["S1", "S2", "S4", "S5"]
            record.health_score_after = 7.9
        elif stage == "testing":
            pass  # post-spec hook passed
        elif stage == "pr-opened":
            record.pr_url = (
                f"https://github.com/{record.owner}/{record.name}/"
                f"pull/1"
            )

    RESURRECTIONS[resurrection_id] = record


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
