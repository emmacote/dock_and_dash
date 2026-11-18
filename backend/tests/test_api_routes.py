import pytest
from dockanddash.api import app

@pytest.fixture
def client():
    client = app.test_client()
    return client

@pytest.mark.parametrize("endpoint", ["/activecontainers",
                                      "/inactivecontainers",
                                      "/volumes",
                                      "/images",
                                      "/networks"])
def test_routes_all_200(client, endpoint):
    res = client.get("/images")
    assert res.status_code == 200
