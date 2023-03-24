import pytest
import allure
import pytest_check as check
from api.base import BaseApi
from api.error_classes import ResponseStatusCodeException
from api.input_data.api import InputData


class TestApiAddUserAuth(BaseApi):

    input_data = InputData()

    @pytest.mark.API
    @allure.title("Positive test for user creation and constraint check.")
    @pytest.mark.parametrize("user_data", input_data.positive_test_cases_add_user())
    def test_positive_cases(self, user_data, mysql_client):
        response = self.api_client_user_unlock.post_create_user(user_data, 201)
        check.equal(
            response.status_code, 201,
            f"Status code {response.status_code}, expected 201!"
        )
        response_db = mysql_client.get_created_user(username=user_data['username'])
        check.is_true(response_db, "User not created!")
        for key_user_data in user_data.keys():
            check.equal(
                user_data[key_user_data],
                eval(f"response_db.{key_user_data}"),
                f"Field value {key_user_data} transmitted incorrectly!"
            )
        if response_db:
            mysql_client.delete_user(username=user_data['username'])

    @pytest.mark.API
    @allure.title("Negative user creation test and constraint check.")
    @pytest.mark.parametrize("user_data", input_data.negative_test_cases_add_user())
    def test_negative_cases(self, user_data, mysql_client):
        response = self.api_client_user_unlock.post_create_user(user_data, 400)
        check.equal(
            response.status_code, 400,
            f"Status code {response.status_code}, expected 400!"
        )
        response_db = mysql_client.get_created_user(username=user_data['username'])
        check.is_false(response_db, "The user was created bypassing restrictions!")
        if response_db:
            mysql_client.delete_user(username=user_data['username'])

    @pytest.mark.API
    @allure.title("Negative test for creating a user with an already existing username.")
    def test_negative_username_already_use(self, mysql_client):
        user_data = self.input_data.user_username_already_use()
        response = self.api_client_user_unlock.post_create_user(user_data[0], 201)
        check.equal(
            response.status_code, 201,
            f"Status code {response.status_code}, expected 201!"
        )
        response = self.api_client_user_unlock.post_create_user(user_data[1], 400)
        check.equal(
            response.status_code, 400,
            f"Status code {response.status_code}, expected 201!"
        )
        response_db = mysql_client.get_created_user(email=user_data[1]["email"])
        check.is_false(response_db, "Created an entry with the same username!")
        if response_db:
            mysql_client.delete_user(username=user_data[1]['username'])
        mysql_client.delete_user(username=user_data[0]['username'])

    @pytest.mark.API
    @allure.title("Negative test for creating a user with an already existing email.")
    def test_negative_email_already_use(self, mysql_client):
        user_data = self.input_data.user_email_already_use()
        response = self.api_client_user_unlock.post_create_user(user_data[0], 201)
        check.equal(
            response.status_code, 201,
            f"Status code {response.status_code}, expected 201!"
        )
        response = self.api_client_user_unlock.post_create_user(user_data[1], 400)
        check.equal(
            response.status_code, 400,
            f"Status code {response.status_code}, expected 400!"
        )
        response_db = mysql_client.get_created_user(username=user_data[1]["username"])
        check.is_false(response_db, "Created an entry with the same email!")
        if response_db:
            mysql_client.delete_user(email=user_data['email'])
        mysql_client.delete_user(email=user_data[0]['email'])

    @pytest.mark.API
    @allure.title("Negative test for creating a user with a blocked account.")
    def test_negative_add_user_blocked_user(self, mysql_client):
        user_data = self.input_data.default_user()
        response = self.api_client_user_block.post_create_user(user_data[0], 401)
        check.equal(
            response.status_code, 401,
            f"Status code {response.status_code}, expected 401!"
        )
        response_db = mysql_client.get_created_user(username=user_data[0]["username"])
        check.is_false(response_db, "The user was created by a blocked user!")
        if response_db:
            mysql_client.delete_user(username=user_data[0]['username'])


class TestApiAddUserNoAuth(BaseApi):

    input_data = InputData()
    authorize = False

    @pytest.mark.API
    @allure.title("Negative test for creating a user without authorization.")
    def test_negative_add_user_no_auth(self, mysql_client):
        user_data = self.input_data.default_user()
        response = self.api_client_user_unlock.post_create_user(user_data[0], 401)
        check.equal(
            response.status_code, 401,
            f"Status code {response.status_code}, expected 401!"
        )
        response_db = mysql_client.get_created_user(username=user_data[0]["username"])
        check.is_false(response_db, "User created without authorization!")
        if response_db:
            mysql_client.delete_user(username=user_data[0]['username'])
