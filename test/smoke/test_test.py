import pytest
from page.login.log_page import LoginPage
from page.login.log_locators import (
    email_input,
    pass_input)
from page.search.search_page import Search
from page.navigation.navi_page import NaviGation
import time

@pytest.mark.smoke
def test_navigation(browser):
    navigation = NaviGation(browser)
    navigation.navigation()

@pytest.mark.smoke
def test_main_win(browser):
    main_win = NaviGation(browser)
    main_win.main_win()

@pytest.mark.smoke
def test_search(browser):
    search_page = Search(browser)
    search_page.search()

@pytest.mark.smoke
def test_searchActor(browser):
    search_page = Search(browser)
    search_page.searchActor()

@pytest.mark.smoke
def test_searchFilter(browser):
    search_filter = Search(browser)
    search_filter.searchFiltor()

@pytest.mark.smoke
def test_searchFilterCheck(browser):
    search_filterCheck = Search(browser)
    search_filterCheck.searchFiltorCheck()

@pytest.mark.smoke
def test_premier(browser):
    search_premier = Search(browser)
    search_premier.premier()

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

"""Это в конце, это тест с ошибкой для скриншота"""
@pytest.mark.smoke
def test_errT(browser):
    search_errT = Search(browser)
    search_errT.errT()