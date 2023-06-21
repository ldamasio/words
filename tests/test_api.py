import pytest
from api.app import app
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    assert client.get("/").status_code == 200

def test_health(client):
    assert client.get("/health").status_code == 200

def test_vowel_non_post_method(client):
    response = client.get('/vowel_count')
    assert response.status_code != 200

def test_vowel_inexistent_route(client):
    response = client.get('/inexistent')
    assert response.status_code == 404

def test_vowel_content_type_json_but_non_json_body(client):
    response = client.post('/vowel_count', content_type='application/json')
    assert not response.status_code == 200

def test_vowel_content_type_json_and_a_body(client):
    json_dict = {"hw": "ok"}
    response = client.post('/vowel_count', content_type='application/json', \
                           data=json.dumps(json_dict))
    assert response.status_code == 200

def test_vowel_valid_json_body_response(client):
    json_dict = {"words": ["batman", "robin", "coringa"], "order": "desc"}
    response = client.post('/vowel_count', content_type='application/json', \
                           data=json.dumps(json_dict))
    assert response.status_code == 200

def test_vowel_valid_request(client):
    json_dict = {"words": ["batman", "robin", "coringa"], "order": "desc"}
    response = client.post('/vowel_count', content_type='application/json', \
                           data=json.dumps(json_dict))
    assert response.data ==  b'{"batman": "2", "robin": "2", "coringa": "3"}'

def test_vowel_invalid_json_body_response(client):
    json_dict = {"wo50rds": ["bat50man", "ro$$bin", "cor@@inga"]}
    response = client.post('/vowel_count', content_type='application/json', \
                           data=json.dumps(json_dict))
    assert not response.data == \
          b'{"batman": "2", "robin": "2", "coringa": "3"}'

def test_sort_asc(client):
    json_dict = {"words": ["batman", "robin", "coringa"], "order": "asc"}
    response = client.post('/sort', content_type='application/json', \
                           data=json.dumps(json_dict))
    assert response.data ==  b'["batman", "coringa", "robin"]'

def test_sort_desc(client):
    json_dict = {"words": ["batman", "robin", "coringa"], "order": "desc"}
    response = client.post('/sort', content_type='application/json', \
                           data=json.dumps(json_dict))
    assert response.data ==  b'["robin", "coringa", "batman"]'
