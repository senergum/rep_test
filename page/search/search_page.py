import allure
import pytest
from faker import Faker
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage
from config.utils.actions import ActionPage
from config.utils.asserts import AssertPage
from config.utils.reporter import ReportPage
import selenium.common.exceptions
from page.login.log_data import (login_url)
from page.search.search_locators import (
    search_in,
    search_sel,
    form_menu,
    gen_menu,
    coun_menu,
    vod_menu,
    f_ui_menu_f,
    f_ui_menu_m,
    f_ui_menu_s,
    el_fil_a,
    el_fil_m,
    el_fil_s,
    gen_act,
    coun_act,
    vod_act,
    fil_lang,
    fil_ser,
    fil_ser_off,
    gen_prem,
    coun_prem,
    years_prem
)
from page.search.search_data import (
    v_film,
    v_actor,
    s_url,
    s_v_url,
    v_film_err,
    prem_url
)
import time

class Search(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.actions = ActionPage(driver)
        self.asserts = AssertPage(driver)
        self.report = ReportPage(driver)

    @allure.step("Поиск кино")        
    def search(self):
        self.actions.navigate(login_url)
        self.asserts.url_is(login_url)
        self.actions.fill_posled(search_in, v_film)
        self.asserts.element_contains_text(search_sel, v_film)

    @allure.step("Поиск актёра")
    def searchActor(self):
        self.actions.navigate(login_url)
        self.asserts.url_is(login_url)
        self.actions.fill_posled(search_in, v_actor)
        self.asserts.element_contains_text(search_sel, v_actor)

    @allure.step("Фильтры")
    def searchFiltor(self):
        self.actions.navigate(s_url)
        self.asserts.url_is(s_url)
        self.actions.click(form_menu)
        self.actions.click(f_ui_menu_f)
        self.actions.click(form_menu)
        self.actions.click(f_ui_menu_m)
        self.actions.click(form_menu)
        self.actions.click(f_ui_menu_s)
        self.asserts.element_is_visible(el_fil_s)
        self.asserts.element_is_visible(el_fil_m)
        self.asserts.element_is_visible(el_fil_a)
        self.actions.click(gen_menu)
        self.asserts.element_is_enabled(gen_act)
        self.actions.click(coun_menu)
        self.asserts.element_is_enabled(coun_act)
        self.actions.click(vod_menu)
        self.asserts.element_is_enabled(vod_act)

    @allure.step("Чекбокс")
    def searchFiltorCheck(self):
        self.actions.navigate(s_v_url)
        self.asserts.url_is(s_v_url)
        self.actions.click(fil_ser)
        self.asserts.element_is_visible(fil_ser_off)
        self.actions.click(fil_lang)
        self.asserts.checkbox_is_inactive(fil_lang)

    @allure.step("Не прошедший тест")
    def errT(self):
        self.actions.navigate(login_url)
        self.asserts.url_is(login_url)
        self.actions.fill_posled(search_in, v_film_err)
        self.asserts.element_contains_text(search_sel, v_film)

    @allure.step("Премьеры")
    def premier(self):
        self.actions.navigate(prem_url)
        self.asserts.url_is(prem_url)
        self.actions.click(gen_prem)
        self.asserts.element_is_enabled(gen_prem)
        self.actions.click(coun_prem)
        self.asserts.element_is_enabled(coun_prem)
        self.actions.click(years_prem)
        self.asserts.element_is_enabled(years_prem)