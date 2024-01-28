from datetime import datetime
import pytest
from project_kr3.utils import (sort_operations, return_last_operations,
                               format_output_date, format_account_number)


def test_sort_operations():
    pass


@pytest.mark.parametrize("number, expected_result", [([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3, 4, 5])])
def test_return_last_operations(number, expected_result):
    assert return_last_operations(number) == expected_result


def test_format_output_date():
    assert format_output_date("2019-08-26T10:50:58.294041") == "26.08.2019"


@pytest.mark.parametrize("number, expected_result", [("1111111111111111", " 1111 11** **** 1111"),
                                                     ("11111111111111111111", " **1111"),
                                                     ("1", "Неверный или отсутствует номер/счет")])
def test_format_account_number(number, expected_result):
    assert format_account_number(number) == expected_result
