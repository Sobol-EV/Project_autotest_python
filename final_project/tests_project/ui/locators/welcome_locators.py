from selenium.webdriver.common.by import By
from ui.locators.base_locators import BasePageLocators


class WelcomePageLocators(BasePageLocators):

    HEADER_LOGO_BUG_BUTTON = (By.XPATH, '//a[@href="/" and contains(@class, "uk-hidden-small")]')
    HEADER_HOME_BUTTON = (By.XPATH, '//li//a[@href="/"]')
    HEADER_PYTHON_BUTTON_LIST = (By.XPATH, '//li[./a[@href="https://www.python.org/"]]')
    HEADER_PYTHON_HISTORY = (By.XPATH, '//a[contains(@href, "History_of_Python")]')
    HEADER_PYTHON_ABOUT_FLASK = (By.XPATH, '//a[contains(@href, "flask")]')
    HEADER_LINUX_BUTTON_LIST = (By.XPATH, '//li[./a[text()="Linux"]]')
    HEADER_LINUX_CENTOS = (By.XPATH, '//a[contains(text(), "Centos")]')
    HEADER_NETWORK_BUTTON_LIST = (By.XPATH, '//li[./a[text()="Network"]]')
    HEADER_NETWORK_WIRESHARK_NEWS = (By.XPATH, '//a[contains(@href, "wireshark.org/news")]')
    HEADER_NETWORK_WIRESHARK_DOWNLOAD = (By.XPATH, '//a[contains(@href, "wireshark.org/#download")]')
    HEADER_NETWORK_TCPDUMP_EXAMPLES = (By.XPATH, '//a[contains(@href, "tcpdump-examples")]')
    HEADER_NETWORK_WIRESHARK_TEXT = (By.XPATH, '//a[contains(@href, "wireshark.org/news")]/ancestor::li[2]')
    HEADER_NETWORK_TCPDUMP_TEXT = (By.XPATH, '//a[contains(@href, "tcpdump-examples")]/ancestor::li[2]')
    HEADER_LOGIN_AS_INFO = (By.XPATH, '//li[contains(text(), "Logged")]')
    HEADER_USER_INFO = (By.XPATH, '//li[contains(text(), "User:")]')
    HEADER_VK_ID_INFO = (By.XPATH, '//li[contains(text(), "VK ID:")]')
    HEADER_LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
    BODY_API_BUTTON = (By.XPATH, '//a[contains(@href, "Application_programming_interface")]')
    BODY_API_TEXT = (By.XPATH, '//div[contains(text(), "API")]')
    BODY_INTERNET_BUTTON = (By.XPATH, '//a[contains(@href, "future-of-the-internet")]')
    BODY_INTERNET_TEXT = (By.XPATH, '//div[contains(text(), "Future")]')
    BODY_SMTP_BUTTON = (By.XPATH, '//a[contains(@href, "SMTP")]')
    BODY_SMTP_TEXT = (By.XPATH, '//div[contains(text(), "SMTP")]')
    FOOTER_QUOTE = (By.XPATH, '//div[contains(@class, "uk-text")]//p[1]')
