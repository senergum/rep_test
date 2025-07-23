from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger import get_logger


class HelpPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)  # 5 секунд по умолчанию
        self.logger = get_logger(self.__class__.__name__)

    def get_attribute(self, locator: tuple, attr: str):
        """Получает значение указанного атрибута у элемента"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        value = element.get_attribute(attr)
        self.logger.info(f"Атрибут '{attr}' элемента {locator}: {value}")
        return value

    def has_class(self, locator: tuple, class_name: str):
        """Проверяет, содержит ли элемент определённый CSS класс"""
        class_attr = self.get_attribute(locator, "class")
        result = class_name in (class_attr or "").split()
        self.logger.info(f"Элемент {locator} содержит класс '{class_name}': {result}")
        return result

    def get_element_size(self, locator: tuple):
        """Получает ширину и высоту элемента"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        size = {
            "width": element.size["width"],
            "height": element.size["height"]
        }
        self.logger.info(f"Размер элемента {locator}: {size}")
        return size

    def get_element_position(self, locator: tuple):
        """Получает координаты элемента на странице"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        location = element.location
        position = (location["x"], location["y"])
        self.logger.info(f"Координаты элемента {locator}: {position}")
        return position

    def screenshot_element(self, locator: tuple, path: str):
        """Делает скриншот конкретного элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.screenshot(path)
        self.logger.info(f"Скриншот элемента {locator} сохраняется в: {path}")

    def wait_until_hidden(self, locator: tuple, timeout: int = 5):
        """Ожидает, пока элемент исчезнет со страницы (таймаут в секундах)"""
        self.logger.info(f"Ожидание, пока элемент {locator} исчезнет (таймаут {timeout} сек)")
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
        except:
            self.logger.warning(f"Элемент {locator} не исчез за {timeout} секунд")
            raise