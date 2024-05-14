from datetime import datetime, timedelta
from collections import UserDict
from birthday import DATE_FORMAT

def is_weekend_day(day):
    return day > 4

class AddressBook(UserDict):
    def add_record(self, record):
        # Додавання нового запису до адресної книги
        if record.name.value in self.data:
            raise KeyError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        # Пошук запису за ім'ям
        return self.data.get(name)
        


    def delete(self, name):
        # Видалення запису за ім'ям
        del self.data[name]

    def get_upcoming_birthdays(self):
        # Пошук записів, дні народження яких відбудуться протягом наступних days днів
        today = datetime.today().date()
        upcoming_birthdays = []
        for name, record in self.data.items():
            if record.birthday:
                birthday = record.birthday.value.replace(year=today.year).date()

                timedelta_days = (birthday - today).days

                if 0 <= timedelta_days <= 7:
                    if is_weekend_day(birthday.weekday()):
                        days_delta = 2 if birthday.weekday() == 5 else 1
                        congratulation_date = birthday + timedelta(days=days_delta)
                    else:
                        congratulation_date = birthday

                    upcoming_birthdays.append(
                        {
                            "name": name,
                            "congratulation_date": congratulation_date.strftime(
                                DATE_FORMAT
                            ),
                        }
                    )

        return upcoming_birthdays

    