from urllib.parse import urljoin

import allure

from ui.pages.base_page import BasePage
from ui.locators.registration_locators import RegistrationPageLocators
import restrictions


class RegistrationPage(BasePage):

    URL = urljoin(BasePage.URL, "/reg")
    locators = RegistrationPageLocators()

    HEADER_FORM = "Registration"
    PLACEHOLDER_NAME_INPUT = "Name"
    PLACEHOLDER_SURNAME_INPUT = "Surname"
    PLACEHOLDER_MIDDLE_NAME_INPUT = "Middle name"
    PLACEHOLDER_USERNAME_INPUT = "Username"
    PLACEHOLDER_EMAIL_INPUT = "Email"
    PLACEHOLDER_PASSWORD_INPUT = "Password"
    PLACEHOLDER_CONFIRM_INPUT = "Repeat password"
    REGISTRATION_RULES = "I accept that I want to be a SDET"
    REGISTRATION_TEXT_BUTTON = "Register"
    ALREADY_HAVE_ACCOUNT = "Already have an account?"
    TEXT_HYPERLINK_LOG_IN = "Log in"
    ERROR_MESSAGE_PASS_MUST_MATCH = "Passwords must match"
    ERROR_MESSAGE_INVALID_EMAIL = "Invalid email address"
    ERROR_MESSAGE_ALREADY_EMAIL = "This email address is already in use"
    ERROR_MESSAGE_ALREADY_USERNAME = "User already exist"

    LIST_TEXT_ELEMENT = [
        {
            "locator": locators.REGISTRATION_FORM_HEADER,
            "expected": HEADER_FORM,
            "error_message": "The title of the registration form is not correct"
        },
        {
            "locator": locators.TEXT_AGREEING_RULES,
            "expected": REGISTRATION_RULES,
            "error_message": "The text of the rules is not correct"
        },
        {
            "locator": locators.REGISTER_SUBMIT_INPUT,
            "expected": REGISTRATION_TEXT_BUTTON,
            "error_message": "Registration button text is not correct"
        },
        {
            "locator": locators.TEXT_ALREADY_HAVE_ACCOUNT,
            "expected": ALREADY_HAVE_ACCOUNT,
            "error_message": "The text before the hyperlink is incorrect"
        },
        {
            "locator": locators.HYPERLINK_LOG_IN,
            "expected": TEXT_HYPERLINK_LOG_IN,
            "error_message": "The text in the hyperlink is not correct"
        }
    ]

    LIST_FIELD = [
        {
            "locator": locators.NAME_INPUT_FIELD,
            "minlength": restrictions.MIN_LENGTH_NAME,
            "maxlength": restrictions.MAX_LENGTH_NAME,
            "name_field": PLACEHOLDER_NAME_INPUT,
            "icon_field": locators.ICON_NAME_INPUT,
            "required": True
         },
        {
            "locator": locators.SURNAME_INPUT_FIELD,
            "minlength": restrictions.MIN_LENGTH_SURNAME,
            "maxlength": restrictions.MAX_LENGTH_SURNAME,
            "name_field": PLACEHOLDER_SURNAME_INPUT,
            "icon_field": locators.ICON_SURNAME_INPUT,
            "required": True
        },
        {
            "locator": locators.MIDDLE_NAME_INPUT_FIELD,
            "minlength": restrictions.MIN_LENGTH_MIDDLE_NAME,
            "maxlength": restrictions.MAX_LENGTH_MIDDLE_NAME,
            "name_field": PLACEHOLDER_MIDDLE_NAME_INPUT,
            "icon_field": locators.ICON_MIDDLE_NAME_INPUT,
            "required": False
        },
        {
            "locator": locators.USERNAME_INPUT_FIELD,
            "minlength": restrictions.MIN_LENGTH_USERNAME,
            "maxlength": restrictions.MAX_LENGTH_USERNAME,
            "name_field": PLACEHOLDER_USERNAME_INPUT,
            "icon_field": locators.ICON_USERNAME_INPUT,
            "required": True
        },
        {
            "locator": locators.EMAIL_INPUT_FIELD,
            "minlength": restrictions.MIN_LENGTH_EMAIL,
            "maxlength": restrictions.MAX_LENGTH_EMAIL,
            "name_field": PLACEHOLDER_EMAIL_INPUT,
            "icon_field": locators.ICON_EMAIL_INPUT,
            "required": True
        },
        {
            "locator": locators.PASSWORD_INPUT_FIELD,
            "minlength": restrictions.MIN_LENGTH_PASSWORD,
            "maxlength": restrictions.MAX_LENGTH_PASSWORD,
            "name_field": PLACEHOLDER_PASSWORD_INPUT,
            "icon_field": locators.ICON_PASSWORD_INPUT,
            "required": True
        },
        {
            "locator": locators.CONFIRM_PASSWORD_INPUT_FIELD,
            "minlength": restrictions.MIN_LENGTH_PASSWORD,
            "maxlength": restrictions.MAX_LENGTH_PASSWORD,
            "name_field": PLACEHOLDER_CONFIRM_INPUT,
            "icon_field": locators.ICON_CONFIRM_PASSWORD_INPUT,
            "required": True
        },
    ]

    @allure.step("Registration")
    def registration(self, user_data: dict, rules=True):
        self.visibility_element(self.locators.REGISTRATION_FORM)
        self.fill_field(user_data['name'], self.locators.NAME_INPUT_FIELD)
        self.fill_field(user_data['surname'], self.locators.SURNAME_INPUT_FIELD)
        if "middlename" in user_data.keys():
            self.fill_field(user_data['middlename'], self.locators.MIDDLE_NAME_INPUT_FIELD)
        self.fill_field(user_data['username'], self.locators.USERNAME_INPUT_FIELD)
        self.fill_field(user_data['email'], self.locators.EMAIL_INPUT_FIELD)
        self.fill_field(user_data['password'], self.locators.PASSWORD_INPUT_FIELD)
        self.fill_field(user_data['confirm'], self.locators.CONFIRM_PASSWORD_INPUT_FIELD)
        if rules:
            self.click(self.locators.CHECKBOX_AGREEING_RULES)
        self.click(self.locators.REGISTER_SUBMIT_INPUT)

    @allure.step("Checking the message in alert")
    def check_alert_message(self, message):
        result = True if self.compare_text_elements(
            self.locators.ALERT_REGISTRATION_FORM, message
        )(self.driver) else False
        print(self.compare_text_elements(
            self.locators.ALERT_REGISTRATION_FORM, message
        ))
        return result

    @allure.step("Checking for an alert.")
    def check_alert(self):
        result = True if self.visibility_element(
            self.locators.ALERT_REGISTRATION_FORM
        ) else False
        return result

    def count_alert(self):
        return self.len_elements(
            self.locators.ALERT_REGISTRATION_FORM
        )
