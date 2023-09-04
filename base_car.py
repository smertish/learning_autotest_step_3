class Car():
    """Создаем тачку"""

    def __init__(self, model, year, capacity, price, mileage):
        self.model = model
        self.year = year
        self.capacity = capacity
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def machine_description(self):
        """Получение описания тачки"""
        description = f"Модель тачки {self.model} {self.year} года; Объем движка {self.capacity}; Стоимостью " \
                      f"{self.price} и пробегом {self.mileage}; Количество колес {self.wheels}"
        return description
