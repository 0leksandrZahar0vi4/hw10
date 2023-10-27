from collections import UserDict
from itertools import islice
from datetime import datetime, timedelta
import re
import random


class Field:
    def __init__(self, value):
        self.__privat_value = None
        self.value = value

    @property
    def value(self):
        return self.__privat_value

    @value.setter
    def value(self, value: str):
        if value.isalpha():
            self.__privat_value = value
        else:
            raise Exception("Wrong value")


class Birthday(Field):
    def __init__(self, birthday) -> None:
        self.__privat_birthday = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__privat_birthday

    @birthday.setter
    def birthday(self, birthday):
        if not Birthday.is_valid_birth_day(self, birthday):
            self.__privat_birthday = birthday
        else:
            ValueError("Invalid phone number format")

    def is_valid_birth_day(self, birthday: str):
        patern_birth = r"^(1|2)(9|0)[0-2,7-9][0-9]{1}(.|/| )(0|1)[0-9](.|/| )[0-3][0-9]"
        return bool(re.match(patern_birth, birthday))

    def day_year(self, birthday: str):
        day_birth = datetime.strptime(birthday, "%Y.%m.%d")
        bir_th_day = day_birth.replace(
            year=datetime.today().year, month=day_birth.month, day=day_birth.day
        )
        return bir_th_day.date()


class Name(Field):
    def self_name(self, name):
        self.__privat_name = None
        self.name = name
        return str(self.name)

    @property
    def name(self):
        return self.__privat_name

    @name.setter
    def name(self, name: str):
        if name.isalpha():
            self.__privat_name = name
        else:
            raise Exception("Wrong name")


class Phone(Field):
    def __init__(self, value):
        self.__privat_value = None
        self.value = value

    @property
    def value(self):
        return self.__privat_value

    @value.setter
    def value(self, value: str):
        if Phone.is_valid_phone(value):
            self.__privat_value = value
        else:
            raise ValueError("Invalid phone number format")
        # super().__init__(value)

    @staticmethod
    def is_valid_phone(value):
        # відбір номеру з 10 цифр
        pattern = r"((^\+([0-9]{10}$)))|([0-9]{10}$)"
        return bool(re.match(pattern, value))


class Record:
    def __init__(self, name: Name):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday

    def add_phone(self, phone: Phone):
        self.phones.append(Phone(phone))
        return self.phones

    def edit_phone(self, ph, new_phone) -> str:
        # for ph in self.phones:
        result = self.find_phone(ph)
        if result:
            self.remove_phone(ph)
            self.add_phone(new_phone)
            return self.phones
        if not result or self.phones == []:
            raise ValueError("Number not exist")

    def remove_phone(self, phone):
        result = self.find_phone(phone)
        if result:
            self.phones.remove(result)
            return self.phones

    def find_phone(self, phone: Phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph

    # Днів до дня народження
    def days_to_birthday(self, birthday: Birthday):
        self.birthday = birthday
        day_birth = datetime.strptime(birthday, "%Y.%m.%d")
        bir_th_day = day_birth.replace(
            year=datetime.today().year, month=day_birth.month, day=day_birth.day
        )
        # daybirth = datetime.strptime(birthday, "%Y.%m.%d").date()
        daybirth = datetime.today().date() - bir_th_day.date()
        if daybirth.days < 0:
            daybirth = bir_th_day.date() - datetime.today().date()
        else:
            daybirth = 365 - (datetime.today().date() - bir_th_day.date()).days
        return daybirth

    def __str__(self):
        # return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birth: {self.birthday} ({Record.days_to_birthday(self, self.birthday)} day to birthday))"
        if Birthday.birthday:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birth: {self.birthday} ({self.days_to_birthday(self.birthday)} day to birthday))"
        else:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


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

    def delete(self, name_user: Name):
        # name_user = input("Enter name-key1: ")
        for key in self.data.keys():
            if key == name_user:
                self.data.pop(key)
            return self.data

    # def islice(self, **args):
    #     counter = 0
    #     while counter < len(AddressBook.data):
    #         yield self.counter[self.counter : self.counter + n]
    #         counter += 1

    # def iterator(self, n=1):
    #     counter = 0
    #     while counter < len(self.data):
    #         yield self.counter[self.counter : self.counter + n]
    #         counter += 1
    def search_user(self):
        keyword = input("Enter keyword: ")
        # result = {}
        for key, val in self.data.items():
            if keyword in self.data["name"] or keyword in self.data["phone"]:
                return self.data


# class Iterator:
#     MAX_VALUE = len(AddressBook(data))

#     def __init__(self):
#         self.current_value = 0

#     def __next__(self):
#         if self.current_value < self.MAX_VALUE:
#             self.current_value += 1
#             return AddressBook.data
#         raise StopIteration


# def parser(text: str):
#     for func, kw in .items():
#         if text.startswith(kw):
#             return func, text[len(kw) :].strip().split()
#     return unknown, []


if __name__ == "__main__":
    book = AddressBook()
    john_record = Record("John")
    john_record.add_phone("5555555555")
    john_record.add_phone("1234567890")
    book.add_record(john_record)
    john_record.days_to_birthday("2003.07.26")
    john_record
    book.add_record(john_record)
    john_record
    print(john_record)
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    # print(jane_record)
    # for name, record in book.data.items():
    #     print(record)

    john = book.find("John")

    john_record.edit_phone("1234567890", "1112223333")
    john_record.find_phone("5555555555")
    john_record.find_phone("1234567890")
    print(john_record)
    found_phone2 = john_record.find_phone("1112223333")
    # found_phone2
    # book.delete("Jane")
    # address_book_iterator = Iterator(book)
    # for address in address_book_iterator:
    #     print(address)
    # for address in AddressBook.islice(1):
    #     print(address)
    searh = book.search_user()
    print(searh)
