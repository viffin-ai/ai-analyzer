from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_missing_text_returns_422():
    response = client.post("/webhook", json={"user_id": 7})
    assert response.status_code == 422


def test_webhook_returns_category(monkeypatch):
    def fake_analyze(text):
        return {"category": "жалоба"}
    
    monkeypatch.setattr("app.main.analyze_request", fake_analyze)

    response = client.post("/webhook", json={"text": "тест", "user_id": 7})
    assert response.status_code == 200
    assert response.json()["category"] == "жалоба"

