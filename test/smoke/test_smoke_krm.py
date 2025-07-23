import pytest
import allure

import pytest

@pytest.fixture
def reg_page(browser):
    return RegPage(browser)

@pytest.fixture
def autho_page(browser):
    return AuthoPage(browser)

@pytest.fixture
def reg_user(registration_page):
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "securepassword"
    }
    registration_page.register(user_data)
    return user_data

@pytest.fixture
def autho_user(authorization_page, registered_user):
    authorization_page.login(registered_user["username"], registered_user["password"])
    yield registered_user
    authorization_page.logout()