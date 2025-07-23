from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger import get_logger


class AssertPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)  # 5 секунд по умолчанию
        self.logger = get_logger(self.__class__.__name__)

    def url_is(self, expected_url: str):
        """Проверяет, что текущий URL страницы точно совпадает с ожидаемым"""
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Ожидали URL: {expected_url}, получили: {actual_url}"
        self.logger.info(f"URL соответствует ожидаемому: {expected_url}")

    def title_is(self, expected_title: str):
        """Проверяет, что заголовок (title) страницы соответствует ожидаемому"""
        actual_title = self.driver.title
        assert actual_title == expected_title, f"Ожидали title: {expected_title}, получили: {actual_title}"
        self.logger.info(f"Заголовок страницы соответствует: {expected_title}")

    def element_is_visible(self, locator: tuple):
        """Проверяет, что элемент отображается (не скрыт) на странице"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        assert element.is_displayed(), f"Элемент {locator} должен быть видим"
        self.logger.info(f"Элемент {locator} виден на странице")

    def element_is_hidden(self, locator: tuple):
        """Проверяет, что элемент скрыт (display: none или не существует в DOM)"""
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            assert not element.is_displayed(), f"Элемент {locator} должен быть скрыт"
        except:
            pass  # Элемент не найден - значит скрыт
        self.logger.info(f"Элемент {locator} скрыт на странице")

    def element_contains_text(self, locator: tuple, expected_text: str):
        """Проверяет, что элемент содержит указанный текст (частично)"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actual_text = element.text
        assert expected_text in (actual_text or ""), f"Элемент {locator} не содержит текст: {expected_text}"
        self.logger.info(f"Элемент {locator} содержит текст: {expected_text}")

    def element_text_is(self, locator: tuple, expected_text: str):
        """Проверяет, что текст элемента полностью соответствует ожидаемому"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actual_text = element.text
        assert actual_text == expected_text, f"Ожидали текст '{expected_text}', получили: '{actual_text}'"
        self.logger.info(f"Текст элемента {locator} точно соответствует: {expected_text}")

    def element_has_attribute(self, locator: tuple, attr: str, expected_value: str):
        """Проверяет, что значение указанного атрибута элемента соответствует ожидаемому"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        actual_value = element.get_attribute(attr)
        assert actual_value == expected_value, f"Атрибут '{attr}' должен быть '{expected_value}', получено: '{actual_value}'"
        self.logger.info(f"Атрибут '{attr}' элемента {locator} равен: {expected_value}")

    def element_has_class(self, locator: tuple, class_name: str):
        """Проверяет, что элемент содержит указанный CSS класс"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        classes = element.get_attribute("class") or ""
        assert class_name in classes.split(), f"Элемент {locator} не содержит класс: {class_name}"
        self.logger.info(f"Элемент {locator} содержит класс: {class_name}")

    def element_is_enabled(self, locator: tuple):
        """Проверяет, что элемент активен (не отключен)"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        assert element.is_enabled(), f"Элемент {locator} должен быть активен"
        self.logger.info(f"Элемент {locator} активен (не disabled)")

    def element_is_disabled(self, locator: tuple):
        """Проверяет, что элемент отключён (disabled)"""
        element = self.wait.until(EC.presence_of_element_located(locator))
        assert not element.is_enabled(), f"Элемент {locator} должен быть отключён"
        self.logger.info(f"Элемент {locator} отключён (disabled)")

    def element_count_is(self, locator: tuple, expected_count: int):
        """Проверяет, что количество найденных элементов по локатору совпадает с ожидаемым"""
        elements = self.driver.find_elements(*locator)
        count = len(elements)
        assert count == expected_count, f"Ожидали {expected_count} элементов {locator}, получили: {count}"
        self.logger.info(f"Найдено {count} элементов {locator} (ожидалось: {expected_count})")

    def element_position_in_list_has_text(
            self,
            list_selector: tuple,
            position: int,
            expected_text: str,
            item_selector: str = "> div.inventory_item"):
        """Проверяет, что элемент в указанной позиции списка содержит заданный текст"""
        # Конвертируем кортеж локатора в строку для CSS селектора
        by, selector = list_selector
        if by != By.CSS_SELECTOR:
            raise ValueError("Метод element_position_in_list_has_text работает только с CSS_SELECTOR")
        name_locator = (By.CSS_SELECTOR,
                        f"{selector} {item_selector}:nth-child({position}) .inventory_item_name")
        self.element_text_is(name_locator, expected_text)