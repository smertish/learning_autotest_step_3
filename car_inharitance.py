from base_car import Car


class CargoCar(Car):
    """Инициализируем атрибуты класса-наследника"""

    def __init__(self, model, year, capacity, price, mileage):
        super().__init__(model, year, capacity, price, mileage)
        self.wheels = 8


"""Создаем экзмепляр класса Car"""
random_car = Car("Ламборгини диабло", "2005", 5, 20000, 6000)
print(random_car.machine_description())

"""Создаем экземпляр класса наследника"""
cargo_car = CargoCar("Грузовая тачка", "2007", 6, 12000, 20001)
print(cargo_car.machine_description())
