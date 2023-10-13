# 1)
# a = {'apple', 'banana', 'kiwi', 'orange','grapefruit'}
# b = {'blueberry', 'kiwi', 'starwberry', 'banana'}
# print(a-b)

# 2)
# a = set('123456')
# print(a)
# for i in range(1, 5):
#     a.add(i)
# print(a)
#
# b = frozenset('123456')
# print(b)
# for z in range(1, 5):
#     b.add(z)
# print(b)

# 3)
# lst = [1, 2, 3, 4, 5, 6, 7]
# first = lst[0]
# lst[0] = lst[-1]
# lst[-1] = first
# print(lst)

# 4)
# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(lst[2:6])

# 5)
# def useless(lst):
#     return max(lst) / len(lst)
#
#
# print(useless([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# print(useless([42, 646, 97, 451, 787, 3]))
# print(useless([1223, 4567, 890, 987, 654, 321]))

# 6)
# sup = ['Человек-паук', 'железный человек', 'халк']
# Alex, Ivan, Pavel = sup
#
# print('Alex - ', Alex)
# print('Ivan - ', Ivan)
# print('Pavel - ', Pavel)

#7)
# lst = [1, 3, 5, 7, 9, 11, 13, 5, 2, 4, 6, 0]
# lst.sort()
# print(f"Отсортированный список: {lst}")
# lst.pop(0)
# print(f"отсортированный список без наименьшего элемента: {lst}")

#8)
# from random import randint
# def lst():
#     a = [randint(1, 100) * randint(3, 10)]
#     return a
#
#
# if __name__ == '__main__':
#     res = []
#     for i in range(randint(1, 5)):
#         res.append((lst()))
#     print(res)

#9)
# def superset(set_1, set_2):
#     if set_1 > set_2:
#         print(f'Объект {set_1} является чистым супермножеством')
#     elif set_1 < set_2:
#         print(f'Объект {set_2} является чистым супермножеством')
#     elif set_1 == set_2:
#         print('Множества равны')
#     else:
#         print("супермножество не обнаружено")
#
# if __name__ == '__main__':
#     superset({1, 2, 3, 4, 5, 6}, {5, 6})
#     superset({1, 2, 3, 4, 5, 6}, {5, 3, 1, 4, 2, 6})
#     superset({5, 6}, {5, 3, 1, 4, 6, 3})
#     superset({10, 50}, {5, 6})

#10)
# lst = [1, 2, 3, 4, 5, 6]
# print(lst[::-1])
