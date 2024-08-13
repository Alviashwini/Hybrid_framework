# common verification
# Headers
# HTTP Status code
# Data verification
# JSON schema
def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed ER! = AR"

def verify_response_key(key, expected_data):
    assert key == expected_data

def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed - key is non Empty" + key
    assert key > 0,  "Failed - key is greater than zero"


