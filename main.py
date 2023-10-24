from collections import UserDict
from datetime import datetime, timedelta
import re
import random


class Birthday:
    # def gen_birth(self, date):
    #     self.date = date
    #     current_day = datetime.now()
    #     old_day = current_day - timedelta(days=365 * 40)
    #     fake_year = random.randrange(old_day.year, current_day.year)
    #     fake_month = random.randrange(1, 12)
    #     fake_day = random.randrange(1, 31)
    #     try:
    #         fake_birthday = datetime(year=fake_year, month=fake_month, day=fake_day)
    #     except ValueError:
    #         ...

    #     if current_day >= fake_birthday:
    #         self.data["birthday"] = fake_birthday.date()

    #     return self

    def __init__(self, birthday) -> None:
        self.birthday = birthday

    def birth_day(self, birthday: str):
        if not Birthday.is_valid_birth_day(birthday):
            raise ValueError("Invalid phone number format")
        super().__init__(birthday)

    def is_valid_birth_day(self, birthday: str):
        patern_birth = r"^(1|2)(9|0)[0-2,7-9][0-9]{1}(.|/| )(0|1)[0-9](.|/| )[0-3][0-9]"
        return bool(re.match(patern_birth, birthday))

    def day_year(self, birthday: str):
        day_birth = datetime.strptime(birthday, "%Y.%m.%d")
        bir_th_day = day_birth.replace(
            year=datetime.today().year, month=day_birth.month, day=day_birth.day
        )
        return bir_th_day.date()


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
    def days_to_birthday(self, birthday: datetime):
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
        print(daybirth)

    def __str__(self):
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


class Iterator:
    def __init__(self):
        self.current_value = self.data

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration


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
    # print(john_record)
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")

    john_record.edit_phone("1234567890", "1112223333")
    print(john)
    found_phone = john_record.find_phone("5555555555")
    # print(found_phone)
    # john_record.find_phone("1234567890")
    # found_phone2 = john_record.find_phone("1112223333")
    # print(found_phone2)
    # book.delete("Jane")
