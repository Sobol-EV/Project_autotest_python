import time

import allure
import pytest
import pytest_check as check

from ui import base
from generators.registration_data import BuilderRegData
from mysql.models import TestUsersModel
from ui.pages.registration_page import RegistrationPage


class TestLoginPage(base.BaseCase):
    """AUTH. """

    authorize = False

    @pytest.mark.UI
    @allure.title("Successful authorization.")
    def test_successful_authorization(self):
        """AUTH_001. Successful authorization"""
        response_data = self.builder.create_new_user(1, 0)

        response_data = response_data['user_data']
        login = response_data['username']
        password = response_data['password']

        self.login_page.authorization(login, password)
        self.driver.refresh()
        assert self.welcome_page.is_opened(), \
            "Authorization failed"

    @pytest.mark.UI
    # @pytest.mark.xfail(resolve="БАГ: Уведомление не пропадает")
    @allure.title("Failed authorization.")
    def test_negative_authorization(self):
        """AUTH_002. Failed authorization"""
        user_data = BuilderRegData().build()
        self.login_page.authorization(
            user_data["username"],
            user_data["password"]
        )
        assert self.login_page.is_opened(), \
            "Login page not open"
        assert self.login_page.visibility_element(
            self.login_page.locators.LOGIN_ALERT
        ), "Alert not visible"
        assert self.login_page.compare_text_elements(
            self.login_page.locators.LOGIN_ALERT,
            self.login_page.TEXT_ALERT_LOGIN_INCORRECT
        ), "Text is alert incorrect"
        self.driver.refresh()
        check.is_false(self.login_page.visibility_element(
            self.login_page.locators.LOGIN_ALERT,
            "Alert not gone"
        ))

    @pytest.mark.UI
    # @pytest.mark.xfail(resolve="БАГ: отсутствует название страницы.")
    @allure.title("""Checking for the presence and correctness of
        all text elements and icons (except for hyperlinks)""")
    def test_element_presence(self):
        """
        AUTH_003. Checking for the presence and correctness of
        all text elements and icons (except for hyperlinks).
        """
        assert self.base_page.is_opened(), \
            "Login page not open"
        check.is_true(self.login_page.check_title(), "Page has no title")
        check.is_true(
            self.login_page.compare_text_elements(
                self.login_page.locators.LOGIN_FORM_HEADER,
                self.login_page.LOGIN_FORM_HEADER
            ), "Authorization form header incorrect"
        )
        for field in self.login_page.LIST_FIELD:
            check.is_true(
                self.login_page.visibility_element(
                    field["locator_icon_field"]
                ), f"{field['name_field']} field icon incorrect"
            )
            check.equal(
                self.login_page.get_value_attribute(
                    field['locator'], "placeholder"
                ), field['name_field'],
                f"Field name {field['name_field']} incorrect"
            )
        check.equal(
            self.login_page.get_value_attribute(
                self.login_page.locators.LOGIN_BUTTON_INPUT, "value"
            ), self.login_page.SUBMIT_LOGIN_VALUE,
            "The text in the login button is incorrect"
        )
        check.is_true(
            self.login_page.check_copyright(), "Copyright incorrect"
        )

    @pytest.mark.UI
    # @pytest.mark.xfail(resolve="БАГ: Нет ограничений длины макс. и мин у поля с паролем.")
    @allure.title("Validation of login and password fields is checked.")
    def test_field_restrictions(self):
        """AUTH_004. Validation of login and password fields is checked"""
        assert self.base_page.is_opened(), \
            "Login page not open"
        for field in self.login_page.LIST_FIELD:
            for restriction in self.login_page.LIST_RESTRICTIONS:
                result_checking = self.login_page.check_all_field_restrictions(
                    field["locator"], restriction, field[restriction],
                    field['name_field'], field['required']
                )
                check.is_true(
                    result_checking['result'], result_checking['reason']
                )

    @pytest.mark.UI
    @allure.title("""The text before the hyperlink, the text of the hyperlink and
        the correct operation of the hyperlink are checked""")
    def test_hyperlink_relevance(self):
        """
        AUTH_005. The text before the hyperlink, the text of the hyperlink and
        the correct operation of the hyperlink are checked.
        """
        assert self.base_page.is_opened(), \
            "Login page not open"
        assert self.login_page.compare_text_elements(
            self.login_page.locators.TEXT_NO_REGISTERED,
            self.login_page.TEXT_NO_REGISTERED
        ), "Text before hyperlink is invalid"
        assert self.login_page.compare_text_elements(
            self.login_page.locators.HYPERLINK_CREATE_ACCOUNT,
            self.login_page.TEXT_HYPERLINK_CREATE_ACCOUNT
        ), "Hyperlink text is invalid"
        self.login_page.click(
            self.login_page.locators.HYPERLINK_CREATE_ACCOUNT
        )
        assert self.registration_page.is_opened(), \
            "Registration page not open"


