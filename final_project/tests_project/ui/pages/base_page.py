import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException)

from urls import LOCAL_BASE_URL, DOCKER_BASE_URL
from ui.locators import base_locators


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):

    locators = base_locators.BasePageLocators()
    URL = DOCKER_BASE_URL  # Переключатель
    COPYRIGHT_AND_DATE = "powered by VK Education © 2020 - 2023"

    LIST_RESTRICTIONS = ['maxlength', 'minlength']

    def __init__(self, driver, is_local):
        self.driver = driver
        self.is_local = is_local

    @allure.step("Open URL check")
    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if (self.driver.current_url == self.URL) or \
                    (self.driver.current_url == self.URL + "/"):
                return True
        raise PageNotOpenedExeption(
            f'{self.URL} did not open in {timeout} current url {self.driver.current_url}')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 15
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Click')
    def click(self, locator, timeout=None):
        try:
            self.find(locator, timeout=timeout)
            if self.visibility_element(locator):
                elem = self.wait(timeout).until(
                    EC.element_to_be_clickable(locator)
                )
                elem.click()
        except StaleElementReferenceException:
            time.sleep(1)
            self.click(locator)

    @allure.step('Filled the field with a value {query}).')
    def fill_field(self, query, locator):
        """Finds an element on the page and enters the desired query"""
        elem = self.find(locator)
        if self.visibility_element(locator):
            elem.clear()
            elem.send_keys(query)

    @allure.step('Displays the visibility of an element.')
    def visibility_element(self, locator, timeout=None):
        """Displays the visibility of an element"""
        try:
            elem = self.wait(timeout).until(
                    EC.visibility_of_all_elements_located(locator)
            )
            return elem
        except TimeoutException:
            return

    @allure.step('Is the element invisible?')
    def invisible_with_time_element(self, locator, timeout=None):
        try:
            elem = self.wait(timeout).until(
                    EC.invisibility_of_element_located(locator)
            )
            return elem
        except TimeoutException:
            return False

        return EC.invisibility_of_element_located(locator)

    @allure.step('Is the element invisible now.')
    def invisible_now_element(self, locator):
        elem = EC.invisibility_of_element_located(locator)
        if elem == True:
            return True
        else:
            return False

    @allure.step('Get attribute value.')
    def get_value_attribute(self, locator, attribute_name):
        self.visibility_element(locator)
        elem = self.driver.find_element(*locator)
        return elem.get_attribute(attribute_name)

    @allure.step('Get attribute value.')
    def compare_text_elements(self, locator, text):
        self.find(locator)
        return EC.text_to_be_present_in_element(locator, text)

    @allure.step('Attribute check {attribute_name}.')
    def check_attribute(self, locator, attribute_name):
        self.find(locator)
        return EC.element_attribute_to_include(locator, attribute_name)

    @allure.step('Field Restriction Check (Minimum).')
    def min_length_constraint_field(self, locator):
        return self.check_attribute(locator, "minlength")

    @allure.step('Checking field limits (maximum).')
    def max_length_constraint_field(self, locator):
        return self.check_attribute(locator, "maxlength")

    @allure.step('Сopyright check.')
    def check_copyright(self):
        return self.compare_text_elements(
            self.locators.COPYRIGHT_AND_DATE,
            self.COPYRIGHT_AND_DATE
        )

    @allure.step('Field {field_name} constraint check.')
    def check_restriction_required(
            self, locator, attr_name,
            field_name, required
    ):
        result = self.check_attribute(locator, attr_name)
        if result == required:
            return {
                "result": True,
                "reason": None
            }
        else:
            return {
                "result": False,
                "reason": f"The field {field_name} must be required"
            }

    @allure.step('Check restriction length - field {field_name}.')
    def check_restriction_length(
            self, locator, attr_name,
            attr_value, field_name
    ):
        restriction_values = self.get_value_attribute(locator, attr_name)
        if restriction_values:
            if int(restriction_values) == attr_value:
                return {
                    "result": True,
                    "reason": None
                }
            else:
                return {
                    "result": False,
                    "reason": f"The {attr_name} field {field_name} constraint has an invalid value"
                              f"Expected {attr_value} - current {restriction_values}"
                }
        else:
            return {
                "result": False,
                "reason": f"There is no constraint on the {attr_name} of the {field_name} field"
            }

    @allure.step('Checking all restrictions - field {field_name}.')
    def check_all_field_restrictions(
            self, locator, attr_name,
            attr_value, field_name, required
    ):
        if attr_name == "required":
            result = self.check_restriction_required(
                locator, attr_name, field_name, required
            )
            return result
        result = self.check_restriction_length(
            locator, attr_name, attr_value, field_name
        )
        return result

    @allure.step('Open URL: {url}.')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Count the number of elements.')
    def len_elements(self, locator):
        return len(self.driver.find_elements(*locator))

    @allure.step("Check page title.")
    def check_title(self):
        return True if self.driver.title != "" else False


