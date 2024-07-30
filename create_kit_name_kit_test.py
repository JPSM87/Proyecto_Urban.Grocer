import pytest
import configuration
import data
import requests

# Función para crear un kit
def post_new_kit(kit_body, token):
    headers_kit = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_kit)

# Función para crear un usuario y obtener el token
def get_auth_token():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=data.user_body,
                             headers=data.headers)
    return response.json().get('authToken') if response.status_code == 201 else None

# Pruebas positivas
# 1. Crear un kit con 1 solo caracter en el nombre
def test_create_kit_with_min_length_name():
    auth_token = get_auth_token()  # Obtener el token dentro de la prueba
    if not auth_token:
        pytest.skip("No se pudo obtener el authToken")
    kit_body = {"name": "a"}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

# 2. Crear un kit con el máximo de caracteres en el nombre (511)
def test_create_kit_with_max_length_name():
    auth_token = get_auth_token()  # Obtener el token dentro de la prueba
    if not auth_token:
        pytest.skip("No se pudo obtener el authToken")
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

# 3. Crear un kit con caracteres especiales en el nombre
def test_create_kit_with_special_characters():
    auth_token = get_auth_token()  # Obtener el token dentro de la prueba
    if not auth_token:
        pytest.skip("No se pudo obtener el authToken")
    kit_body = {"name": "!@#№%"}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

# 4. Crear un kit con espacios en el nombre
def test_create_kit_with_spaces():
    auth_token = get_auth_token()  # Obtener el token dentro de la prueba
    if not auth_token:
        pytest.skip("No se pudo obtener el authToken")
    kit_body = {"name": " A Aaa "}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

# 5. Crear un kit con números en el nombre
def test_create_kit_with_numbers():
    auth_token = get_auth_token()  # Obtener el token dentro de la prueba
    if not auth_token:
        pytest.skip("No se pudo obtener el authToken")
    kit_body = {"name": "123"}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json().get('name') == kit_body['name']

# Pruebas negativas
# 6. Error. No se puede crear un kit con el campo "name" vacío
def test_create_kit_with_empty_name():
    auth_token = get_auth_token()  # Obtener el token dentro de la prueba
    if not auth_token:
        pytest.skip("No se pudo obtener el authToken")
    kit_body = {"name": ""}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 400

# 7. Error. No se puede crear un kit con el campo "name" con un número mayor a 511 caracteres
def test_create_kit_with_too_long_name():
    auth_token = get_auth_token()  # Obtener el token dentro de la prueba
    if not auth_token:
        pytest.skip("No se pudo obtener el authToken")
    kit_body = {"name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 400

# 8. Error. No se puede crear un kit sin el parámetro nombre
def test_create_kit_without_name():
    auth_token = get_auth_token()  # Obtener el token dentro de la prueba
    if not auth_token:
        pytest.skip("No se pudo obtener el authToken")
    kit_body = {}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 400

# 9. Error. No se puede crear un kit con un valor numérico en el campo "name"
def test_create_kit_with_invalid_type_name():
    auth_token = get_auth_token()  # Obtener el token dentro de la prueba
    if not auth_token:
        pytest.skip("No se pudo obtener el authToken")
    kit_body = {"name": 123}
    response = post_new_kit(kit_body, auth_token)
    assert response.status_code == 400
