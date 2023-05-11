from collections import UserDict


class Field:

    def __init__(self, value) -> None:
        self.value = value


class Name(Field):

    def __init__(self, value) -> None:
        super().__init__(value)


class Phone(Field):

    def __init__(self, value) -> None:
        super().__init__(value)


class Record:

    def __init__(self, name=Name, phone=None | Phone):
        self.name = name
        self.phone = phone


class AddressBook(UserDict):

    def __init__(self) -> None:
        self.data = {}

    def add_record(self, record=Record):
        self.data[record.name] = record.phone


if __name__ == "__main__":
    USERS = AddressBook()
    print(USERS)
    n = Name('Andy')
    record = Record(n.value, '09013212414')
    USERS.add_record(record)
    b = Phone('07098609')
    USERS[n.value] = b.value
    print(USERS)
