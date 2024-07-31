import pytest
import sender_stand_request

@pytest.fixture
def auth_token():
    return sender_stand_request.get_auth_token()

# 1. Crear un kit con 1 solo caracter en el nombre de este.
def test_create_kit_with_min_length_name(auth_token):
    kit_body = {"name": "a"}
    response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

# 2. Crear un kit con el máximo de caracteres en el nombre de este (511).
def test_create_kit_with_max_length_name(auth_token):
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

# 3. Crear un kit con caracteres especiales en el nombre de este.
def test_create_kit_with_special_characters(auth_token):
    kit_body = {"name": "!@#№%"}
    response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

# 4. Crear un kit con espacios en el nombre.
def test_create_kit_with_spaces(auth_token):
    kit_body = {"name": " A Aaa "}
    response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

# 5. Crear un kit con números en el nombre de este.
def test_create_kit_with_numbers(auth_token):
    kit_body = {"name": "123"}
    response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

# 6. Error. No se puede crear un kit con el campo "name" vacío.
def test_create_kit_with_empty_name(auth_token):
    kit_body = {"name": ""}
    response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert response.status_code == 400

# 7. Error. No se puede crear un kit con el campo "name" con un número mayor a 511 caracteres.
def test_create_kit_with_too_long_name(auth_token):
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert response.status_code == 400

# 8. Error. No se puede crear un kit sin el parámetro "name".
def test_create_kit_without_name(auth_token):
    kit_body = {}
    response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert response.status_code == 400

# 9. Error. No se puede crear un kit con un valor numérico.
def test_create_kit_with_invalid_type_name(auth_token):
    kit_body = {"name": 123}
    response = sender_stand_request.post_new_kit(kit_body, auth_token)
    assert response.status_code == 400
