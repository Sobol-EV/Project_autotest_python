from generators.registration_data import BuilderRegData
from generators.email_data import BuilderEmail


class InputData:

    def __init__(self):
        self.bld_email = BuilderEmail()

    def data_for_successful_authorization(self):
        """
        https://docs.google.com/spreadsheets/d/1suxZsDot5XmrmlGLBWeJWPput-zL4cbvRwb4mwpaVV0
        Позитивные кейсы с 1 по 18
        ::return [dict, dict, ...]
        """
        return [
            BuilderRegData().set_middle_name(255).set_username(16)
            .set_email(email=self.bld_email.email_small_upper(64)).build(),  # 1
            BuilderRegData().set_name(45).set_surname(255).set_middle_name(255)
            .set_username(6).set_email(email=self.bld_email.email_defis_name()).build(),  # 2
            BuilderRegData().set_name(45).set_middle_name(middle_name="null")
            .set_email(6).set_password(255).set_repeat_password().build(),  # 3
            BuilderRegData().set_name(45).set_surname(255).set_username(6)
            .set_email(email=self.bld_email.email_defis_hostname()).build(),  # 4
            BuilderRegData().set_name(45).set_middle_name(middle_name="null")
            .set_email(email=self.bld_email.email_numbers(64)).set_password(255)
            .set_repeat_password().build(),  # 5
            BuilderRegData().set_surname(255).set_middle_name(middle_name="null")
            .set_username(16).set_email(email=self.bld_email.email_underlining_name())
            .set_password(255).set_repeat_password().build(),  # 6
            BuilderRegData().set_username(6).set_email(6).build(),  # 7
            BuilderRegData().set_middle_name(255).set_username()
            .set_email(email=self.bld_email.email_defis_hostname())
            .set_password(255).set_repeat_password().build(),  # 8
            BuilderRegData().set_surname(255).set_middle_name(middle_name="null")
            .set_username(6).set_email(56).build(),  # 9
            BuilderRegData().set_name(45).set_surname(255).set_email(56).build(),  # 10
            BuilderRegData().set_name(45).set_middle_name(255).set_username(6)
            .set_email(6).set_password(255).set_repeat_password().build(),  # 11
            BuilderRegData().set_name(45).set_surname(255).set_username(16)
            .set_email(6).set_password(255).set_repeat_password().build(),  # 12
            BuilderRegData().set_name(45).set_middle_name(middle_name="null").set_username(6)
            .set_email(email=self.bld_email.email_dot_name()).build(),  # 13
            BuilderRegData().set_middle_name(middle_name="null").set_username(16)
            .set_email(email=self.bld_email.email_dot_hostname()).build(),  # 14
            BuilderRegData().set_username(6).set_email(56).set_password(255)
            .set_repeat_password().build(),  # 15
            BuilderRegData().set_surname(255).set_middle_name(middle_name="null")
            .set_email(6).build(),  # 16
            BuilderRegData().set_username(6).set_email(email=self.bld_email.email_cyrillic_hostname())
            .set_password(255).set_repeat_password().build(),  # 17
            BuilderRegData().set_surname(255).set_middle_name(255).set_email(6).build()  # 18
        ]