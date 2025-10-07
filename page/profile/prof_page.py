import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.base_page import BasePage
from config.utils.actions import ActionPage
from config.utils.asserts import AssertPage
from config.utils.reporter import ReportPage
from page.login.log_data import login_url
from page.profile.prof_data import (
    aster,
    set_main,
    nickname,
    nicknick,
    nichcheck,
    pochta
)
from page.profile.prof_locator import (
    prof_main,
    budu_smotret,
    ne_budu_smotret,
    smotru,
    ocenka,
    baje,
    copppy_prof,
    setings,
    k_pro,
    set_txt,
    meow,
    nick,
    save_stg,
    ima,
    backup_but,
    check,
    set_pers,
    backup
)
from page.login.log_locators import (logout)
import time

class ProfilePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.actions = ActionPage(driver)
        self.asserts = AssertPage(driver)
        self.report = ReportPage(driver)

    @allure.step("Главная страница профиля")
    def main(self):
        self.actions.click(prof_main)
        self.asserts.element_is_visible(logout)

    @allure.step("Кнопки взаимодействия с кино")
    def active_kino(self):
        self.actions.navigate(aster)
        self.asserts.url_is(aster)
        self.actions.scroll_to_element(ne_budu_smotret)
        self.actions.safe_click(ne_budu_smotret)
        self.asserts.element_is_enabled(ne_budu_smotret)
        time.sleep(0.3)
        self.actions.safe_click(budu_smotret)
        self.asserts.element_is_enabled(budu_smotret)
        time.sleep(0.3)
        self.actions.safe_click(smotru)
        self.asserts.element_is_enabled(smotru)
        time.sleep(0.3)
        self.actions.safe_click(ocenka)
        self.asserts.element_is_enabled(ocenka)
        self.actions.safe_click(ne_budu_smotret)
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(0.3)
        self.actions.safe_click(ne_budu_smotret)

    @allure.step("Бейджи")
    def baje(self):
        self.actions.click(prof_main)
        self.asserts.element_is_visible(logout)
        self.actions.click(baje)
        self.asserts.element_is_visible(k_pro)

    @allure.step("Копирование профиля")
    def copppy(self):
        self.actions.click(prof_main)
        self.asserts.element_is_visible(logout)
        self.actions.click(copppy_prof)
        self.asserts.assert_tooltip_activated(copppy_prof)

    @allure.step("Настройки")
    def setings(self):
        self.actions.click(prof_main)
        self.asserts.element_is_visible(logout)
        self.actions.click(setings)
        self.asserts.element_is_visible(set_txt)

    @allure.step("Основные настройки")
    def setingsCheck(self):
        self.actions.navigate(set_main)
        self.asserts.url_is(set_main)
        self.actions.scroll_to_element(meow)
        self.actions.click(meow)
        self.asserts.checkbox_is_active(meow)
        self.actions.click(meow)

    @allure.step("Персональные настройки")
    def setingsNick(self):
        self.actions.navigate(set_main)
        self.asserts.url_is(set_main)
        self.actions.click(set_pers)
        self.actions.fill_posled(nick, nickname)
        self.actions.click(save_stg)
        self.actions.navigate(login_url)
        self.actions.click(prof_main)
        self.actions.navigate(set_main)
        self.actions.click(set_pers)
        self.asserts.assert_value_is(nick, nichcheck)
        self.actions.fill_posled(nick, nicknick)
        self.actions.click(save_stg)

    @allure.step("бэкап настройки")
    def setingsback(self):
        self.actions.navigate(login_url)
        self.actions.navigate(set_main)
        self.asserts.url_is(set_main)
        self.actions.click(backup)
        self.actions.click(backup_but)
        self.asserts.element_contains_text(check, pochta)