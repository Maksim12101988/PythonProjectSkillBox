# conftest.py
"""import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import logging

@pytest.fixture(scope="session")
def web_driver_setup(request):
    chrome_options = Options()
    chrome_options.binary_location = r'C:\\Users\\ezhov\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
    driver = webdriver.Chrome(options=chrome_options)

    def fin():
        print("\nТесты завершены. Браузер открыт.")
        # Здесь можно добавить дополнительные действия перед закрытием браузера

    request.addfinalizer(fin)
    return driver"""

# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def web_driver_setup(request):
    chrome_options = Options()
    chrome_options.binary_location = r'C:\\Users\\ezhov\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
    driver = webdriver.Chrome(options=chrome_options)

    def fin():
        print("\nТесты завершены. Браузер открыт.")
        # Здесь можно добавить дополнительные действия перед закрытием браузера

    request.addfinalizer(fin)
    return driver

def pytest_configure(config):
    pass
