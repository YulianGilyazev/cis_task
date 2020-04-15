import re


class PhoneDirectory:

    def __init__(self):
        self.dict_name = {}
        self.dict_phone = {}

    def insert(self, phone, name):
        self.dict_phone[phone] = name
        self.dict_name[name] = phone

    def find_by_name(self, name):
        if name in self.dict_name:
            return self.dict_name[name]
        else:
            raise Exception('this name is not in the directory')

    def find_by_phone(self, phone):
        if phone in self.dict_phone:
            return self.dict_phone[phone]
        else:
            raise Exception('this phone number is not in the directory')

    def find_by_first_numbers(self, first_nums):
        numbers = self.dict_phone.keys()
        suitable_names = []
        for number in numbers:
            if number[0:len(first_nums)] == first_nums:
                suitable_names.append(self.dict_phone[number])
        return suitable_names

    def find_by_template(self, template):
        correct_template = template.replace('*', '.')
        numbers = self.dict_phone.keys()
        suitable_names = []
        for number in numbers:
            if re.match(correct_template, number) is not None:
                suitable_names.append(self.dict_phone[number])
        return suitable_names

