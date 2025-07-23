import pytest
from page.login.log_page import LoginPage
from page.login.log_locators import (
    email_input,
    pass_input)

@pytest.mark.smoke
def test_reg(browser):
    reg_page = LoginPage(browser)
    reg_page.reg()

@pytest.mark.smoke
def test_login(browser):
    login_page = LoginPage(browser)
    login_page.login()

@pytest.mark.smoke
def test_logout(browser):
    logout_page = LoginPage(browser)
    logout_page.logout()