"""Tests for Lazarus routes (property-based + unit)."""

from fastapi.testclient import TestClient
from hypothesis import given, strategies as st

from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Lazarus"
    assert "Kiroween 2026" in data["hackathon"]


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "alive"


def test_resurrect_valid_github_url():
    response = client.post(
        "/resurrect",
        json={"repo_url": "https://github.com/octocat/Hello-World"},
    )
    assert response.status_code == 202
    data = response.json()
    assert data["status"] == "ingested"
    assert "resurrection_id" in data


@given(
    owner=st.text(min_size=1, max_size=40).filter(lambda s: " " not in s),
    name=st.text(min_size=1, max_size=40).filter(lambda s: " " not in s),
)
def test_resurrect_arbitrary_repo_names(owner, name):
    """Property-based test: any well-formed owner/repo pair is accepted."""
    url = f"https://github.com/{owner}/{name}"
    response = client.post("/resurrect", json={"repo_url": url})
    assert response.status_code == 202


def test_resurrect_invalid_url():
    response = client.post("/resurrect", json={"repo_url": "https://notgithub.com/x/y"})
    assert response.status_code == 400 or response.status_code == 422
