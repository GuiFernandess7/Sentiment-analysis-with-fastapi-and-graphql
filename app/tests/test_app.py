from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_graphql_query():
    response = client.post(
        "/app",
        json={"query": "getData { id }"}
    )
    assert response.status_code == 200
