from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger import get_logger

HOME_URL = "https://ru.kinorium.com"


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.logger = get_logger(self.__class__.__name__)

    def goto_home(self):
        """Переходит на домашнюю страницу"""
        self.logger.info(f"Переход на домашнюю страницу: {HOME_URL}")
        self.driver.get(HOME_URL)
