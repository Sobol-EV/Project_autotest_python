from generators.builder_base import BuilderBase
from random import randint


class BuilderEmail(BuilderBase):

    def __init__(self):
        super().__init__()

    @staticmethod
    def gen_quary(length):
        return "?" * length

    def email_small_upper(self, length=35):
        """Email в верхнем и нижнем регистре"""
        if 7 <= length <= 63:
            return self.fake.lexify(self.gen_quary(randint(1, 25)),
                                    letters=self.alf_english_small) + \
                   self.fake.lexify(self.gen_quary(randint(1, 30)),
                                    letters=self.alf_english_upper) + "@TeSt.Qa"
        if length == 64:
            return self.fake.lexify(self.gen_quary(28), letters=self.alf_english_small) + \
                   self.fake.lexify(self.gen_quary(28), letters=self.alf_english_upper) + "@TeSt.Qa"

    def email_numbers(self, length=35):
        """Email с цифрами в имени пользователя"""
        if 7 <= length <= 63:
            return self.fake.lexify(
                self.gen_quary(randint(1, 55)) + "@test.qa",
                letters=self.alf_numbers
            )
        if length == 64:
            return self.fake.lexify(
                self.gen_quary(56) + "@test.qa",
                letters=self.alf_numbers
            )

    def email_defis_name(self, length=35):
        """Email с дефисом в именной части"""
        if 7 <= length <= 63:
            return self.fake.lexify(
                self.gen_quary(randint(1, 25)) + "-" +
                self.gen_quary(randint(1, 29)) + "@test.qa",
                letters=self.alf_english
            )
        if length == 64:
            return self.fake.lexify(
                self.gen_quary(28) + "-" +
                self.gen_quary(27) + "@test.qa",
                letters=self.alf_english
            )

    def email_defis_hostname(self, length=35):
        """Email с дефисом в доменной части"""
        if 7 <= length <= 63:
            return self.fake.lexify(
                self.gen_quary(randint(1, 54)) + "@te-st.qa",
                letters=self.alf_english
            )
        if length == 64:
            return self.fake.lexify(
                self.gen_quary(55) + "@te-st.qa",
                letters=self.alf_english
            )

    def email_underlining_name(self, length=35):
        """Email со знаком подчеркивания в имени пользователя"""
        if 7 <= length <= 63:
            return self.fake.lexify(
                self.gen_quary(randint(1, 25)) + "_" +
                self.gen_quary(randint(1, 29)) + "@test.qa",
                letters=self.alf_english
            )
        if length == 64:
            return self.fake.lexify(
                self.gen_quary(28) + "_" +
                self.gen_quary(27) + "@test.qa",
                letters=self.alf_english
            )

    def email_underlining_hostname(self, length=35):
        """Email со знаком подчеркивания в доменной части"""
        if 7 <= length <= 63:
            return self.fake.lexify(
                self.gen_quary(randint(1, 54)) + "@te_st.qa",
                letters=self.alf_english
            )
        if length == 64:
            return self.fake.lexify(
                self.gen_quary(55) + "@te_st.qa",
                letters=self.alf_english
            )

    def email_dot_name(self, length=35):
        """Email с точками в имени пользователя"""
        if 7 <= length <= 63:
            return self.fake.lexify(
                self.gen_quary(randint(1, 12)) + "." +
                self.gen_quary(randint(1, 12)) +
                "." + self.gen_quary(randint(1, 29)) + "@test.qa",
                letters=self.alf_english
            )
        if length == 64:
            return self.fake.lexify(
                self.gen_quary(14) + "." + self.gen_quary(13) +
                "." + self.gen_quary(27) + "@test.qa",
                letters=self.alf_english
            )

    def email_dot_hostname(self, length=35):
        """Email с несколькими точками в доменной части"""
        if 7 <= length <= 63:
            return self.fake.lexify(
                self.gen_quary(randint(1, 54)) + "@te.st.qa",
                letters=self.alf_english
            )
        if length == 64:
            return self.fake.lexify(
                self.gen_quary(55) + "@te.st.qa",
                letters=self.alf_english
            )

    def email_cyrillic_hostname(self, length=35):
        """Email с кириллическим доменным именем (login@домен.рф)"""
        if 7 <= length <= 63:
            return self.fake.lexify(
                self.gen_quary(randint(1, 55)) + "@тест.кюа",
                letters=self.alf_english
            )
        if length == 64:
            return self.fake.lexify(
                self.gen_quary(56) + "@тест.кюа",
                letters=self.alf_english
            )

    def bad_email_no_dot_hostname(self):
        """Email без точек в доменной части"""
        return self.fake.lexify(
            self.gen_quary(randint(1, 57)) + "@testqa",
            letters=self.alf_english
        )

    def bad_email_no_dog_symbol(self):
        """Отсутствие @ в email"""
        return self.fake.lexify(
            self.gen_quary(randint(7, 64)),
            letters=self.alf_english
        )

    def bad_email_space_hostname(self):
        """Email с пробелами в доменной части"""
        return self.fake.lexify(
            self.gen_quary(randint(7, 55)) + "@test qa",
            letters=self.alf_english
        )

    def bad_email_space_name(self):
        """Email с пробелами в имени пользователя"""
        return self.fake.lexify(
            self.gen_quary(randint(1, 25)) + " " +
            self.gen_quary(randint(1, 25)) + "@test.qa",
            letters=self.alf_english
        )

    def bad_email_no_name(self):
        """Email без имени пользователя"""
        return self.fake.lexify(
             "@" + self.gen_quary(randint(1, 25)) + "test.qa",
            letters=self.alf_english
        )

    def bad_email_no_hostname(self):
        """Email без доменной части"""
        return self.fake.lexify(
            self.gen_quary(randint(7, 63)) + "@",
            letters=self.alf_english
        )
