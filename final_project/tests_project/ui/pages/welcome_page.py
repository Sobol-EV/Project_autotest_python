from urllib.parse import urljoin

from ui.pages.base_page import BasePage
from ui.locators.welcome_locators import WelcomePageLocators


class WelcomePage(BasePage):

    URL = urljoin(BasePage.URL, "/welcome/")
    locators = WelcomePageLocators()

    def check_username(self, username):
        text_info = "Logged as " + username
        return True if self.compare_text_elements(
            self.locators.HEADER_LOGIN_AS_INFO,
            text_info
        ) else False

    def check_full_name(self, name, surname, middle_name):
        text_info = "User: " + name + " " + surname + " " + middle_name
        return True if self.compare_text_elements(
            self.locators.HEADER_USER_INFO,
            text_info
        ) else False
