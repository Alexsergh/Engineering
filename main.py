# 1)
# import time
#
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"\nВремя выполнения функции: {execution_time} секунд")
#         return result
#     return wrapper
#
# @timing_decorator
# def fibonacci(n):
#     fib1 = fib2 = 1
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#         print(fib2, end=' ')
#     return fib2
#
# if __name__ == '__main__':
#     fibonacci(200)

# 2)
# def file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             if not content:
#                 raise Exception(f"Файл {file_path} пустой")
#             else:
#                 print(f"Информация из файла {file_path}:")
#                 print(content)
#     except FileNotFoundError:
#         print(f"Файл '{file_path}' не найден.")
#     except Exception as e:
#         print(e)
#
#
# file1 = '123.txt'
# file2 = '1234.txt'
#
# file(file1)
# file(file2)

# 3)
# def user_input():
#     try:
#         num = int(input('введите число: '))
#         res = 2 + num
#         print(f"Результат: {res}")
#     except ValueError:
#         print("Непрвильные входные данные")
# user_input()

# 4)
# def check_even_result(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if result % 2 == 0:
#             print(f"Число {result} четное")
#         else:
#             print(f'Число {result} нечетное')
#         return result
#     return wrapper
#
#
# @check_even_result
# def add_numbers(a, b):
#     c = a + b
#     return c
#
#
# @check_even_result
# def multiply_numbers(a, b):
#     c = a * b
#     return c
#
#
# result1 = add_numbers(2, 3)
# result2 = multiply_numbers(4, 5)

# 5)
# class Ex(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)
#
#
# # Фрагмент 1: Использование исключения в функции
# def divide_numbers(a, b):
#     if b == 0:
#         raise Ex("Делить на 0 нельзя")
#     return a / b
#
# def custom_operation(value):
#     if value < 0:
#         raise Ex("Отрицательные значения не поддерживаются")
#     return value
#
# try:
#     result1 = divide_numbers(10, 2)
#     print(f"Результат деления: {result1}")
#
#     result2 = custom_operation(-5)
#     print(f"Результат деления: {result2}")
#
# except Ex as ce:
#     print(f"Произошло исключение: {ce.message}")




