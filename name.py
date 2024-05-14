from field import Field

class Name(Field):
    def __init__(self, name):
        # Ініціалізуємо значення імені через батьківський клас Field
        self.value = name