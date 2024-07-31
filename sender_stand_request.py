import configuration
import requests
import data

def get_auth_token():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=data.user_body,
                             headers=data.headers)
    return response.json().get('authToken') if response.status_code == 201 else None

def post_new_kit(kit_body, token):
    headers_kit = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers_kit)

def get_kit_by_id(kit_id, token):
    headers_kit = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    return requests.get(f"{configuration.URL_SERVICE}{configuration.KITS_PATH}/{kit_id}",
                        headers=headers_kit)
