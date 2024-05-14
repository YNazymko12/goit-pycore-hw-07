class Field:
    def __init__(self, value):
         # Ініціалізуємо значення полів
        self.value = value

    def __str__(self):
        # Перетворюємо значення поля на рядок та повертаємо його
        return str(self.value)