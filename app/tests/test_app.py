import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_home_returns_json(client):
    response = client.get("/")
    assert response.content_type == "application/json"

def test_health_returns_200(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_health_returns_healthy(client):
    response = client.get("/health")
    data = response.get_json()
    assert data["status"] == "healthy"

def test_health_has_timestamp(client):
    response = client.get("/health")
    data = response.get_json()
    assert "timestamp" in data

def test_status_returns_200(client):
    response = client.get("/api/status")
    assert response.status_code == 200

def test_status_returns_ok(client):
    response = client.get("/api/status")
    data = response.get_json()
    assert data["status"] == "ok"