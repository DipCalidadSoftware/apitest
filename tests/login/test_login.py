import json
import pytest
import requests
import logging

logger = logging.getLogger(__name__)

from src.assertions.login_assertions import assert_login_succesfuly, assert_login_schema, assert_login_schema_file
from config import BASE_URI
import jsonschema


# functional SMOKE Verificar un login exitoso con credenciales validos      200 ok
# functional SMOKE Verificar un login credencialess errones username, pwd     401
# not automated # functional Verificar el bloqueo de la cuenta  403
# functional Verificar si envio usuario sin password       400
# functional Verificar  que le mande parametros adicionales perfil  400
# functional Verificar  que le mande header content type application/json perfil  400


@pytest.mark.smoke
def test_login_exitoso_credenciales_validos(get_token_login):
    response_data = get_token_login
    print(response_data)
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
            "jwt_tokllllllen": {
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
        jsonschema.validate(instance=response_data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        pytest.fail(f"JSON schema dont match {err}")
    assert response_data["token_type"] is not None
    assert response_data["jwt_token"] is not None


@pytest.mark.smoke1
@pytest.mark.xfail(reason="known parser issue", run=False)
def test_login_credenciales_erroneas():
    url = f'{BASE_URI}/wp-json/api/v1/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = "username=auto&password=apitesdddddt01."
    response = requests.post(url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 400
    assert response_data["error"] == "INVALID_CREDENTIALS"


@pytest.mark.smoke1
def test_login_exitoso_credenciales_validos_mejorado(get_token_login):
    response_data = get_token_login
    assert assert_login_schema(response_data) == True
    assert_login_succesfuly(response_data)




@pytest.mark.smoke1
def test_login_exitoso_credenciales_validos_mejoradisimo(get_token_login):
    response_data = get_token_login
    logger.debug("Sfsfsdfsfd")
    assert assert_login_schema_file(response_data) == True
    assert_login_succesfuly(response_data)