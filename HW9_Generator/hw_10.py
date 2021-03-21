# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем

def read_file_line_by_line(file_name):
    """This generator outputs unique lines from a file line by line."""
    with open(file_name) as f:
        unique_strings = []
        while True:
            line = f.readline()
            if line not in unique_strings:
                unique_strings.append(line)
                yield line
            elif not line:
                break


gen = read_file_line_by_line('test.txt')

# for line in gen:
#     print(line, end='')


# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

# Структура пайплайна:
# ```
from functools import wraps
from time import sleep


def coroutine(func):  # инициализация корутин
    @wraps(func)
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g

    return wrapper


@coroutine
def grep(pattern, printer):  # фильтер, проверяем полученную строку на наличие в ней pattern
    while True:
        line = yield  # получаем строку от dispenser
        if pattern in line:
            printer.send(line)  # если pattern в строке есть, отправляем на печать


@coroutine
def printer():  # Сопрограмма, которая получает данные от корутин grep и выводит их на печать
    while True:
        line = yield
        print(line, end='')


@coroutine
def dispenser(greps):  # получает поток строк и разветвляет поток на несколько корутин
    while True:
        line = yield  # получаем данные и отправляем их в цикле дальше в несколько корутин
        for grep in greps:
            grep.send(line)


def follow(file, dispenser):  # получаем файл, читаем строки и отправляем их в dispenser
    file.seek(0, 2)  # идем в конец файла
    while True:
        line = file.readline()
        if not line:
            sleep(0.1)
            continue
        dispenser.send(line)


# ```
#
# Каждый grep следит за определенной сигнатурой
#
# Как это будет работать:
#
# ```
f_open = open('log.txt')  # подключаемся к файлу
follow(f_open,
       # делегируем ивенты
       dispenser([
           grep('python', printer()),  # отслеживаем
           grep('is', printer()),  # заданные
           grep('great', printer()),  # сигнатуры
       ])
       )


# ```
# Как только в файл запишется что-то содержащее ('python', 'is', 'great') мы сможем это увидеть
#
# Итоговая реализация фактически будет асинхронным ивент хендлером, с отсутствием блокирующих операций.
#
# Если все плохо - план Б лекция Дэвида Бизли
# [warning] решение там тоже есть :)
# https://www.dabeaz.com/coroutines/Coroutines.pdf


# Задача-3 (упрощенный вариант делаете его если задача 2 показалась сложной)
# Вам нужно создать pipeline (конвеер, подобие pipeline в unix https://en.wikipedia.org/wiki/Pipeline_(Unix)).
#
# Схема пайплайна :
# source ---send()--->coroutine1------send()---->coroutine2----send()------>sink
#
# Все что вам нужно сделать это выводить сообщение о том что было получено на каждом шаге и обработку ошибки GeneratorExit.
#
# Например: Ваш source (это не корутина, не генератор и прочее, это просто функция ) в ней опеделите цикл из 10 элементов
# которые будут по цепочке отправлены в каждый из корутин и в каждом из корутив вызвано сообщение о полученном элементе.
# После вызова .close() вы должны в каждом из корутин вывести сообщение что работа завершена.

def source(coroutine):  # источник пайплайна, генрим элементы и отпрваляем в корутины
    for i in range(10):
        coroutine.send(i)
    coroutine.close()


@coroutine
def coroutine1(coroutine): # принимает данные, обрабатывает и посылает в следующую корутину
    try:
        while True:
            data = yield
            print(f'{coroutine1.__name__} получил элемент:', data)
            coroutine.send(data)
    except GeneratorExit:
        coroutine.close()
        print(f'{coroutine1.__name__} Работа завершена')


@coroutine
def coroutine2(sink):
    try:
        while True:
            data = yield
            print(f'{coroutine2.__name__} получил элемент:', data)
            sink.send(data)
    except GeneratorExit:
        sink.close()
        print(f'{coroutine2.__name__} Работа завершена')


@coroutine
def sink():  # дно пайплайна
    try:
        while True:
            data = yield
            print(f'{sink.__name__} получил элемент:', data)
    except GeneratorExit:
        print(f'{sink.__name__} Работа завершена')


pipeline = source(coroutine1(coroutine2(sink())))
