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

    def add_phone(self, value):
        self.phones.append(Field(value))
        return self.phones

    def edit_phone(self, name, value):
        name_user = input("Enter name-key: ")

        # new_phone = input("Enter value: ")
        if name == name_user:
            book.find(name)
        print(book)
        # contact = book.find(Name(name))

        # return contact

    def remove_phone(self, name):
        self.data(self, name)

    def find_phone(self, *args):
        phone = args[0]
        name = self.name.name
        phones = book[name]
        if phone in phones:
            return {name: phone}

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, value):
        self.name = Name
        self.value = value

    def find(self, key):
        name_user = input("Enter name-key: ")
        for val in self.data.values():
            if val == name_user:
                print(self.data[Phone])
        return self.data

    def delete(self):
        name_user1 = input("Enter name-key1: ")
        for key in self.data.keys():
            if key == name_user1:
                self.data.setdefault(key)
            return self.data


# if __name__ == "__main__":
#     main()

book = AddressBook()
john_record = Record("John")
john_record.add_phone("5555555555")
john_record.add_phone("1234567890")
book.add_record(john_record)
print(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
print(jane_record)
for name, record in book.data.items():
    print(record)
book.find("John")
# print(sq)
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print()
# print(book.add_record(john_record))
