# 1)
# from datetime import datetime  # импортируем модуль datatime и пакета datatime
# from math import sqrt  # импортируем модуль sqrt из пакета math
#
#
# def main(**kwargs):
#     """
#     Функция перебирает элементы в аргументах ключевого слова, вычисляет квадратный корень из суммы квадратов первого элемента и квадрата второго элемента.
#     Args:
#         **kwargs
#     Print:
#         квадратный корень из суммы квадратов первого элемента и квадрата второго элемента
#     """
#
#     for key in kwargs.items():  # перебираем каждый элемент в аргументах
#         result = sqrt(key[1][0] ** 2 + key[1][
#             1 ** 2])  # вписываем в переменную result квадратный корень из суммы квадратов первого элемента и квадрата второго элемента
#         print(result)  # выводим получившийя результат
#
#
# if __name__ == '__main__':  # проверяем, является ли текущий модуль точкой входа в программу
#     start_time = datetime.now() # в переменную start_time вывдим настоящее время
#     main(
#         one=[10, 3],
#         two=[5, 4],
#         three=[15, 13],
#         four=[93, 53],
#         five=[133, 15]
#
#     ) # вызываем функцию и заполняем ее аргументами
#     time_costs = datetime.now() - start_time # вычисляем время, затраченное на запуск программы
#     print(f'Время выполнения программы - {time_costs}') # выводим затраченнное время в консоль

# 2)
# from random import randint
#
# def main():
#
#     random = randint(1, 6)
#     print(f'Вы бросили кубик  и вам выпало {random}')
#
#     if random in [5,6]:
#         print("Вы победили")
#     elif random in [1,2]:
#         print('Вы проиграли')
#     else:
#         main()
#
# if __name__ == '__main__':
#     main()

# 3)
# import datetime
# import time
#
# for _ in range(5):
#     cur_time = datetime.datetime.now()
#     print(f"Теущая дата: {cur_time.strftime('%Y-%m-%d %H:%M:%S')}")
#     time.sleep(1)

# 4)
# def main():
#     numbers = []
#     while True:
#         user_input = input('Введите число.Чтобы прекратить ввод, введите слово "стоп": ')
#         if user_input == 'стоп':
#             break
#         try:
#             fl = float(user_input)
#             numbers.append(fl)
#         except ValueError:
#             print("Неверный формат числа. Повторите ввод.")
#
#     if len(numbers) == 0:
#         return None
#
#     evarage = sum(numbers) / len(numbers)
#     return evarage
#
#
# if __name__ == '__main__':
#     evar = main()
#     if evar is not None:
#         print(f'Среднее арифметическое для введенных чисел равно: {evar}')
#     else:
#         print('Для начала нужно ввести числа!')

#5
# from five import main
# if __name__ == '__main__':
#
#     a = float(input('Введите длину стороны а: '))
#     b = float(input('Введите длину стороны b: '))
#     c = float(input('Введите длину стороны c: '))
#
#     if a < 0 or b < 0 or c < 0:
#         print('Стороны треугольника не могут принимать отрицательн значения')
#     elif a + b <= c or a + c <= b or b + c <= a:
#         print('Треугольник с заданными сторонами не существует')
#     else:
#         area = main(a, b, c)
#         print(f'площадь заданного треугольника равна: {area}')









