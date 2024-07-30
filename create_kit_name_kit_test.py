import pytest
import configuration
import data
import requests

# Función auxiliar para crear un kit
def post_new_kit(kit_body, token):
    headers_kit = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_kit)

# Función auxiliar para crear un usuario y obtener el token
def get_auth_token():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=data.user_body,
                             headers=data.headers)
    return response.json().get('authToken') if response.status_code == 201 else None

@pytest.fixture
def auth_token():
    return get_auth_token()

# Pruebas positivas
def test_create_kit_with_min_length_name(auth_token):
    kit_body = {"name": "a"}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

def test_create_kit_with_max_length_name(auth_token):
    kit_body = {"name": "a" * 511}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

def test_create_kit_with_special_characters(auth_token):
    kit_body = {"name": "!@#№%"}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

def test_create_kit_with_spaces(auth_token):
    kit_body = {"name": " A Aaa "}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

def test_create_kit_with_numbers(auth_token):
    kit_body = {"name": "123"}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

# Pruebas negativas
def test_create_kit_with_empty_name(auth_token):
    kit_body = {"name": ""}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_create_kit_with_too_long_name(auth_token):
    kit_body = {"name": "a" * 512}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_create_kit_without_name(auth_token):
    kit_body = {}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_create_kit_with_invalid_type_name(auth_token):
    kit_body = {"name": 123}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 400
