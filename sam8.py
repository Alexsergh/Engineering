# class Animals:
#     def __init__(self, name, nickname):
#         self.name = name
#         self.nickname = nickname
#
#     def pet(self):
#         print(f"It is {self.name}, it's nickname is {self.nickname}")
#
#
# animals = Animals('Cat', 'Lissi')
# print(animals.name)
# animals.pet()
#
#
# class WildAnimals(Animals):
#     def __init__(self, name, nickname, zoo_location):
#         super().__init__(name, nickname)
#         self.zoo_location = zoo_location
#
#     def wild(self):
#         print(
#             f"It is a {self.name}, it's name is {self.nickname}. {self.nickname} is located in the {self.zoo_location}")
#
#
# wild_animal = WildAnimals("Bear", "Bob", "New York")
# wild_animal.wild()

# 5)
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         pass
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof"
#
#
#
# def animal_speak(animal):
#     print(animal.speak())
#
#
# cat = Cat("Fluffy")
# dog = Dog("Buddy")
#
#
# animal_speak(cat)
# animal_speak(dog)
