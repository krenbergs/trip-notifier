import pytest
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture
def test_app():
    with TestClient(app) as test_client:
        yield test_client
