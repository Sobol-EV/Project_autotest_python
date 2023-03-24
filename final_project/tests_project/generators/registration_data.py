
from generators.builder_base import BuilderBase


class BuilderRegData(BuilderBase):

    def __init__(self):
        super().__init__()
        self.reset()

    def set_name(self, length=10, alphabet=None, name=None):
        if not alphabet:
            alphabet = self.default_alf
        if name:
            self.result['name'] = name
            return self
        query = "?" * length
        self.result['name'] = self.fake.lexify(query, letters=alphabet)
        return self

    def set_surname(self, length=10, alphabet=None, surname=None):
        if not alphabet:
            alphabet = self.default_alf
        if surname:
            self.result['surname'] = surname
            return self
        query = "?" * length
        self.result['surname'] = self.fake.lexify(query, letters=alphabet)
        return self

    def set_middle_name(self, length=10, alphabet=None, middle_name=None):
        if middle_name == "null":
            if "middle_name" in self.result.keys():
                del self.result["middle_name"]
            return self
        if not alphabet:
            alphabet = self.default_alf
        if middle_name:
            self.result['middle_name'] = middle_name
            return self
        query = "?" * length
        self.result['middle_name'] = self.fake.lexify(query, letters=alphabet)
        return self

    def set_username(self, length=10, alphabet=None, username=None):
        if not alphabet:
            alphabet = self.default_alf
        if username:
            self.result['username'] = username
            return self
        query = "?" * length
        self.result['username'] = self.fake.lexify(query, letters=alphabet)
        return self

    def set_email(self, length=10, type_email=True, email=None):
        if email:
            self.result['email'] = email
            return self
        query = "?" * length
        if length == 6:
            self.result['email'] = self.fake.lexify("?@t.qa")
            return self
        if type_email:
            self.result['email'] = self.fake.lexify(query + "@test.qa")
        else:
            self.result['email'] = self.fake.lexify(query)
        return self

    def set_password(self, length=10, alphabet=None, password=None):
        if not alphabet:
            alphabet = self.default_alf
        if password:
            self.result['password'] = password
            return self
        query = "?" * length
        self.result['password'] = self.fake.lexify(query, letters=alphabet)
        return self

    def set_repeat_password(self, length=10, alphabet=None, equals=True, password=None):
        if password:
            self.result['confirm'] = password
            return self
        if equals:
            self.result['confirm'] = self.result['password']
            return self
        query = "?" * length
        self.result['confirm'] = self.fake.lexify(query, letters=alphabet)
        return self

    def set_other(self, fullness=None, term=None):
        if fullness:
            if term:
                self.result['term'] = 'y'
            else:
                self.result['term'] = ""
            self.result['submit'] = "Register"

    def reset(self):
        self.set_name()
        self.set_surname()
        self.set_middle_name()
        self.set_username()
        self.set_email()
        self.set_password()
        self.set_repeat_password()
        self.set_other()

