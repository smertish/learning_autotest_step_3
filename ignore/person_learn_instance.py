class Person():
    """Создаем человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описания человека"""
        description = self.name + " в возрасте " + str(self.age) + " лет; Его рост " + str(
            self.height) + "; Его вес " + self.weight
        print("Нового человека зовут " + description)

    def get_weight(self):
        """Получение веса человека"""
        print("Вес человека " + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg


man = Person("Алекс", 30, 180)
man.update_weight(110)
man.get_weight()
