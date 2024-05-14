from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        # Додавання нового запису до адресної книги
        if record.name.value in self.data:
            raise KeyError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        # Пошук запису за ім'ям
        record = self.data.get(name, None)
        if record is None:
            raise KeyError(f"Record with name '{name}' not found.")
        return record


    def delete(self, name):
        # Видалення запису за ім'ям
        if name not in self.data:
            raise KeyError(f"Record with name '{name}' not found.")
        del self.data[name]
