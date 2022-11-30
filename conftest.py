import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    if user_language is not None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError('--language should contain language.')

    yield browser
    browser.quit()
