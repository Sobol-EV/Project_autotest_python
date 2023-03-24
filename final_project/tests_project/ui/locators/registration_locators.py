from selenium.webdriver.common.by import By
from ui.locators.base_locators import BasePageLocators


class RegistrationPageLocators(BasePageLocators):

    REGISTRATION_FORM = (By.XPATH, '//div[contains(@class, "uk-width-large")]')
    REGISTRATION_FORM_HEADER = (By.XPATH, '//h3[contains(@class, "uk-card-title")]')
    NAME_INPUT_FIELD = (By.XPATH, '//input[@id="user_name"]')
    ICON_NAME_INPUT = (By.XPATH, '//input[@id="user_name"]/preceding-sibling::*//*[local-name() = "svg"]')
    SURNAME_INPUT_FIELD = (By.XPATH, '//input[@id="user_surname"]')
    ICON_SURNAME_INPUT = (By.XPATH, '//input[@id="user_surname"]/preceding-sibling::*//*[local-name() = "svg"]')
    MIDDLE_NAME_INPUT_FIELD = (By.XPATH, '//input[@id="user_middle_name"]')
    ICON_MIDDLE_NAME_INPUT = (By.XPATH, '//input[@id="user_middle_name"]/preceding-sibling::*//*[local-name() = "svg"]')
    USERNAME_INPUT_FIELD = (By.XPATH, '//input[@id="username"]')
    ICON_USERNAME_INPUT = (By.XPATH, '//input[@id="username"]/preceding-sibling::*//*[local-name() = "svg"]')
    EMAIL_INPUT_FIELD = (By.XPATH, '//input[@id="email"]')
    ICON_EMAIL_INPUT = (By.XPATH, '//input[@id="email"]/preceding-sibling::*//*[local-name() = "svg"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@id="password"]')
    ICON_PASSWORD_INPUT = (By.XPATH, '//input[@id="password"]/preceding-sibling::*//*[local-name() = "svg"]')
    CONFIRM_PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@id="confirm"]')
    ICON_CONFIRM_PASSWORD_INPUT = (By.XPATH, '//input[@id="confirm"]/preceding-sibling::*//*[local-name() = "svg"]')
    CHECKBOX_AGREEING_RULES = (By.XPATH, '//input[@type="checkbox"]')
    TEXT_AGREEING_RULES = (By.XPATH, '//label[@class="uk-text-small"]')
    REGISTER_SUBMIT_INPUT = (By.XPATH, '//input[@id="submit"]')
    TEXT_ALREADY_HAVE_ACCOUNT = (By.XPATH, '//div[./a[@href="/login"]]')
    ALERT_REGISTRATION_FORM = (By.XPATH, '//div[@id="flash"]')
    HYPERLINK_LOG_IN = (By.XPATH, '//a[@href="/login"]')

