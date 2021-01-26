# 1) Сгенерировать dict() из списка ключей ниже по формуле (key : key* key).keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ожидаемый результат: {1: 1, 2: 4, 3: 9 …}
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = {}
for key in keys:
    d.setdefault(key, key ** 2)
print(d)
# или
keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = {}
for key in keys:
    d[key] = key ** 2
print(d)

# =======================================================
### Your solutions are correct, however, you may consider dictionary comprehension as well. Thus, it'll look like:
### new_dict = {i: i * i for i in keys}
# =======================================================

# 2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа.
a = [i for i in range(1, 101) if i % 2 == 0]

# 3)Заменить в произвольной строке согласные буквы на гласные.
from random import randint

consonants = 'бвгджзйклмнпрстфхцчшщ'
vowels = 'аоиеёэыуюя'
s = input()
print(''.join([vowels[randint(0, 9)] if i in consonants else i for i in s ]))

# =======================================================
### Do not forget that case matters. You may add capitalized letters to the initial 'vowels' and 'consonants'
# arrays or use the lower() method to convert the input.
# =======================================================

# 4)Дан массив чисел. [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
# 4.1) убрать из него повторяющиеся элементы
lis = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
a = list(set(lis))  # если не нужно соблюдать последовательность
# или
b = []
for i in lis:
    if i not in b:
        b.append(i)
# 4.2) вывести 3 наибольших числа из исходного массива
lis = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
a = []
while len(a) < 3:
    a.append(max(lis))
    lis.remove(max(lis))
print(*a)

# =======================================================
### Your method works. Also, it is possible to sort the initial array and use slicing.
# =======================================================

# 4.3) вывести индекс минимального элемента массива
lis = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
print(lis.index(min(lis)))
# 4.4) вывести исходный массив в обратном порядке
lis = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
lis.reverse()
print(lis)

# 5) Найти общие ключи в двух словарях:
dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}
print([key for key in dict_two if key in dict_one])

# 6)Дан массив из словарей
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# 6.1) отсортировать массив из словарей по значению ключа ‘age'
from pprint import pprint
pprint(sorted(data, key=lambda x: x['age']))

# 6.2) сгруппировать данные по значению ключа 'city'
result = {}
for i in data:
    if i.get('city') not in result:
        result.setdefault(i.pop('city'), [i])
    else:
        result[i.pop('city')].append(i)

pprint(result)

# вывод должен быть такого вида :
result = {
    'Kiev': [
        {'name': 'Viktor', 'age': 30},
        {'name': 'Andrey', 'age': 34}],

    'Dnepr': [{'name': 'Maksim', 'age': 20},
              {'name': 'Artem', 'age': 50}],
    'Lviv': [{'name': 'Vladimir', 'age': 32},
             {'name': 'Dmitriy', 'age': 21}]
}


# =======================================================
# 7) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:

def most_frequent(list_var):
    a = [(list_var.count(i), i) for i in set(list_var)]
    return max(a)[1]


most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'


# =======================================================
# 8) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.
def mult(n):
    pr = 1
    for i in str(n):
        if int(i) != 0:
        # =======================================================
        ### if int(i):
        # =======================================================
            pr *= int(i)
    return pr
print(mult(123405))
# или
n = 123405
pr = 1
while n > 0:
    if n % 10 != 0:
    # =======================================================
    ### if n % 10:
    # =======================================================
        pr *= n % 10
    n = n // 10
print(pr)


# =======================================================
# 9) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.
def some_function(array, n):
    if len(array) > abs(n) or n == -len(array):
        return array[n] ** n
    return -1

print(some_function([10, 11, 2, 3, 5, 8, 23], -7))

# =======================================================
### Seems like the function doesn't work correctly. In your case, if we have a list of 7 elements and the number is -7
# (that is out of list range, the index og the last element is 6), the function should return -1 but not 1e-07
# =======================================================

# или
def some_function(array, n):
        return array[n] ** n if len(array) > n and len(array) >= abs(n) else -1

print(some_function([10, 11, 2, 3, 5, 8, 23], -7))
# =======================================================
### This function works correctly with positive numbers.
# =======================================================


# =======================================================
# 10) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.
a = input().split()
count = 0
res = 'No'
for i in a:
    if i.isalpha():
        count += 1
        if count == 3:
            res = 'Yes'
            break
    else:
        count = 0
print(res)

# =======================================================
### This comment is more like general recommendation. It's a good practice to call the variables, functions and methods
# with understandable names. It makes your code easier to read and will help you to work with it in the future without
# recalling why the variable is called, for instance, a. It would be better to create a list that is called
# 'sorted_list', 'reversed_list' rather than 'lis', for example.
# =======================================================