import pytest


@pytest.fixture(scope='session')
def some_resource():
    print("entre al setup sesion")
    login = "soy login de la sesion"

    def some_teardown():
        print("borrar login de sesion")

    yield login
    some_teardown()

    return login


@pytest.mark.smoke
def test_all_pages_are_listed_session(some_resource):
    login = some_resource
    print(login)
    print("test_all_pages_are_listed_session")
    assert login is not None


@pytest.fixture(scope='function')
def some_resource_function():
    print("soy setup de funcion")
    token = "variable de funcion"

    def some_teardown_function():
        print("borrar token de funcion")

    yield token
    some_teardown_function()

    return token


@pytest.mark.smoke
def test_all_pages_are_listed_session_function(some_resource, some_resource_function):
    login = some_resource
    token = some_resource_function
    print(login)
    print(token)
    print("test_all_pages_are_listed_session_function")
    assert login is not None
    assert token is not None
