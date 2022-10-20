import json
import pytest
import sys

sys.path.append('../')

from helloworld.application import application

@pytest.fixture
def client():
    return application.test_client()

def test_response(client):
    result = client.get()
    response_body = json.loads(result.get_data())
    assert result.status_code == 200
    assert result.headers['Content-Type'] == 'application/json'
    assert response_body['Output'] == 'Hello Luiz'

def test_post(client):
    response = client.post(
                "/post",
                data = {"test": "test"},
                headers={"Content-Type": "application/json"},
            )
    assert response.status_code == 200
    assert response.json["Output"] == 'Hello Luiz'
