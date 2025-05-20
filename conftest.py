import pytest
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

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
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
        options.add_argument("--window-size=1920,1080")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Неизвестный браузер: {browser_name}")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()