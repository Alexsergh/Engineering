# 2)
# f = open('input.txt', 'r')
# print(f.readline())
# f.close()

# 3)
# f = open('input.txt', 'r')
# print(f.readlines())
# f.close()

# 4)
# with open('input.txt') as f:
#     print(f.readlines())

# 5)
# with open('input.txt') as f:
#     for line in f:
#         print(line)

# 6)
# with open('input.txt', 'a+') as f:
#     f.write('\nI am student')
#
# with open('input.txt', 'r') as f:
#     print(f.readlines())

# 7)
# lines = ['one', 'two', 'three']
# with open('input.txt', 'w') as f:
#     for line in lines:
#         f.write('\nCycle run ' + line)
#     print('Done!')

# 8)
# import os
#
#
# def main(directory):
#     all_files = os.walk(directory)
#     for catalog in all_files:
#         print(f'Папка {catalog[0]} содержит: ')
#     print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
#     print(f'Файлы: {", ".join([file for file in catalog[2]])}')
#     print('-' * 48)
#
#
# main('C:/Users/Alexandr/Desktop/engineering/lab6')

# 9)
# def main(file):
#     with open(file, encoding='utf-8')as f:
#         words = f.read().split()
#         max_len = len(max(words, key=len))
#         for word in words:
#             if len(word) == max_len:
#                 sought_words = word
#
#         if len(sought_words) == 1:
#             return sought_words[0]
#         return sought_words
#
#
# print(main('input2.txt'))

# 10)
# import csv
# import datetime
# import time
#
# with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['№', 'Секунда', 'Микросекунда'])
#     for line in range(1, 301):
#         writer.writerow([line, datetime.datetime.now().second,
#                          datetime.datetime.now().microsecond])
#         time.sleep(0.01)

