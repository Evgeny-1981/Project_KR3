import pytest
import project_kr3.utils


def test_sort_operations():
    assert str(type(project_kr3.utils.sort_operations())) == "<class 'list'>"


def test_return_last_operations():
    assert project_kr3.utils.return_last_operations([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5]


def test_format_output_date():
    assert project_kr3.utils.format_output_date("2024-01-28T10:50:58.294041") == "28.01.2024"


@pytest.mark.parametrize("number, expected_result", [("Maestro 1111111111111111", "Maestro 1111 11** **** 1111"),
                                                     ("Счет 11111111111111111111", "Счет **1111"),
                                                     ("11111", "Неверный или отсутствует номер/счет")])
def test_format_account_number(number, expected_result):
    assert project_kr3.utils.format_account_number(number) == expected_result
