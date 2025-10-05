from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from config.logger import get_logger


class ActionPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)  # 5 секунд по умолчанию
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url):
        """Переходит на указанный URL"""
        self.logger.info(f"Переход по URL: {url}")
        self.driver.get(url)

    def click(self, locator):
        """Кликает по элементу с заданным локатором"""
        self.logger.info(f"Клик по элементу: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def fill(self, locator, text):
        """Заполняет поле с заданным локатором текстом"""
        self.logger.info(f"Заполнение поля {locator} текстом: {text}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def fill_posled(self, locator, text):
        """Заполняет поле с заданным локатором текстом, по одному символу"""
        self.logger.info(f"Заполнение поля {locator} текстом: {text}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        for char in text:
            element.send_keys(char)

    def select_option(self, locator, value):
        """Выбирает значение из селектора с выпадающим списком"""
        self.logger.info(f"Выбор значения '{value}' в селекторе {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_value(value)

    def wait_for_url(self, url):
        """Ждёт появления заданного URL"""
        self.logger.info(f"Ожидание загрузки URL: {url}")
        self.wait.until(EC.url_to_be(url))

    def hover(self, locator):
        """Наводит курсор мыши на элемент"""
        self.logger.info(f"Наведение на элемент: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def get_text(self, locator):
        """Получает текстовое содержимое элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        text = element.text
        self.logger.info(f"Получен текст из {locator}: {text}")
        return text

    def is_visible(self, locator):
        """Проверяет, виден ли элемент на странице"""
        try:
            visible = self.driver.find_element(*locator).is_displayed()
        except:
            visible = False
        self.logger.info(f"Элемент {locator} видим: {visible}")
        return visible

    def is_enabled(self, locator):
        """Проверяет, активен ли элемент (не disabled)"""
        try:
            enabled = self.driver.find_element(*locator).is_enabled()
        except:
            enabled = False
        self.logger.info(f"Элемент {locator} активен: {enabled}")
        return enabled

    def wait_for_selector(self, locator, timeout=5):
        """Ждёт появления элемента с заданным локатором (timeout в секундах)"""
        self.logger.info(f"Ожидание селектора {locator} в течение {timeout} секунд")
        custom_wait = WebDriverWait(self.driver, timeout)
        custom_wait.until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, locator, timeout=5):
        """Листаем до локатора"""
        self.logger.info(f"Пролистывание страницы до селектора {locator} в течение {timeout} секунд")
        custom_wait = WebDriverWait(self.driver, timeout)
        element = custom_wait.until(EC.presence_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

