import jsonschema
import pytest

from src.utils.load_resources import load_schema_resource


def assert_login_succesfuly(response):
    assert response["token_type"] is not None
    assert response["jwt_token"] is not None


def assert_login_schema(response):
    schema = {
        "type": "object",
        "properties": {
            "token_type": {
                "type": "string"
            },
            "iat": {
                "type": "integer"
            },
            "expires_in": {
                "type": "integer"
            },
            "jwt_token": {
                "type": "string"
            }
        },
        "required": [
            "token_type",
            "iat",
            "expires_in",
            "jwt_token"
        ]
    }
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")


def assert_login_schema_file(response):
    schema = load_schema_resource("login_schema.json")
    try:
        jsonschema.validate(instance=response, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")
