# 1)
# req = int(input('Введите номер кабинета: '))
#
# dic = {
#     101: {'key': 1234, 'access': True},
#     102: {'key': 1337, 'access': True},
#     103: {'key': 8943, 'access': True},
#     104: {'key': 5555, 'access': False},
#     None: {'key': None, 'access': False}
# }
#
# res = dic.get(req)
# if not res:
#     res = dic[None]
# key = res.get('key')
# access = res.get('access')
#
# print(key, access)

# 2)
# from pprint import pprint
#
# dic = {'first': 'so easy'}
#
#
# def dict_maker(**kwargs):
#     dic.update(**kwargs)
#
#
# dict_maker(a1=1, a2=20, a3=54, a4=13)
# dict_maker(name='Александр', age=19, weight=65, eyes_color='green')
# pprint(dic)

# 3)
# inp = 'helloworld'
# res = tuple(inp)
# print(res, list(res), sep='\n')

# 4)
# def info(name, age, company='unnamed'):
#     print(f'Имя: {name}, Возраст: {age}, Компания: {company}')
#
#
# tom = ('Григорий', 22)
# info(*tom)
#
# bob = ("Георгий", 41, "Yandex")
# info(*bob)

# 5)
# def tup(tpl):
#     for el in tpl:
#         if not isinstance(el,int):
#             return tpl
#     return tuple(sorted(tpl))
#
#
# if __name__ =='__main__':
#     print(tup((5, 5, 3, 1, 9)))
#     print(tup((5, 5, 3, '1', 9)))

