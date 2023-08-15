import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, es, fr, ru, etc.")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--incognito")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nStart browser for test..")
    try:
        browser = webdriver.Chrome(executable_path='/path/to/updated/chromedriver', options=options)
    except Exception as e:
        print("Error during Chrome initialization:", e)
        raise
    yield browser
    print("\nQuit browser..")
    browser.quit()