class TestRegistrationPage(base.BaseCase):

    authorize = False

    @pytest.mark.UI
    @pytest.mark.xfail(resolve=
                       "БАГ: Отсутствие валидации на UI поля Middle name"
                       "Превышение верхней границы количества символов, у поля Surname"
                       "Отсутствие валидации на UI поля Password"
                       "Отсутствие валидации на UI поля Repeat password"
                       )
    @allure.title("Validating fields on the registration page.")
    def test_field_restrictions(self):
        """REG_001. Validating fields on the registration page"""
        self.login_page.go_to_url(self.registration_page.URL)
        self.registration_page.visibility_element(
            self.registration_page.locators.REGISTRATION_FORM
        )
        for field in self.registration_page.LIST_FIELD:
            for restriction in self.registration_page.LIST_RESTRICTIONS:
                result_checking = self.registration_page.check_all_field_restrictions(
                    field["locator"], restriction, field[restriction],
                    field['name_field'], field['required']
                )
                check.is_true(
                    result_checking['result'], result_checking['reason']
                )

    @pytest.mark.UI
    @pytest.mark.xfail(resolve="БАГ: Ошибка в placeholder middle name")
    @allure.title("Checking field names placeholder")
    def test_placeholder_field(self):
        """REG_002. Checking field names placeholder"""
        self.login_page.go_to_url(self.registration_page.URL)
        self.registration_page.visibility_element(
            self.registration_page.locators.REGISTRATION_FORM
        )
        for field in self.registration_page.LIST_FIELD:
            check.equal(
                self.registration_page.get_value_attribute(
                    field["locator"], "placeholder"
                ),
                field["name_field"],
                f"The field {field['name_field']} is invalid placeholder."
            )

    @pytest.mark.UI
    @allure.title("Checking field icons")
    def test_icon_field(self):
        """REG_003. Checking field icons"""
        self.login_page.go_to_url(self.registration_page.URL)
        self.registration_page.visibility_element(
            self.registration_page.locators.REGISTRATION_FORM
        )
        for field in self.registration_page.LIST_FIELD:
            check.is_true(
                self.registration_page.visibility_element(field["icon_field"]),
                f"{field['name_field']} field icon missing"
            )

    @pytest.mark.UI
    @allure.title("Checking all text elements.")
    def test_text_in_elements(self):
        """REG_004. Checking all text elements"""
        self.login_page.go_to_url(self.registration_page.URL)
        check.is_true(self.login_page.check_title(), "Page has no title")
        self.registration_page.visibility_element(
            self.registration_page.locators.REGISTRATION_FORM
        )
        for text_element in self.registration_page.LIST_TEXT_ELEMENT:
            check.is_true(
                self.registration_page.compare_text_elements(
                    text_element["locator"],
                    text_element["expected"]
                ), text_element["error_message"]
            )
        check.is_true(
            self.registration_page.check_copyright(), "Copyright incorrect"
        )

    @pytest.mark.UI
    @allure.title("Hyperlink Check.")
    def test_hyperlinks_log_in(self):
        """REG_005. Hyperlink Check"""
        self.login_page.go_to_url(self.registration_page.URL)
        self.registration_page.visibility_element(
            self.registration_page.locators.REGISTRATION_FORM
        )
        self.registration_page.click(
            self.registration_page.locators.HYPERLINK_LOG_IN
        )
        self.login_page.is_opened()

    @pytest.mark.UI
    # @pytest.mark.xfail(resolve="БАГ: Нет заполняется поле Middle name, "
    #                            "не проставляется флаг активности и время "
    #                            "начала активности")
    @allure.title("Successful registration.")
    def test_successful_registration(self):
        """REG_006. Successful registration"""
        self.login_page.go_to_url(self.registration_page.URL)
        user_data = BuilderRegData().build()
        self.registration_page.registration(user_data)
        self.driver.refresh()
        self.welcome_page.is_opened()
        check.is_true(
            self.welcome_page.check_username(user_data["username"]),
            "Username does not match the one specified during registration"
            )
        check.is_true(
            self.welcome_page.check_full_name(
                user_data["name"], user_data["surname"], user_data["middle_name"]
            ),
            "Full name does not match those specified during registration"
        )
        self.mysql.session.commit()
        res = self.mysql.session.query(TestUsersModel)
        res = res.all()[0]
        user_data.pop("confirm")
        for key in user_data.keys():
            check.equal(
                eval(f"res.{key}"),
                user_data[key],
                f"The {key} field is not in the database"
            )
        check.is_true(
            res.active, "The user has not been set an active flag"
        )
        check.is_not_none(
            res.start_active_time,
            "The user has not been set the start time of the activity"
        )

    @pytest.mark.UI
    @pytest.mark.xfail(resolve="БАГ: Уведомление не пропало при обновлении страницы")
    @allure.title("Failed registration.")
    @pytest.mark.parametrize(
        "user_data,error_message", [
            (  # REG_007.  1. Error different passwords
                    BuilderRegData().set_repeat_password(
                        equals=False, alphabet=BuilderRegData.alf_english
                    ).build(), RegistrationPage.ERROR_MESSAGE_PASS_MUST_MATCH),
            (  # REG_008.  2. Incorrect email error
                    BuilderRegData().set_email(
                        type_email=False
                    ).build(), RegistrationPage.ERROR_MESSAGE_INVALID_EMAIL)
        ])
    def test_failed_registration(self, user_data, error_message):
        self.login_page.go_to_url(self.registration_page.URL)
        self.registration_page.registration(user_data)
        check.is_true(
            self.registration_page.check_alert(),
            "Alert did not appear"
        )
        check.is_true(self.registration_page.check_alert_message(
            error_message
        ), "Alert message is incorrect")
        check.is_true(self.registration_page.invisible_with_time_element(
            self.registration_page.locators.ALERT_REGISTRATION_FORM, 5
        ), "The Alert didn't go away after showing")
        self.driver.refresh()
        check.is_false(self.registration_page.visibility_element(
            self.registration_page.locators.ALERT_REGISTRATION_FORM,
            "Alert not gone"
        ))

    @pytest.mark.UI
    @pytest.mark.xfail(resolve="БАГ: Уведомление не пропало при обновлении страницы")
    @allure.title("""""Checking registration with incorrect
        email and mismatched passwords.""")
    def test_failed_registration_several_alert(self):
        """
        REG_009. Checking registration with incorrect
        email and mismatched passwords.
        """
        self.login_page.go_to_url(self.registration_page.URL)
        user_data = BuilderRegData().set_email(type_email=False).set_repeat_password(
            equals=False, alphabet=BuilderRegData.alf_english
        ).build()
        self.registration_page.registration(user_data)
        assert self.registration_page.count_alert() == 2, \
            "Wrong number of warnings"
        check.is_true(self.registration_page.check_alert_message(
            self.registration_page.ERROR_MESSAGE_INVALID_EMAIL
        ), "Alert message is incorrect")
        check.is_true(self.registration_page.check_alert_message(
            self.registration_page.ERROR_MESSAGE_PASS_MUST_MATCH
        ), "Alert message is incorrect")
        check.is_true(self.registration_page.invisible_with_time_element(
            self.registration_page.locators.ALERT_REGISTRATION_FORM, 5
        ), "The Alert didn't go away after showing")
        self.driver.refresh()
        check.is_false(self.registration_page.visibility_element(
            self.registration_page.locators.ALERT_REGISTRATION_FORM,
            "Alert not gone"
        ))

    @pytest.mark.UI
    @allure.title("""Checking registration for an already taken email.""")
    def test_failed_registration_two_accounts_per_email(self):
        """
        REG_010. Checking registration for an already taken email
        """
        self.login_page.go_to_url(self.registration_page.URL)
        response_data = self.builder.create_new_user(1, 0)
        response_data = response_data['user_data']

        user_data = BuilderRegData().set_email(
            email=response_data["email"]
        ).build()
        self.registration_page.registration(user_data)
        print(self.registration_page.check_alert_message(
            self.registration_page.ERROR_MESSAGE_ALREADY_EMAIL
        ))
        check.is_true(self.registration_page.check_alert_message(
            self.registration_page.ERROR_MESSAGE_ALREADY_EMAIL
        ), "Alert message is incorrect")
        check.is_true(self.registration_page.invisible_with_time_element(
            self.registration_page.locators.ALERT_REGISTRATION_FORM, 5
        ), "The Alert didn't go away after showing")
        self.driver.refresh()
        time.sleep(5)
        check.is_false(self.registration_page.visibility_element(
            self.registration_page.locators.ALERT_REGISTRATION_FORM,
            "Alert not gone"
        ))

    @pytest.mark.UI
    @allure.title("""Checking registration for an already taken username.""")
    def test_failed_registration_two_accounts_per_username(self):
        """
        REG_011. Checking registration for an already taken username
        """
        self.login_page.go_to_url(self.registration_page.URL)
        response_data = self.builder.create_new_user(1, 0)
        response_data = response_data['user_data']

        user_data = BuilderRegData().set_username(
            username=response_data['username']
        ).build()

        self.registration_page.registration(user_data)
        print(self.registration_page.check_alert_message(
            self.registration_page.ERROR_MESSAGE_ALREADY_USERNAME
        ))
        check.is_true(self.registration_page.check_alert_message(
            self.registration_page.ERROR_MESSAGE_ALREADY_USERNAME
        ), "Alert message is incorrect")
        check.is_true(self.registration_page.invisible_with_time_element(
            self.registration_page.locators.ALERT_REGISTRATION_FORM, 5
        ), "The Alert didn't go away after showing")
        self.driver.refresh()
        time.sleep(5)
        check.is_false(self.registration_page.visibility_element(
            self.registration_page.locators.ALERT_REGISTRATION_FORM,
            "Alert not gone"
        ))
