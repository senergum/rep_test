import pytest
import subprocess
import os
import shutil
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