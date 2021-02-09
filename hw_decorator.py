from functools import wraps
from datetime import datetime


# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.
def remainder_of_division(f):
    @wraps(f)
    def wrapper():
        divider = f()
        rez = 100 % int(divider)
        if rez:
            return f"Bad news guys, we got {rez}"
        return "We are OK!"

    return wrapper

@remainder_of_division
def func():
    return input("введите число: ")

print(func())

# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

def check_type(func):
    @wraps(func)
    def wrapper(arg):
        if isinstance(arg, int):
            return func(arg)
        elif isinstance(arg, str):
            return 'ValueError: string type is not supported'
        return 'ValueError: unknown type'

    return wrapper


@check_type
def func1(arg):
    return arg



print(func1("sfffa"))
print(func1(10.0))

# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.

def memoize(func):
    cache = {}
    count_func_executed = 0
    count_used_cache = 0

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            nonlocal count_used_cache
            count_used_cache += 1
            print(f'Used cache with counter = {count_used_cache}. Value = {cache[args]}')
        else:
            nonlocal count_func_executed
            cache[args] = func(*args)
            count_func_executed += 1
            print(f'Function executed with counter = {count_func_executed}, function result = {cache[args]}')

    return wrapper


@memoize
def factorial(n):
    """This function calculates the factorial"""
    pr, factor = 1, 1
    while factor <= n:
        pr *= factor
        factor += 1
    return pr


factorial(5)
factorial(4)
factorial(5)



def timeit(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        res_string = f'{func.__name__} - {result} - {datetime.now() - start}'
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(res_string + '\n')

        return res_string

    return inner


@timeit
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


@timeit
def two(n):
    l = [i for i in range(n) if i % 2 == 0]
    return l


print(one(1000))
print(two(1000))