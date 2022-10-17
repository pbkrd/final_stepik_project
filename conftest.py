import time
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: chrome or firefox")


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    # time.sleep(30)
    browser.quit()


@pytest.fixture(scope="function")
def lang_option(request):
    return request.config.getoption("language")
