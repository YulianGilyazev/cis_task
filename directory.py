import re


class PhoneDirectory:

    def __init__(self):
        self.dict_name = {}
        self.dict_phone = {}

    def insert(self, phone, name):
        self.dict_phone[phone] = name
        self.dict_name[name] = phone

    def find_by_name(self, name):
        return self.dict_name[name]

    def find_by_phone(self, phone):
        return self.dict_phone[phone]

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


def test():
    d = PhoneDirectory()
    d.insert('123', 'ivan')
    d.insert('345', 'kolya')
    print(d.find_by_phone('123'))
    d.insert('124', 'petr')
    print(d.find_by_template('1**'))


if __name__ == '__main__':
    test()