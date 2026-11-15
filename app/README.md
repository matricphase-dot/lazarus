# Lazarus Backend

FastAPI service for the Lazarus resurrection pipeline.

## Run locally

```bash
cd app
pip install -r requirements.txt
uvicorn main:app --reload
```

## Run tests

```bash
cd app
pip install pytest pytest-asyncio hypothesis
pytest
```

## Endpoints

- `GET /` — project info
- `GET /health` — health check
- `POST /resurrect` — start resurrection pipeline (body: `{ "repo_url": "..." }`)
- `GET /resurrect/{id}` — get resurrection record
- `GET /resurrects` — list all resurrections

## Kiro Integration

This backend is the orchestration layer for Kiro Crew agents defined in `../.kiro/agents/`. In production, the background pipeline drives real agents via the GitHub MCP server and Filesystem MCP.
