import json
import pathlib
from pathlib import Path
from datetime import datetime


def sort_operations():
    """Функция сортирует json файл"""

    path = Path(pathlib.Path.home(), 'PycharmProjects', 'project_KR3', 'project_kr3', 'data', 'operations.json')
    with open(path, "r", encoding='utf8') as file:
        operations = json.load(file)
    operations_sort = [item for item in operations if item.get('state') == "EXECUTED" and item.get('from') is not None]
    operations_sort.sort(key=lambda x: x.get('date'), reverse=True)

    return operations_sort


def return_last_operations(operations_sort):
    """Функция возвращает список последних 5 операций"""

    result_operations = []
    for item in operations_sort[0:5]:
        result_operations.append(item)

    return result_operations


def format_output_date(item):
    """Функция преобразует доту в формат %d.%m.%Y и возвращает полуенное значение"""

    output_data = datetime.strftime(datetime.strptime(item.split('T')[0], '%Y-%m-%d'), '%d.%m.%Y')
    return output_data


def format_account_number(item):
    """Функция возвращает номер карты/счета в приватном виде"""

    account_number = item.split()[-1]
    name = ' '.join(item.split()[:-1])
    if len(account_number) == 16:
        account_number = name + ' ' + account_number[0:4] + ' ' + account_number[5:7] + '** **** ' + account_number[-4:]
    elif len(account_number) == 20:
        account_number = name + ' ' + '**' + account_number[-4:]
    else:
        account_number = 'Неверный или отсутствует номер/счет'

    return account_number
