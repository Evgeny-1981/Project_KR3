from datetime import datetime
import pytest
from project_kr3.utils import (sort_operations, return_last_operations,
                               format_output_date, format_account_number)


def test_sort_operations():
    assert str(type(sort_operations())) == "<class 'list'>"
def test_return_last_operations():
    assert return_last_operations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [1, 2, 3, 4, 5]


def test_format_output_date():
    assert format_output_date("2024-01-28T10:50:58.294041") == "28.01.2024"


@pytest.mark.parametrize("number, expected_result", [("Maestro 1111111111111111", "Maestro 1111 11** **** 1111"),
                                                     ("Счет 11111111111111111111", "Счет **1111"),
                                                     ("11111", "Неверный или отсутствует номер/счет")])
def test_format_account_number(number, expected_result):
    assert format_account_number(number) == expected_result
