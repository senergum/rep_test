from selenium.webdriver.remote.webdriver import WebDriver
from config.logger import get_logger
import allure


class ReportPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def attach_screenshot(self, name: str = "Screenshot"):
        """Прикрепляет скриншот к отчету Allure."""
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
        self.logger.info(f"Сделали скриншот {name}")