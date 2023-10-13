# №1)
# lst = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,
#        1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666,
#        5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,
#        5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,
#        3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]
# print(f'Всего было выдано {len(lst)} чеков')
#
# print(f'ресторан посетило {len(set(lst))} человек')
#
# print(f'Работник {max(set(lst), key=lst.count)} посетил ресторан больше всех раз')

# №2
# lst = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1,
#        30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
# lst2 = sorted(lst)
#
# print(lst2[0:3])
# print(lst2[-4:-1])
# print(lst[9:])

# №3)
# from math import sqrt
#
# one = [12, 25, 3, 48, 71]
# two = [5, 18, 40, 62, 98]
# three = [4, 21, 37, 56, 84]
#
# max_side1, max_side2, max_side3 = max(one), max(two), max(three)
# min_side1, min_side2, min_side3 = min(one), min(two), min(three)
#
# p_max, p_min = 1/2*(max_side1 + max_side2 + max_side3), 1/2*(min_side1 + min_side2 + min_side3)
#
# S_max = sqrt(p_max*(p_max-max_side1)*(p_max-max_side2)*(p_max-max_side3))
# S_min = sqrt(p_min*(p_min-min_side1)*(p_min-min_side2)*(p_min-min_side3))
#
# print(f'площадь треугольника, стоставленного из максимальных элементов равна {S_max}')
# print(f'площадь треугольника, стоставленного из минимальных элементов равна {S_min}')

# №4
# def main(lst):
#     count = lst.count(2)
#
#     for _ in range(count):
#         lst.remove(2)
#
#     for i in range(len(lst)):
#         if lst[i] == 3:
#             lst[i] = 4
#     return lst
#
# if __name__ == '__main__':
#     lst1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
#     lst2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
#     lst3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
#
#     res1, res2, res3 = main(lst1), main(lst2), main(lst3)
#
#     print(res1, res2, res3, sep='\n')

# №5
# def main(lst):
#     result_set = set()
#
#     for num in lst:
#         count = lst.count(num)  # Подсчитываем количество повторений числа
#
#         if count > 1:
#             # Если число повторяется, добавляем его строковые варианты
#             num_str = str(num)
#             for i in range(1, count + 1):
#                 result_set.add(num_str * i)
#         else:
#             # Если число не повторяется, добавляем его как целое число
#             result_set.add(num)
#
#     return result_set
#
#
# if __name__ == '__main__':
#
#     list_1 = [1, 1, 3, 3, 1]
#     list_2 = [5, 5, 5, 5, 5, 5, 5]
#     list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
#
#     res1, res2, res3 = main(list_1), main(list_2), main(list_3)
#
#     print(res1, res2, res3, sep='\n')

