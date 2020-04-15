class Node:
    def __init__(self):
        self.next = {}
        self.is_leaf = False
        self.path_to_leaf = ""


class Bohr:
    def __init__(self):
        self.root = Node()

    def insert_string(self, string):
        cur_node = self.root
        for symb in string:
            new_node = Node()
            next_node = cur_node.next.get(symb, new_node)
            cur_node.next[symb] = next_node
            cur_node = next_node
        cur_node.is_leaf = True
        cur_node.path_to_leaf = string

    def find_all_leafs(self, node):
        answer = []
        if node.is_leaf:
            answer = [node.path_to_leaf]
        for key in node.next.keys():
            answer = answer + self.find_all_leafs(node.next[key])
        return answer

    def find_by_first(self, string):
        cur_node = self.root
        for symb in string:
            if cur_node.next.get(symb) is not None:
                cur_node = cur_node.next[symb]
            else:
                return []
        return self.find_all_leafs(cur_node)

    def find_by_template_rec(self, cur_node, string):
        if string == "":
            if cur_node.is_leaf:
                return [cur_node.path_to_leaf]
            return []

        symb = string[0]
        if symb == ".":
            answer = []
            for key in cur_node.next.keys():
                answer = answer + self.find_by_template_rec(
                    cur_node.next[key], string[1::]
                )
            return answer
        else:
            if cur_node.next.get(symb) is not None:
                cur_node = cur_node.next[symb]
                return self.find_by_template_rec(cur_node, string[1::])
            else:
                return []

    def find_by_template(self, string):
        return self.find_by_template_rec(self.root, string)


class PhoneDirectory:
    def __init__(self):
        self.dict_name = {}
        self.dict_phone = {}
        self.phone_numbers = Bohr()

    def insert(self, phone, name):
        self.dict_phone[phone] = name
        self.dict_name[name] = phone
        self.phone_numbers.insert_string(phone)

    def find_by_name(self, name):
        if name in self.dict_name:
            return self.dict_name[name]
        else:
            raise Exception("this name is not in the directory")

    def find_by_phone(self, phone):
        if phone in self.dict_phone:
            return self.dict_phone[phone]
        else:
            raise Exception("this phone number is not in the directory")

    def find_by_first_numbers(self, first_nums):
        numbers = self.phone_numbers.find_by_first(first_nums)
        suitable_names = []
        for number in numbers:
            suitable_names.append(self.dict_phone[number])
        return suitable_names

    def find_by_template(self, template):
        correct_template = template.replace("*", ".")
        numbers = self.phone_numbers.find_by_template(correct_template)
        suitable_names = []
        for number in numbers:
            suitable_names.append(self.dict_phone[number])
        return suitable_names
