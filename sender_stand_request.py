import configuration
import data
import requests

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)
response = post_new_user(data.user_body)
token = response.json()['authToken']
print(response.status_code)
print(response.json())

def post_new_client_kit(kit_body, auth_token):
    header = data.headers_kit.copy()
    header['Authorization'] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KIT_PATH,
                         json=kit_body,
                         headers=header)
response = post_new_client_kit(data.kit_body, token)
print(response.status_code)
print(response.json())
