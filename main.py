# 1), 2), 3)
# class Car:  # создаем класс Car
#     def __init__(self, make, model):  # инициализируем объект данного класса, где self - ссылка на текущий объект
#         self.make = make  # устанавливаем значение атрибута make
#         self.model = model  # устанавливаем значение атрибута model
#
#     def drive(self):
#         print(
#             f"Driving the {self.make} {self.model}")  # метод класса Car, который выводит сообщение о том, что мы водим машину с атрибутами make и model
#
#
# my_car = Car("Toyota", "Corolla")
# my_car.drive()
#
#
# class ElectricCar(Car):  # создание класса ElectricCar, который наследует атрибуты и методы класса Car
#     def __init__(self, make, model, battery_capacity):
#         super().__init__(make, model) # вызываем метода родительского класса Car для установки атрибутов make и model.
#         self.battery_capacity = battery_capacity # устанавливаем значение атрибута battery_capacity
#
#     def charge(self):
#         print(f'Charging the {self.make} {self.model} with {self.battery_capacity} kWh')
# # Метод класса ElectricCar, который выводит сообщение о том, что мы заряжаем машину с атрибутами make, model и battery_capacity.
#
# my_electric_car = ElectricCar("Tesla", "Model S", 75)
# my_electric_car.drive()
# my_electric_car.charge()

# 4)
# class Car:  # создаем класс Car
#     def __init__(self, make, model):  # инициализируем объект данного класса, где self - ссылка на текущий объект
#         self.make = make  # устанавливаем значение атрибута make
#         self.model = model  # устанавливаем значение атрибута model
#
#     def drive(self):
#             print(f"Driving the {self.make} {self.model}")  # метод класса Car, который выводит сообщение о том, что мы водим машину с атрибутами make и model
#
#
# my_car = Car("Toyota", "Corolla")
# print(my_car.make) # Доступ к защищенному атрибуту
# my_car.drive()

# 5)
# class Shape:
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#
# rec = Rectangle(20, 30)
# cir = Circle(5)
#
# print(rec.area())
# print(cir.area())