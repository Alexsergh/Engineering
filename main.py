# 1)
# count = 0
# word_count = {}
#
# lst = []
# with open('sam7.1.txt', 'r', encoding='utf-8') as f:
#     lines = f.read().split()
#     count += len(lines)
# print(count)
#
# for i in lines:
#     if i in word_count:
#         word_count[i] += 1
#     else:
#         word_count[i] = 1
# print(max(word_count, key=word_count.get))


# 2)
# import csv
#
#
# def add_expense():
#     with open('expenses.csv', 'a', newline='') as f:
#         writer = csv.writer(f)
#         date = input("Введите дату (ГГГГ-MM-ДД): ")
#         category = input("Введите расход: ")
#         amount = input("введите цену расхода: ")
#         writer.writerow([date, category, amount])
#
#
# def show_expenses():
#     with open('expenses.csv', 'r') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             print(row)
#
#
# while True:
#     print("1. Ввести расход")
#     print("2. Показать расходы")
#     print("3. Выход")
#     choice = input("Выберете из вышеперечисленного: ")
#     if choice == '1':
#         add_expense()
#     elif choice == '2':
#         show_expenses()
#     elif choice == '3':
#         break
#     else:
#         print("Invalid choice")

# 3)
# with open('input.txt', 'r') as f:
#     text = f.read()
#
# len_lines = 0
# lines = text.split('\n')
# for i in lines:
#     if i:
#         len_lines += 1
#
#
# len_words = len(text.split())
#
# count_let = 0
# for i in text:
#     if i.isalpha():
#         count_let += 1
#
# print(count_let, ' letters')
# print(len_words, " words")
# print(len_lines, ' lines')

# 4)
# sen = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
# sen2 = sen.lower()
# with open('input2.txt', 'r') as f:
#     text = f.read().split()
#
# for i in text:
#     sen2 = sen2.replace(i, '*' * len(i))
#
# print(sen2)

# 5) Создайте програму, которая будет выводить самое длинное слово в файле и его длину.
# with open('text.txt', 'r') as file:
#     text = file.read()
#
# sen = text.split()
#
# max_word = max(sen, key=len)
# print(max_word, len(max_word), sep='\n')

