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
from page.login.log_locators import (
    goto_intAuth,
    auth_button,
    email_input,
    pass_input,
    login_button,
    log_elem,
    m_button,
    reg_button,
    input_email,
    input_lastname,
    input_name,
    input_pass,
    input_repass,
    gotovo,
    prevoshodno,
    logout)
from page.login.log_data import (
    name,
    user,
    password,
    login_url,
    repass,
    first_name,
    last_name,
    email)
import time

class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.actions = ActionPage(driver)
        self.asserts = AssertPage(driver)
        self.report = ReportPage(driver)

    @allure.step("Регистрируемся")
    def reg(self):
        self.actions.navigate(login_url)
        self.asserts.url_is(login_url)
        self.actions.click(auth_button)
        self.actions.click(reg_button)
        self.actions.fill_posled(input_name, first_name)
        self.actions.fill_posled(input_lastname, last_name)
        self.actions.fill_posled(input_email, email)
        self.actions.fill_posled(input_pass, repass)
        self.actions.fill_posled(input_repass, repass)
        self.asserts.element_is_visible(gotovo)
        self.actions.click(gotovo)
        self.asserts.element_is_visible(prevoshodno)
  
    @allure.step(f"Логин. Имя: {name}")
    def login(self, username=user, password=password):
        username = username if username is not None else user
        password = password if password is not None else password
        self.actions.navigate(login_url)
        self.actions.click(auth_button)
        self.actions.click(goto_intAuth)
        self.asserts.element_is_visible(email_input)
        self.asserts.element_is_visible(pass_input)
        self.asserts.element_is_visible(login_button)
        self.actions.fill_posled(email_input, username)
        self.actions.fill_posled(pass_input, password)
        self.actions.click(login_button)
        try:
            self.actions.wait_for_selector(m_button, timeout=2)
            self.actions.click(m_button)
        except selenium.common.exceptions.TimeoutException:
            pass
        self.actions.wait_for_selector(log_elem)
        self.report.attach_screenshot("Итоги логина")
        self.asserts.element_is_visible(log_elem)

    @allure.step("Выход из системы")
    def logout(self):
        self.actions.navigate(login_url)
        self.asserts.url_is(login_url)
        self.actions.click(log_elem)
        self.actions.wait_for_selector(logout)
        self.asserts.element_is_visible(logout)
        self.actions.click(logout)
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()
        self.actions.logger.info("Алерт подтвержден (нажато OK)")
        self.asserts.url_is(login_url)