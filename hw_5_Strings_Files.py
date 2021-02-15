from string import punctuation


# 1)Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.

def remove_words_in_line(line):
    """This function removes all words from a string containing 3 to 5 characters,
    in this case, only an even number of such words is deleted."""
    last_word = ''
    count_word = 0
    new_line = []
    index_last_word = None
    for word in line:
        word_without_punct = remove_punctuation(word)  # убираем знаки пунктуации
        if 3 <= len(word_without_punct) <= 5:
            last_word = word  # с учетом знаков пунктуации
            count_word += 1
            index_last_word = line.index(word, count_word + len(new_line) - 1)  # ндекс с учетом одинаковых слов
        else:
            new_line.append(word)  # с учетом знаков пунктуации
    if count_word % 2:
        new_line.insert(index_last_word - count_word + 1, last_word)  # крайнее нечетное слово вставляем в строку под
        # нужным индексом с учетом удаленных слов
    return new_line


def remove_punctuation(word):
    """This function removes punctuation marks from words"""
    for punct in punctuation:
        if punct in word:
            word = word.replace(punct, '')
    return word


def remove_words_in_file(file_name):
    """This function removes from a text file all words containing
    from 3 to 5 characters, while only an even number of such words
    is removed from each line"""
    with open(file_name) as file:
        for line in file:
            words = line.split()
            words_without_3_5 = remove_words_in_line(words)
            with open('copy_' + file_name, 'a+') as new_file:
                new_file.write(' '.join(words_without_3_5) + '\n')


remove_words_in_file('test.txt')


# 2)Текстовый файл содержит записи о телефонах и их владельцах. Переписать в другой файл
# телефоны тех владельцев, фамилии которых начинаются с букв К и С.

def get_phone_numbers(file_name):
    """This function gets from the file the phone numbers of those owners whose
    surnames begin with the letters K and C and writes them to a new file.
"""

    with open(file_name, encoding='utf-8') as file:
        for line in file:
            elem = line.split()
            if elem[1][0] in 'КС':
                with open('copy_' + file_name, 'a+', encoding='utf-8') as new_file:
                    new_file.write(elem[0] + '\n')


get_phone_numbers('phone_numbers.txt')


# 3) Получить файл, в котором текст выровнен по правому краю путем равномерного добавления пробелов.

def right_aligns_text_in_file(file_name):
    """this function right-aligns text by adding spaces evenly."""
    with open(file_name) as file:
        max_len_line = len(sorted(file.read().split('\n'), key=len)[-1])  # находим размер самой длинной строки
        file.seek(0)
        for line in file:
            with open('new_' + file_name, 'a+') as new_file:
                new_file.write(line.rstrip().rjust(max_len_line) + '\n')  # rstrip удаляет переносы, чтобы последняя
                # строка выровнялась со всеми, так как она не заканчивается переносом


right_aligns_text_in_file('test.txt')


# 4)Дан текстовый файл со статистикой посещения сайта за неделю. Каждая строка содержит ip адрес, время и название дня
# недели (например, 139.18.150.126 23:12:44 sunday). Создайте новый текстовый файл, который бы содержал список ip без
# повторений из первого файла. Для каждого ip укажите количество посещений, наиболее популярный день недели. Последней
# строкой в файле добавьте наиболее популярный отрезок времени в сутках длиной один час в целом для сайта.

def ip_without_repeating(file_name):
    """This function writes to a file statistics of site visits for
    ip - the number of visits and the most popular day of the week."""
    data_ip = {}
    pop_time = []
    with open(file_name) as file:
        for line in file:
            elem = line.split()  # разбиваем строку на елементы по пробелу
            pop_time.append(elem[1])
            if elem[0] not in data_ip:  # если ip нет в словаре, создаем ключ = ip, значение - вложенный словарь,
                data_ip[elem[0]] = {}  # с ключами количества повторений ip и дни посещения сайта
                data_ip[elem[0]]['count'] = 1
                data_ip[elem[0]]['days'] = [elem[2]]
            else:
                data_ip[elem[0]]['count'] += 1
                data_ip[elem[0]]['days'].append(elem[2])
    with open('copy_' + file_name, 'a+') as new_file:
        for ip, data in data_ip.items():
            new_file.write(
                f"IP-{ip}, visits-{data['count']}, Pop day-{sorted(data['days'], key=lambda x: data['days'].count(x))[-1]}\n")
            # сортировка по количеству повторений, берем крайний элемент
        new_file.write(
            f"Pop time-{sorted(pop_time, key=lambda x: int(x.split(':')[0]))[-1][:2]}")  # раздклили время по :
        # и отсортировали по часам


ip_without_repeating('statistics')
