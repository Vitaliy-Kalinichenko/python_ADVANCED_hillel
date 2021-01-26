# from pprint import pprint
# data = [
#     {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
#     {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
#     {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
#     {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
#     {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
#     {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
#
# result = {}
# for i in data:
#     if i.get('city') not in result:
#         result.setdefault(i.pop('city'), [i])
#     else:
#         result[i.pop('city')].append(i)
#
# pprint(result)

from random import randint

consonants = 'бвгджзйклмнпрстфхцчшщ'
vowels = 'аоиеёэыуюя'
s = input()
print(''.join([vowels[randint(0, 9)] if i in consonants else i for i in s ]))