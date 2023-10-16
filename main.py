# 1)
# inp = (map(int, input().split()))
# lst = list(inp)
# print(lst)
# print(tuple(lst))

# 2)
# def main(input_tuple, el):
#     if el in input_tuple:
#         index = input_tuple.index(el)
#         new_tuple = input_tuple[:index] + input_tuple[index+1:]
#         return new_tuple
#     else:
#         return input_tuple
#
# test_tuple1 = (1, 2, 3)
# test_tuple2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
# test_tuple3 = (2, 4, 6, 6, 4, 2)
#
# res1 = main(test_tuple1, 1)
# res2 = main(test_tuple2, 3)
# res3 = main(test_tuple3, 9)
#
# print(res1, res2, res3, sep='\n')

# 3)
# import random
#
#
# def count_digits(s):
#     digit_count = {}
#     for digit in s:
#         if digit in digit_count:
#             digit_count[digit] += 1
#         else:
#             digit_count[digit] = 1
#     most_common = sorted(digit_count.items(), key=lambda x: (-x[1], x[0]))[:3]
#     return {k: v for k, v in most_common}
#
#
# s = ''.join([str(random.randint(0, 9)) for _ in range(15)])
#
# digit_count = count_digits(s)
#
# winner = max(digit_count, key=digit_count.get)
#
# print("Random string of digits:", s)
# print("Digit count:", digit_count)
# print("Winner:", winner)

# 4)
# def main(input_tuple, el):
#     if el in input_tuple:
#         start = input_tuple.index(el)
#         count = input_tuple.count(el)
#
#         if count == 1:
#             return input_tuple[start:]
#         elif count >= 2:
#             end = input_tuple.index(el, start + 1)
#             return input_tuple[start:end + 1]
#         else:
#             return input_tuple
#
#
# test1 = (1, 2, 4)
# test2 = (1, 8, 3, 4, 8, 8, 9, 2)
# test3 = (1, 2, 8, 5, 1, 2, 9)
#
#
# res1 = main(test1, 8)
# res2 = main(test2, 8)
# res3 = main(test3, 8)
#
# print(res1, res2, res3, sep='\n')

# 5)
# Задача: Нужно подсичтать, сколько слов начинаются с каждой буквы алфавита.
# Функция будет принимать список слов и возвращать словарь, в котором ключами будут буквы алфавита, а значениями - количество слов, начинающихся с этой буквы.

# def main(word_list):
#     letter_count = {}
#     for word in word_list:
#         if word:
#             initial_letter = word[0].lower()
#             letter_count[initial_letter] = letter_count.get(initial_letter, 0) + 1
#     return letter_count
#
# # Тесты
# lst1 = ["apple", "banana", "cherry", "date", "apricot"]
# res1 = main(lst1)
# print(res1)
#
# lst2 = ["cat", "dog", "elephant", "fox", "volf"]
# res2 = main(lst2)
# print(res2)
#
# lst3 = ["apple", "banana", "cherry", "date", "apricot", "berry"]
# res3 = main(lst3)
# print(res3)

