import pytest
from page.login.log_page import LoginPage
from page.search.search_page import Search
from page.navigation.navi_page import NaviGation
from page.profile.prof_page import ProfilePage
import time

@pytest.mark.smoke
@pytest.fixture                                 # фикстура логин
def loginAuth(browser):
    loginAuth = LoginPage(browser)
    loginAuth.login()

@pytest.mark.smoke                           
def test_navigation(browser):                   # базовая навигация по сайту
    navigation = NaviGation(browser)
    navigation.navigation()

@pytest.mark.smoke
def test_main_win(browser):                     # переход на главную страницу
    main_win = NaviGation(browser)
    main_win.main_win()

@pytest.mark.smoke
def test_donate(browser):                        # Страница доната
    donate = Search(browser)
    donate.donate()

@pytest.mark.smoke
def test_search(browser):                       # поиск фильмов
    search_page = Search(browser)
    search_page.search()

"""Тест с ошибкой для скриншота"""
@pytest.mark.smoke                              # поиск фильма с ошибкой в названии
def test_errT(browser):
    search_errT = Search(browser)
    search_errT.errT()

@pytest.mark.smoke
def test_searchActor(browser):                  # поиск актёра
    search_actor = Search(browser)
    search_actor.searchActor()

@pytest.mark.smoke
def test_searchFilter(browser):                 # фильтры поиска
    search_filter = Search(browser)
    search_filter.searchFiltor()

@pytest.mark.smoke
def test_searchFilterCheck(browser):            # проверка чекбоксов
    search_filterCheck = Search(browser)
    search_filterCheck.searchFiltorCheck()

@pytest.mark.smoke
def test_premier(browser):                      # проверка раздела премьеры
    search_premier = Search(browser)
    search_premier.premier()

@pytest.mark.smoke
def test_reg(browser):                          # проверка регистрации
    reg_page = LoginPage(browser)
    reg_page.reg()

@pytest.mark.smoke
def test_login(browser):                        # проверка логина
    login_page = LoginPage(browser)
    login_page.login()

@pytest.mark.smoke
def test_profile(browser):               # переход на главную страницу профиля
    profile_page = ProfilePage(browser)
    profile_page.main()

@pytest.mark.smoke
def test_active_kino(browser):       # кнопки активности на странице с кино
    active = ProfilePage(browser)
    active.active_kino()

@pytest.mark.smoke  
def test_baje(browser):              # проверка бейджей в профиле
    baje = ProfilePage(browser)
    baje.baje()

@pytest.mark.smoke  
def test_copppy(browser):            # проверка копирования страницы
    copppy = ProfilePage(browser)
    copppy.copppy()

@pytest.mark.smoke  
def test_setings(browser):            # проверка перехода на страницу настпроек
    setiungs = ProfilePage(browser)
    setiungs.setings()

@pytest.mark.smoke  
def test_setingsCheck(browser):       # проверка чекбоксов в настройках
    setiungsCheck = ProfilePage(browser)
    setiungsCheck.setingsCheck()

@pytest.mark.smoke  
def test_setingsNick(browser):        # проверка изменения никнейма
    setiungsNick = ProfilePage(browser)
    setiungsNick.setingsNick()
    time.sleep(1)

@pytest.mark.smoke  
def test_setingsback(browser):        # проверка отправки бэкапа на почту
    setiungsback = ProfilePage(browser)
    setiungsback.setingsback()

@pytest.mark.smoke
def test_logout(browser):                       # првоерка логаута
    logout_page = LoginPage(browser)
    logout_page.logout()
