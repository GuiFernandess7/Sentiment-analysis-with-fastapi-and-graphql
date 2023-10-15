from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_graphql_query():
    response = client.post(
        "/app",
        json={"query": "getData { id }"}
    )
    assert response.status_code == 200

def test_graphql_sentiment_response():
    sentence = 'This is awesome!'
    response = client.post(
        '/app',
        json={"query": f"mutation {{ addData(sentence: '{sentence}') {{ sentence, sentimentScore }} }}"}
    )
    assert response.status_code == 200
    #assert isinstance(data["data"]["getData"], list)
    #assert data["data"]["addData"]["sentence"] == sentence