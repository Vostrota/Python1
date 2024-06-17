from typing import Literal
import pytest
from string_utils import StringUtils

utils = StringUtils()

"""capitilize Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст"""

def test_capitilize():
    #позитивный сценарий
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("добрый день!") == "Добрый день!"
    assert utils.capitilize("79833059032") == "79833059032"
    #негативный сценарий
    assert utils.capitilize("") == ""
    assert utils.capitilize("  ") == "  "
    assert utils.capitilize("465547номер") == "465547номер"


"""trim Принимает на вход текст и удаляет пробелы в начале, если они есть"""

def test_trim():
#позитивный сценарий
    assert utils.trim("  Востротина Влада") == "Востротина Влада"
    assert utils.trim("   skypro") == "skypro" 
    assert utils.trim(" добрый день!") == "добрый день!"
#негативный сценарий
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_mumbers():
     assert utils.trim(79833059032) == "79833059032"

@pytest.mark.xfail()
def test_trim_whitespace():
     assert utils.trim(" skypro ") == " skypro "


"""to_list Принимает на вход текст с разделителем и возвращает список строк"""

@pytest.mark.parametrize('string, delimeter, result', [
# позитивный сценарий
     ("математика,русский язык,биология", ",", ["математика", "русский язык", "биология"]),
     ("7,983,305,90,32", ",", ["7", "983", "305", "90", "32"]),
     ("!.@.#.$.%.^", ".", ["!", "@", "#", "$", "%", "^"]),
#негативный сценарий
     ("", None, []),
     ("7,9 8 3,3 0 5,90,32", ",", ["7", "9 8 3", "3 0 5", "90", "32"]),
 ])
def test_to_list(string: Literal['математика,русский язык,биология'] | Literal['7,983,305,90,32'] | Literal['!.@.#.$.%.^'] | Literal[''] | Literal['7,9 8 3,3 0 5,90,32'], delimeter: None | Literal[','] | Literal['.'], result: list[str]):
     if delimeter is None:
         res = utils.to_list(string)
     else:
         res = utils.to_list(string, delimeter)
     assert res == result


"""contains  Возвращает `True`, если строка содержит искомый символ и `False` - если нет """

@pytest.mark.parametrize('string, symbol, result', [
# позитивный сценарий
     ("Востротина", "В", True),
     ("Vlada", "V", True),
     ("79833059032", "5", True),
     ("Москва-сити", "-", True),
#негативный сценарий
     ("добрый день", "!", False),
     ("skypro", "z", False),
     ("79833059032", "V", False),
     ("", "45", False),
    ])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result


"""delete_symbol Удаляет все подстроки из переданной строки"""

@pytest.mark.parametrize('string, symbol, result', [
# позитивный сценарий
     ("Влада", "В", "лада"),
     ("Vlada", "V", "lada"),
     ("Москва-сити", "-", "Москвасити"),
     ("79833059032", "7983305", "9032"),
#негативный сценарий
     ("skypro", "", "skypro"),
     ("skypro", "z", "skypro"),
     ("", "z", ""),
     ("", "", ""),
 ])
def test_delete_symbol(string, symbol, result):
     res = utils.delete_symbol(string, symbol)
     assert res == result


"""starts_with Возвращает `True`, если строка начинается с заданного символа и `False` - если нет"""

@pytest.mark.parametrize('string, symbol, result', [
# позитивный сценарий
    ("Влада", "В", True),
    ("Vlada", "V", True),
    ("Москва-сити", "М", True),
    ("79833059032", "7", True),
#негативный сценарий
    ("Влада", "в", False),
    ("Vlada", "v", False),
    ("Москва-сити", "_", False),
    ("", "@", False),
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result


"""end_with Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет"""

@pytest.mark.parametrize('string, symbol, result', [
# позитивный сценарий
    ("Влада", "а", True),
    ("Vlada", "a", True),
    ("Москва-сити", "и", True),
    ("79833059032", "2", True),
#негативный сценарий
    ("Влада", "v", False),
    ("Vlada", "v", False),
    ("Москва-сити", "_", False),
    ("Москва-сити", "И", False),
    ("", "@", False),
 ])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result


"""is_empty Возвращает `True`, если строка пустая и `False` - если нет"""

@pytest.mark.parametrize('string, result', [
# позитивный сценарий
     ("", True),
     (" ", True),
     ("     ", True),
#негативный сценарий
     ("Vlada", False),
     (" skypro", False),
     ("79833059032", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


"""list_to_string Преобразует список элементов в строку с указанным разделителем"""

@pytest.mark.parametrize('lst, joiner, result', [
# позитивный сценарий
     (["V", "l", "a", "d", "a"], "'", "V'l'a'd'a"),
     (["7", "9", "8", "3", "3", "0", "5", "9", "0", "3", "2"], "", "79833059032"),
#негативный сценарий
    ([], None, ""),
    ([], "'", ""),
    ([], "skypro", ""),
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result