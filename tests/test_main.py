import os
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

# A test-only configuration lets the app be imported without a local .env or DB.
os.environ.setdefault("POSTGRES_USER", "test-user")
os.environ.setdefault("POSTGRES_PASSWORD", "test-password")
os.environ.setdefault("POSTGRES_DB", "test-db")
os.environ.setdefault("POSTGRES_HOST", "localhost")
os.environ.setdefault("GREETING", "Test guestbook")

import main


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> TestClient:
    connection = MagicMock()
    connection.__enter__.return_value = connection
    connection.__exit__.return_value = False
    connection.execute.return_value.fetchall.return_value = [
        ("Ada", "Hello from tests"),
    ]
    monkeypatch.setattr(main, "connect", lambda: connection)

    with TestClient(main.app) as test_client:
        yield test_client


def test_root_returns_greeting(client: TestClient) -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == main.settings.greeting


def test_health_is_ok(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_messages(client: TestClient) -> None:
    response = client.get("/messages")

    assert response.status_code == 200
    assert response.json() == [{"author": "Ada", "text": "Hello from tests"}]


def test_add_message(client: TestClient) -> None:
    response = client.post(
        "/messages",
        json={"author": "Grace", "text": "A test message"},
    )

    assert response.status_code == 200
    assert response.json() == {"ok": True}
