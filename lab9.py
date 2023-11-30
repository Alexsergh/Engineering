# 1)
# class Ivan:
#     __slots__ = ['name']
#
#     def __init__(self, name):
#         if name == 'Иван':
#             self.name = f'Да, я {name}'
#         else:
#             self.name = f'Я не {name}, а Иван'
#
#
# per1 = Ivan('Алексей')
# per2 = Ivan('Иван')
# print(per1.name)
# print(per2.name)
#
# per2.surname = 'Петров'

# 2)
# class Icecream:
#     def __init__(self, ingredient=None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None
#
#     def composition(self):
#         if self.ingredient:
#             print(f'мороженое с {self.ingredient}')
#         else:
#             print('Обычное мороженое')
#
#
# icecream = Icecream()
# icecream.composition()
# icecream = Icecream('шоколадом')
# icecream.composition()

# 3)
# class MyClass:
#     def __init__(self, value):
#         self._value = value
#
#     def set_value(self, value):
#         self._value = value
#
#     def get_value(self):
#         return self._value
#
#     def del_value(self):
#         del self._value
#
#     value = property(get_value, set_value, del_value,'Свойство value')
#
# obj = MyClass(42)
# print(obj.get_value())
# obj.set_value(45)
# print(obj.get_value())
# obj.set_value(100)
# print(obj.get_value())
# obj.del_value()
# print(obj.get_value())

# 4)
# class Mammal:
#     className = 'Mammal'
#
#
# class Dog(Mammal):
#    species = 'canine'
#    sounds = 'wow'
#
#
# class Cat(Mammal):
#     species = 'feline'
#     sounds = 'meow'
#
# dog = Dog()
# print(f'Dog is {dog.className}, but they say {dog.sounds}')
# cat = Cat()
# print(f'Cat is {cat.className}, but they say {cat.sounds}')

# 5)
# class Russian:
#     @staticmethod
#     def greeting():
#         print('Привет')
#
#
# class English:
#     @staticmethod
#     def greeting():
#         print('Hello')
#
#
# def greet(language):
#     language.greeting()
#
#
# ivan = Russian()
# greet(ivan)
# john = English()
# greet(john)
