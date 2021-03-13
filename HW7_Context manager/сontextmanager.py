import os
from contextlib import contextmanager
from time import perf_counter, sleep


# Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
# Так же ваш объект должен принимать исключение которое он будет подавлять Если флаг об исключении отсутствует,
# исключение должно быть поднято.

class Cd:
    """This context manager navigates in and out of the directory it accepts as input"""

    def __init__(self, path, *exc):
        self._path = path
        self._exc = exc

    def __enter__(self):
        self._saved_cwd = os.getcwd()
        try:
            os.chdir(self._path)
        except self._exc:
            print('Не верно указан путь к файлу')

    def __exit__(self, *exc_info):
        os.chdir(self._saved_cwd)


print(os.getcwd())
path = r'C:1/Users/Zver/PycharmProjects'

with Cd(path, OSError):
    print(os.getcwd())


# Описать задачу выше но уже с использованием @contexmanager

@contextmanager
def dir(path, *exc):
    saved_cwd = os.getcwd()
    try:
        os.chdir(path)
    except exc:
        print('Не верно указан путь к файлу')
    yield
    os.chdir(saved_cwd)


print(os.getcwd())
path = r'C:/Users/Zver/PycharmProjects'

with dir(path, FileNotFoundError):
    print(os.getcwd())


# 3.Создать менеджер контекста который будет подсчитывать время выполнения вашей функции

class Timer:
    """This context manager counts the execution time of the function"""

    def __enter__(self):
        self._start = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Время выполнения функции - {perf_counter() - self._start}')


def test_func():
    sleep(2)


with Timer():
    test_func()
