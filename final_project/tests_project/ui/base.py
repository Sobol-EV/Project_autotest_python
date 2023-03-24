import os
import pytest
import allure
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.registration_page import RegistrationPage
from ui.pages.login_page import LoginPage
from ui.pages.welcome_page import WelcomePage
from mysql.MysqlBuilder import MysqlBuilder
from mysql.client import MysqlClient


class BaseCase:
    driver = None
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']} - {i['message']}\n")
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            driver.get_screenshot_as_file(screenshot_path)
            allure.attach.file(
                screenshot_path, 'failed.png', allure.attachment_type.PNG
            )
            with open(browser_logs, 'r') as f:
                allure.attach.file(
                    f.read(), 'test.log', allure.attachment_type.TEXT
                )

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest, mysql_client):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.mysql: MysqlClient = mysql_client
        self.builder: MysqlBuilder = MysqlBuilder(self.mysql)

        self.login_page: LoginPage = (request.getfixturevalue('login_page'))
        self.registration_page: RegistrationPage = (request.getfixturevalue('registration_page'))
        self.base_page: BasePage = (request.getfixturevalue('base_page'))
        self.welcome_page: WelcomePage = (request.getfixturevalue('welcome_page'))

        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

