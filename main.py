from collections import UserDict
import re


# def staticmethod(func):
#     def inner(*args):
#         try:
#             return func(*args)
#         except IndexError:
#             return "Not enough params. Use help."
#         except KeyError:
#             return "Unknown rec_id. Try another or use help."
#         except TypeError:
#             return "How can I help you?"
#         except NameError:
#             return "There is no such number in the dict"

#     return inner


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def self_name(self, name):
        self.name = name
        return str(self.name)


class Phone(Field):
    def __init__(self, value):
        if not Phone.is_valid_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    @staticmethod
    def is_valid_phone(value):
        # відбір номеру з 10 цифр
        pattern = r"((^\+([0-9]{10}$)))|([0-9]{10}$)"
        return bool(re.match(pattern, value))


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: Phone):
        self.phones.append(phone)
        return self.phones

    def edit_phone(self, ph: Phone, new_phone: Phone) -> str:
        # for ph in self.phones:
        if ph in self.phones:
            self.phones.remove(ph)
            self.phones.append(new_phone)
            return self.phones
        # if not ph in self.phones or self.phones == []:
        # return ValueError("Number not exist")

    def remove_phone(self, phone: Phone):
        if phone in self.phones:
            self.phones.remove(phone)
        return self.phones

    def find_phone(self, phone: Phone):
        # for phone in self.phones:
        if phone in self.phones:
            return phone

        # return self.phones

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        self.name = Name
        self.value = Phone
        return self.data

    def find(self, name_user: Name):
        for key in self.data.keys():
            if key == name_user:
                return self.data.get(key)
            # return self.data

    # if Record.name.value == name_user:
    #     print(self.data[Phone])
    # return self.data

    def delete(self, name_user: Name):
        # name_user = input("Enter name-key1: ")
        for key in self.data.keys():
            if key == name_user:
                self.data.pop(key)
            return self.data


# def parser(text: str):
#     for func, kw in .items():
#         if text.startswith(kw):
#             return func, text[len(kw) :].strip().split()
#     return unknown, []


# if __name__ == "__main__":
#     main()

book = AddressBook()
john_record = Record("John")
john_record.add_phone("5555555555")
john_record.add_phone("1234567890")
book.add_record(john_record)
# print(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
# print(jane_record)
for name, record in book.data.items():
    print(record)
# sq = book.find("John")
# print(sq)
john = book.find("John")

john_record.edit_phone("1234567890", "1112223333")
print(john)
found_phone = john_record.find_phone("5555555555")
print(found_phone)
# print(f"{john_record.name}: {found_phone}")  # Виведення: 5555555555
# print()
# book.add_record(john_record)
