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
from page.login.log_data import (login_url, main_url)
from page.navigation.navi_data import (
    premier_url,
    all_films_url,
    serials_url,
    lenta_url,
    video_url
)
from page.navigation.navi_locator import (
    premier,
    all_films,
    serials,
    lenta,
    video,
    main_win
)
import time

class NaviGation(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.actions = ActionPage(driver)
        self.asserts = AssertPage(driver)
        self.report = ReportPage(driver)

    @allure.step("Навигация по сайту")
    def navigation(self):
        self.actions.navigate(login_url)
        self.asserts.url_is(login_url)
        self.actions.click(premier)
        self.wait
        self.asserts.url_is(premier_url)
        self.wait
        self.actions.click(all_films)
        self.asserts.url_is(all_films_url)
        self.wait
        self.actions.click(serials)
        self.asserts.url_is(serials_url)
        self.wait
        self.actions.click(lenta)
        self.asserts.url_is(lenta_url)
        self.wait
        self.actions.click(video)
        self.asserts.url_is(video_url)

    @allure.step("Возврат на главную")
    def main_win(self):
        self.actions.click(video)
        self.asserts.url_is(video_url)
        self.wait
        self.actions.click(main_win)
        self.asserts.url_is(main_url)
