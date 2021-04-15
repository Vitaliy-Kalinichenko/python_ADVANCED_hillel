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

