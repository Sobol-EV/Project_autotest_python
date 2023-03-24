from faker import Faker


class BuilderBase:

    default_alf = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" \
                  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                  "1234567890~`!@#$%^&*()_+?:\"{}[];’▲♦♥öäβ "

    alf_cyrillic_small = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alf_cyrillic_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alf_cyrillic = alf_cyrillic_small + alf_cyrillic_upper
    alf_english_small = "abcdefghijklmnopqrstuvwxyz"
    alf_english_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alf_english = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alf_numbers = "1234567890"
    alf_special_characters = "~`!@#$%^&*()_+?:\"{}[];’"
    alf_other = "▲♦♥öäβ"

    def __init__(self):
        self.fake = Faker()
        self.result = {}

    def update_inner_value(self, keys, value):
        """
        The function allows you to change the generated objects at any level of
        nesting, and also makes it possible to create new ones
        """
        if not isinstance(keys, list):
            self.result[keys] = value
        else:
            temp = self.result
            for item in keys[:-1]:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[keys[-1]] = value
        return self

    def build(self):
        return self.result