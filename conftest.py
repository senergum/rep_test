import pytest
import subprocess
import os
import shutil
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Делает скриншот при падении теста"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Получаем драйвер из фикстуры
        driver = None
        for fixture_name in item.funcargs:
            if "browser" in fixture_name:
                driver = item.funcargs[fixture_name]
                break
        
        if driver is not None:
            # Делаем скриншот
            screenshot_path = f"allure-results/screenshot_{item.name}.png"
            driver.save_screenshot(screenshot_path)
            
            with open(screenshot_path, "rb") as file:
                allure.attach(
                    file.read(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG
                )

# ФИНАЛЬНАЯ ВЕРСИЯ - ТОЛЬКО ОЧИСТКА КЭША
def pytest_configure(config):
    """Очистка кэша pytest и allure перед тестами"""
    if os.path.exists('.pytest_cache'): 
        shutil.rmtree('.pytest_cache')
    if os.path.exists('allure-results'): 
        shutil.rmtree('allure-results')

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox", "edge"])
    parser.addoption(
        "--headless",
        action="store_true")

@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    print(f"[DEBUG] >>> browser_name = {browser_name}, headless = {headless}")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1360,768")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.set_window_size(1360, 768)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1280,720")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.set_window_size(1280, 720)

    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1280,720")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
        driver.set_window_size(1280, 720)

    else:
        raise ValueError(f"Неизвестный браузер: {browser_name}")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def pytest_sessionfinish(session, exitstatus):
    print("[INFO] Генерация Allure-отчета...")
    try:
        if not os.path.exists("allure-results"):
            print("[WARN] Папка allure-results не найдена. Отчёт не будет создан.")
            return
        subprocess.run(["allure", "generate", "allure-results", "-o", "allure-report", "--clean"], shell=True)
        subprocess.run(["allure", "open", "allure-report"], shell=True)
    except Exception as e:
        print(f"[ERROR] Ошибка при генерации или открытии Allure-отчёта: {e}")

def pytest_sessionstart(session):
    if not os.path.exists("allure-results"):
        os.makedirs("allure-results")