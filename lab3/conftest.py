import os
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


HEADLESS = False


@pytest.fixture
def browser():
    options = ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    driver.maximize_window()
    driver.implicitly_wait(2)

    yield driver

    driver.quit()
