import pytest


@pytest.mark.smoke
def test_all_pages_are_listed(get_token_login):
    print(get_token_login)
    assert get_token_login is not None
