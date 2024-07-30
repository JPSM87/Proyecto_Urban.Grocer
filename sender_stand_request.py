import configuration
import requests
import data


def post_new_user(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=body,
                             headers=data.headers)
    print(response.status_code)
    print(response.json())  # Para mostrar el authToken para crear usuario
    return response


# Generar un nuevo usuario y recuperar el authToken
response = post_new_user(data.user_body)
if response.status_code == 201:
    auth_token = response.json().get('authToken')
    print(f'Token de autenticación generado: {auth_token}')
else:
    print(f"Fallo al crear usuario. Código de estado: {response.status_code}, Respuesta: {response.text}")


# Crear un nuevo kit usando el authToken generado
def post_new_kit(kit_body, token):
    headers_kit = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                             json=kit_body,
                             headers=headers_kit)
    print(f"URL de la solicitud: {configuration.URL_SERVICE + configuration.KITS_PATH}")
    print(f"Encabezados de la solicitud: {headers_kit}")
    print(f"Cuerpo de la solicitud: {kit_body}")
    print(f"Código de estado de la respuesta: {response.status_code}")
    print(f"Cuerpo de la respuesta: {response.text}")
    return response


# Crear un kit con el authToken generado
if auth_token:
    response = post_new_kit(data.kits_body, auth_token)
else:
    print("No hay authToken disponible, no se puede crear el kit.")


# Obtener un kit específico
def get_kit_by_id(kit_id, token):
    headers_kit = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f"{configuration.URL_SERVICE}{configuration.KITS_PATH}/{kit_id}", headers=headers_kit)
    print(f"URL de la solicitud: {configuration.URL_SERVICE}{configuration.KITS_PATH}/{kit_id}")
    print(f"Encabezados de la solicitud: {headers_kit}")
    print(f"Código de estado de la respuesta: {response.status_code}")
    print(f"Cuerpo de la respuesta: {response.text}")
    return response

