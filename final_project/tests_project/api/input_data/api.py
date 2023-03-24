import allure
from generators.api_json_data import BuilderAddUser


class InputData:
    """
    Test cases, input data for autotests
    """
    TEST_CASE_LINK = "https://docs.google.com/spreadsheets/d/"
    "1hKhQdMW60mBiX_1Kio1XOHSM1yScmC9_BOJ_CE4dTFA/"

    @staticmethod
    @allure.step("Generation of user data for a positive test.")
    @allure.link(TEST_CASE_LINK, name='Test documentation')
    def positive_test_cases_add_user():
        return [
            BuilderAddUser().set_name(1).set_surname(100).set_middle_name(100)
            .set_username(10).set_password(100).set_email(32).build(),  # 1
            BuilderAddUser().set_name(45).set_surname(255).set_middle_name(100)
            .set_username(6).set_password(255).set_email(6).build(),  # 2
            BuilderAddUser().set_name(45).set_surname(100).set_middle_name(1)
            .set_username(16).set_password(1).set_email(56).build(),  # 3
            BuilderAddUser().set_name(45).set_surname(1).set_middle_name(255)
            .set_username(6).set_password(255).set_email(24).build(),  # 4
            BuilderAddUser().set_name(45).set_surname(1).set_middle_name(255)
            .set_username(10).set_password(1).set_email(56).build(),  # 5
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(255)
            .set_username(16).set_password(1).set_email(6).build(),  # 6
            BuilderAddUser().set_name(20).set_surname(1).set_middle_name(1)
            .set_username(10).set_password(255).set_email(56).build(),  # 7
            BuilderAddUser().set_name(20).set_surname(255).set_middle_name(255)
            .set_username(6).set_password(1).set_email(24).build(),  # 8
            BuilderAddUser().set_name(20).set_surname(1).set_middle_name(100)
            .set_username(16).set_password(255).set_email(6).build(),  # 9
            BuilderAddUser().set_name(20).set_surname(255).set_middle_name(1)
            .set_username(6).set_password(100).set_email(56).build(),  # 10
            BuilderAddUser().set_name(1).set_surname(1).set_middle_name(255)
            .set_username(16).set_password(100).set_email(6).build(),  # 11
            BuilderAddUser().set_name(1).set_surname(255).set_middle_name(100)
            .set_username(6).set_password(1).set_email(56).build(),  # 12
            BuilderAddUser().set_name(1).set_surname(1).set_middle_name(1)
            .set_username(16).set_password(255).set_email(24).build(),  # 13
            BuilderAddUser().set_name(1).set_surname(100).set_middle_name(1)
            .set_username(6).set_password(255).set_email(56).build(),  # 14
            BuilderAddUser().set_name(45).set_surname(255).set_middle_name(1)
            .set_username(10).set_password(255).set_email(6).build(),  # 15
            BuilderAddUser().set_name(45).set_surname(1).set_middle_name(255)
            .set_username(6).set_password(100).set_email(56).build(),  # 16
            BuilderAddUser().set_name(45).set_surname(255).set_middle_name(1)
            .set_username(16).set_password(1).set_email(24).build(),  # 17
            BuilderAddUser().set_name(45).set_surname(100).set_middle_name(255)
            .set_username(6).set_password(255).set_email(6).build(),  # 18
            BuilderAddUser().set_name(45).set_surname(1).set_middle_name(100)
            .set_username(16).set_password(1).set_email(56).build(),  # 19
            BuilderAddUser().set_name(45).set_surname(45).set_middle_name(0)
            .set_username(16).set_password(45).set_email(56).build()  # 20
        ]

    @staticmethod
    @allure.step("Generation of user data for a negative test.")
    @allure.link(TEST_CASE_LINK, name='Test documentation')
    def negative_test_cases_add_user():
        return [
            BuilderAddUser().set_name(0).set_surname(100).set_middle_name(100)
            .set_username(10).set_password(100).set_email(24).build(),  # 1
            BuilderAddUser().set_name(46).set_surname(100).set_middle_name(100)
            .set_username(10).set_password(100).set_email(24).build(),  # 2
            BuilderAddUser().set_name(20).set_surname(0).set_middle_name(100)
            .set_username(10).set_password(100).set_email(24).build(),  # 3
            BuilderAddUser().set_name(20).set_surname(256).set_middle_name(100)
            .set_username(10).set_password(100).set_email(24).build(),  # 4
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(256)
            .set_username(10).set_password(100).set_email(24).build(),  # 5
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(5).set_password(100).set_email(24).build(),  # 6
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(17).set_password(100).set_email(24).build(),  # 7
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(10).set_password(0).set_email(24).build(),  # 8
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(10).set_password(256).set_email(24).build(),  # 9
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(10).set_password(100).set_email(5).build(),  # 10
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(10).set_password(100).set_email(67).build(),  # 11
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(0).set_password(100).set_email(24).build(),  # 12
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(10).set_password(100).set_email(0).build()  # 13
        ]

    @staticmethod
    @allure.step("Generation of users for with the same username.")
    def user_username_already_use():
        return [
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(username="UserTest").set_password(100).set_email(24).build(),
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(username="UserTest").set_password(100).set_email(24).build()
        ]

    @staticmethod
    @allure.step("Generation of users for with the same email.")
    @allure.link(TEST_CASE_LINK, name='Test documentation')
    def user_email_already_use():
        return [
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(10).set_password(100).set_email(email="test@test.test").build(),
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(10).set_password(100).set_email(email="test@test.test").build()
        ]

    @staticmethod
    @allure.step("Normal user generation.")
    def default_user():
        return [
            BuilderAddUser().set_name(20).set_surname(100).set_middle_name(100)
            .set_username(10).set_password(100).set_email(24).build(),
        ]





