import os.path
import shutil
import sys

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from _pytest.fixtures import FixtureRequest
from api.client import ApiClient
from urls import LOCAL_BASE_URL, DOCKER_BASE_URL

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.welcome_page import WelcomePage
from ui.pages.registration_page import RegistrationPage


@pytest.fixture()
def driver(config, temp_dir):
    browser = config['browser']
    url = config['url']
    selenoid = config['selenoid']
    vnc = config['vnc']
    local_url = config['local_url']
    options = Options()
    options.add_experimental_option(
        "prefs", {
            "download.default_directory": temp_dir
        }
    )
    if selenoid:
        capabilities = {
            "browserName": "chrome",
            'version': '99.0',
        }
        if vnc:
            capabilities['enableVNC'] = True
        driver = webdriver.Remote(
            'http://selenoid:4444/wd/hub',
            options=options,
            desired_capabilities=capabilities,
        )
    elif browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def is_local(config):
    return config['local_url']


@pytest.fixture()
def base_page(driver):
    return BasePage(driver=driver, is_local=is_local)


@pytest.fixture()
def welcome_page(driver):
    return WelcomePage(driver=driver, is_local=is_local)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver=driver, is_local=is_local)


@pytest.fixture()
def registration_page(driver):
    return RegistrationPage(driver=driver, is_local=is_local)

@allure.step("Receiving cookies for authorization.")
@pytest.fixture(scope='session')
def cookies(config, credentials_user_unlock):
    cookies = []
    login, password = credentials_user_unlock
    if config['local_url']:
        api_client = ApiClient(LOCAL_BASE_URL, login, password)
    else:
        api_client = ApiClient(DOCKER_BASE_URL, login, password)
    api_client.authorize()
    cookies_dict = dict(api_client.session.cookies)
    for cookie_name in cookies_dict.keys():
        cookies.append(
            {
                "name": cookie_name,
                "value": cookies_dict[cookie_name]
            }
        )

    return cookies


@pytest.fixture(scope='function')
def auth(request: FixtureRequest, driver):
    cookies = request.getfixturevalue('cookies')
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

    return WelcomePage(driver=driver, is_local=is_local)

