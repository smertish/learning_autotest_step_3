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
            self.height) + "; Его вес " + str(self.weight)
        print("Нового человека зовут " + description)

    def get_weight(self):
        """Получение веса человека"""
        print("Вес человека " + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg


class Warrior(Person):
    """Создаем класс воина"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряда ярости"""
        print("Заряд ярости равен значению " + str(self.rage))

    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + " в возрасте " + str(self.age) + " лет; Его заряд ярости равен значению " + str(
            self.rage)
        # print("Нового человека зовут " + description)
        return description
