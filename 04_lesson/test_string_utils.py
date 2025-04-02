import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),                  # Стандартный случай
    ("hello world", "Hello world"),        # Строка с пробелом
    ("python", "Python"),                  # Одно слово
    ("123abc", "123abc"),                  # Числа в начале
    ("04 апреля 2023", "04 апреля 2023"),  # Дата
], ids=["standard", "with_space", "single_word", "numeric", "date"])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),            # Пустая строка
    ("   ", "   "),      # Строка из пробелов
    (None, None),        # None (упадёт с AttributeError)
], ids=["empty", "whitespace", "none"])
def test_capitalize_negative(input_str, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            utils.capitalize(input_str)
    else:
        assert utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),       # Пробелы в начале
    ("skypro", "skypro"),          # Без пробелов
    ("  hello  ", "hello  "),      # Пробелы только в начале
], ids=["spaces", "no_spaces", "mixed_spaces"])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                      # Пустая строка
    (None, None),                  # None (упадёт с AttributeError)
], ids=["empty", "none"])
def test_trim_negative(input_str, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            utils.trim(input_str)
    else:
        assert utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),        # Символ есть
    ("SkyPro", "Pro", True),      # Подстрока есть
    ("123", "2", True),           # Число как строка
], ids=["char", "substring", "numeric"])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),       # Символа нет
    ("", "a", False),             # Пустая строка
    ("   ", " ", True),           # Пробел в строке из пробелов
    (None, "a", False),           # None (упадёт с AttributeError)
], ids=["not_found", "empty", "whitespace", "none"])
def test_contains_negative(string, symbol, expected):
    if string is None:
        with pytest.raises(AttributeError):
            utils.contains(string, symbol)
    else:
        assert utils.contains(string, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),     # Удаление символа
    ("SkyPro", "Pro", "Sky"),     # Удаление подстроки
    ("12345", "3", "1245"),       # Числа как строка
], ids=["char", "substring", "numeric"])
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),    # Символа нет
    ("", "a", ""),                # Пустая строка
    (None, "a", None),            # None (упадёт с AttributeError)
], ids=["not_found", "empty", "none"])
def test_delete_symbol_negative(string, symbol, expected):
    if string is None:
        with pytest.raises(AttributeError):
            utils.delete_symbol(string, symbol)
    else:
        assert utils.delete_symbol(string, symbol) == expected
