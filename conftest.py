import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def browser():
    service = Service(executable_path='chromedriver.exe')
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=service, options=options)
    browser.set_window_size(1400, 1000)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
