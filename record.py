from phone import Phone
from name import Name
from birthday import Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        contact_info = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        if self.birthday:
            contact_info += f", birthday: {self.birthday}"
        return contact_info
    
    def add_phone(self, phone_number):
       # Додавання нового номеру телефону до запису
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
       # Видалення номеру телефону з запису
        self.phones = list(filter(lambda p: p.value != phone_number, self.phones))
    
    def edit_phone(self, old_phone, new_phone):
        # Редагування номеру телефону у записі
        self.phones = list(map(lambda phone: Phone(new_phone) if phone.value == old_phone else phone, self.phones))

    def find_phone(self, phone_number):
         # Пошук номеру телефону у записі
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
    
    def add_birthday(self, birthday):
        # Додавання дати народження до запису
        if not self.birthday:
            self.birthday = Birthday(birthday)
        else:
            raise ValueError("Birthday already exists for this record.")
            
    