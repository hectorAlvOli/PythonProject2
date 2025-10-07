import data
import sender_stand_request


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    response = sender_stand_request.post_new_user(data.user_body)
    token = response.json()['authToken']
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert kit_response.status_code == 201

def negative_assert(name):
    response = sender_stand_request.post_new_user(data.user_body)
    token = response.json()['authToken']
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert kit_response.status_code == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parametros requeridos"

def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_user(data.user_body)
    token = response.json()['authToken']
    kit_response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "No se han aprobados los parametros requeridos"

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert ("a")

def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_0_letter_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_no_name(kit_body)

def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_special_characters_in_name_get_success_response():
    positive_assert("@@@@")

def test_create_kit_name_with_spaces_in_name_get_success_response():
    positive_assert("A Aaa ")

def test_create_kit_3_numbers_like_string_in_name_get_success_response():
    positive_assert("123")

def test_create_kit_with_null_in_name_get_error_response():
    kit_body = { }
    negative_assert(kit_body)

def test_create_kit_with_numbers_in_name_get_error_response():
    response = sender_stand_request.post_new_user(data.user_body)
    token = response.json()['authToken']
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400

