from HW11_TESTS.my_func.file_workers import remove_punctuation, remove_words_in_line, remove_words_in_file, \
    get_phone_numbers
import pytest
import os


@pytest.mark.parametrize('line, expected_result',
                         [(['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaa', 'aa'], ['a', 'aa', 'aa']),
                          (['a', 'aa', 'aaa'], ['a', 'aa', 'aaa']),
                          (['aaa', 'aaaa', 'aaaaa', 'aa', 'aa'], ['aaaaa', 'aa', 'aa']),
                          ([], []),
                          (['aaa'], ['aaa'])])
def test_remove_words_in_line(line, expected_result):
    """Этот тест проверяет, что при передачи списка слов разной длины в функцию она удаляет все слова,
     содержащие от трех до пяти символов, но при этом из списка должно быть удалено только четное количество
     таких слов и возвращает список без этих слов"""
    assert remove_words_in_line(line) == expected_result


@pytest.mark.parametrize('word, expected_result', [('word!', 'word'),
                                                   ('word,', 'word'),
                                                   ('word.', 'word'),
                                                   ('', '')])
def test_remove_punctuation(word, expected_result):
    """Этот тест проверяет удаляет ли функция remove_punctuation
    знаки пунктуации в переданых ей словах"""
    assert remove_punctuation(word) == expected_result


def test_remove_punctuation_returns_str():
    """Этот тест проверяет возвращает ли функция remove_punctuation тип строку после своей работы"""
    assert isinstance(remove_punctuation(''), str)


def test_remove_words_in_line_returns_list():
    """Этот тест проверяет возвращает ли функция remove_words_in_line тип лист после своей работы"""
    assert isinstance(remove_words_in_line([]), list)


def test_remove_words_in_file_except():
    """Этот тест проверяет обрабатывается ли исключение при неверном указании пути"""
    remove_words_in_file('q')


@pytest.fixture()
def clean_res_file():
    """Эта фикстура очищает ризультирующий файл перед записью в него данных"""
    with open('res_file.txt', 'w'):
        pass


def test_remove_words_in_file_path(clean_res_file):
    """Этот тест проверяет создает ли функция remove_words_in_file файл после своей работы"""
    remove_words_in_file('tests/testfile.txt')
    assert os.path.isfile('res_file.txt')


def test_remove_words_in_file(clean_res_file):
    """Этот тест проверяет корректную работу функции remove_words_in_file"""
    test_data = ['function removes a containing\n', '3 to 5 characters, an number of\n', 'is removed line\n']
    remove_words_in_file('tests/testfile.txt')
    with open('res_file.txt') as f_o:
        assert f_o.readlines() == test_data


@pytest.fixture()
def clean_copy_file():
    """Эта фикстура очищает ризультирующий файл перед записью в него данных"""
    with open('copy_phone_numbers.txt', 'w'):
        pass


def test_get_phone_numbers_path(clean_copy_file):
    """Этот тест проверяет создает ли функция get_phone_numbers файл после своей работы"""
    get_phone_numbers('tests/testphone_numbers.txt')
    assert os.path.isfile('copy_phone_numbers.txt')


def test_get_phone_numbers(clean_copy_file):
    """Этот тест проверяет корректную работу функции get_phone_numbers"""
    test_data = ['0968628896\n', '0968628897\n', '0968628899\n']
    get_phone_numbers('tests/testphone_numbers.txt')
    with open('copy_phone_numbers.txt') as f_o:
        assert f_o.readlines() == test_data
