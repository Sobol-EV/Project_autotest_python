from selenium.webdriver.common.by import By


class BasePageLocators:

    COPYRIGHT_AND_DATE = (By.XPATH, '//div[contains(@class, "uk-text")]//p[@style]')
    SVG = (By.XPATH, '//path')
