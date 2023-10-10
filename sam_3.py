# 1)
# num = 1
# for i in range(2):
#     num *= 5
#     num += 1
# print(num)

# 2)
# mes = 'Hello World'
# for let in reversed(mes):
#     print(let)

# 3)
# a = int(input())
# if 0 <= a <= 10:
#     if 0 <= a <= 3:
#         print('число находится в диапазоне от 0 до 3 включительно')
#     elif 3 <= a < 6:
#         print('число находится в диапазоне от 3 до 6')
#     else:
#         print('число находится в диапазоне от 6 до 10 включительно')
# else:
#     print('Нужно ввести число в диапазоне от 0 до 10')

# 4)
# a = input('Введите предложение:')
# print(len(a))
# print(a.lower())
# print(a.count('a'), a.count('e'), a.count('i'), a.count('o'), a.count('u'))
# print(a.replace('ugly', 'beauty'))
# if a.startswith("The") and a.endswith("end"):
#     print("Yes")
# else:
#     print("No")

# 5)
# memory = 'world'
# string = 'hello'
# values = [0, 2, 4, 6, 8, 10]
# counter = 0
# while counter != 10:
#     if counter in values:
#         string = string + ' world'
#         counter += 1
#         print(string)
#         while ' world' not in string:
#             print(memory)
