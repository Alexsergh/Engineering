# 1)
# one = int(input('Введите значение первой переменной: '))
# two = int(input('Введите значение второй переменной: '))
# if one >= two:
#     print('Выполняется')
# else:
#     print('Не выполняется')

# 2)
# one = int(input("Введите значение переменной: "))
# if one < 0:
#     print("переменя меньше 0")
# elif  0 < one < 10:
#     print("перемнная больше 0 и меньше 10")
# else:
#     print('переменя больше 10')

#3)
# numbers = [1, 2, 3, 4, 5]
# value = int(input("Введите значение переменной: "))
# if value in numbers:
#     print("Перемення есть в данном массиве")
# else:
#     print("Переменной нет в данном массиве")

#4)
# numbers = [1, 2, 10, 20, 3, 30, 423, 532]
# value = int(input("Введите значение переменной: "))
# if value in numbers:
#     if value % 2 == 0:
#         print('Перемнная четная и есть в массиве')
#     else:
#         print('Переменная нечетная и есть в массиве' )
# else:
#     print(f'перемнной нет в массиве и она равна {value}')

# 5)
# for i in range(10):
#     print('i = ', i)
#     if i == 0:
#         i += 2
#     if i == 1:
#         continue
#     if i == 2 or i == 3:
#         print('переменная равна 2 или 3')
#     elif i in [4,5,6]:
#         print('переменная равная 4,5 или 6')
#     else:
#         break

# 6)
# str = 'Привет всем изучающим Python!'
# value = input()
# for i in str:
#     if i == value:
#         index = str.find(value)
#         print(f'Буква "{value}" есть в строке под {index} индексом')
#         break
# else:
#     print(f"Буквы '{value}' нет в указанной строке")

#7)
# value = 2
# for i in range(10, -1, -1):
#     value *= i
#     print(i, value)

#8)
# value = 0
# while value < 1000:
#     if value == 0:
#         value += 20
#     elif value // 2 > 1:
#         value += 100
#     else:
#         value -= 1
#     print(value)

# 9)
# value = 0
# for i in range(10):
#     for j in range(10):
#         if i != j:
#             value += j
#         else:
#             pass
# print(value)

# 10)
# numbers = [1, 2, 3, 4, 4, 5, 6]
# flag = False
# for value in numbers:
#     if value % 5 == 0:
#         flag = True
#
# if flag:
#     print('В массиве есть число, которое делится на 5')
# else:
#     print('В массиве нет числа, которое делится на 5')

