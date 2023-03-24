from selenium.webdriver.common.by import By
from ui.locators.base_locators import BasePageLocators


class LoginPageLocators(BasePageLocators):

    LOGIN_FORM = (By.XPATH, '//div[contains(@class, "uk-width-large")]')
    LOGIN_FORM_HEADER = (By.XPATH, '//h3[contains(@class, "uk-card-title")]')
    LOGIN_INPUT_FIELD = (By.XPATH, '//input[@id="username"]')
    LOGIN_ICON_USERNAME = (By.XPATH, '//span[contains(@uk-icon, "user")]//*[local-name() = "svg"]')
    PASSWORD_INPUT_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_ICON_PASSWORD = (By.XPATH, '//span[contains(@uk-icon, "lock")]//*[local-name() = "svg"]')
    LOGIN_BUTTON_INPUT = (By.XPATH, '//input[@id="submit"]')
    TEXT_NO_REGISTERED = (By.XPATH, '//div[contains(@class, "uk-text-small")]')
    HYPERLINK_CREATE_ACCOUNT = (By.XPATH, '//a[@href="/reg"]')
    LOGIN_ALERT = (By.XPATH, '//div[@id="flash"]')

