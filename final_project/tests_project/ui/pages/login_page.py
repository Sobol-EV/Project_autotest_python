from urllib.parse import urljoin

import allure

from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators
import restrictions


class LoginPage(BasePage):

    URL = urljoin(BasePage.URL, "/login")
    locators = LoginPageLocators()

    LOGIN_FORM_HEADER = "Welcome to the TEST SERVER"
    PLACEHOLDER_LOGIN_INPUT = "Username"
    PLACEHOLDER_PASSWORD_INPUT = "Password"
    SUBMIT_LOGIN_VALUE = "Login"
    TEXT_ALERT_LOGIN_INCORRECT = "Invalid username or password"
    TEXT_NO_REGISTERED = "Not registered?"
    TEXT_HYPERLINK_CREATE_ACCOUNT = "Create an account"

    LIST_FIELD = [
        {
            "locator": locators.LOGIN_INPUT_FIELD,
            "minlength": restrictions.MIN_LENGTH_USERNAME,
            "maxlength": restrictions.MAX_LENGTH_USERNAME,
            "name_field": PLACEHOLDER_LOGIN_INPUT,
            "locator_icon_field": locators.LOGIN_ICON_USERNAME,
            "required": True
        },
        {
            "locator": locators.PASSWORD_INPUT_FIELD,
            "minlength": restrictions.MIN_LENGTH_PASSWORD,
            "maxlength": restrictions.MAX_LENGTH_PASSWORD,
            "name_field": PLACEHOLDER_PASSWORD_INPUT,
            "locator_icon_field": locators.LOGIN_ICON_PASSWORD,
            "required": True
        }]

    @allure.step("Authorization.")
    def authorization(self, username, password):
        self.visibility_element(self.locators.LOGIN_FORM)
        self.fill_field(username, self.locators.LOGIN_INPUT_FIELD)
        self.fill_field(password, self.locators.PASSWORD_INPUT_FIELD)
        self.visibility_element(self.locators.LOGIN_BUTTON_INPUT)
        self.click(self.locators.LOGIN_BUTTON_INPUT)

