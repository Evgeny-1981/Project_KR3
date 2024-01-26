import json


def sort_operations():
    """Функция сортирует json файл"""


    with open("operations.json", "r", encoding='utf8') as json_file:
        operations = json.load(json_file)
    operations_sort = [item for item in operations if item.get('state') == "EXECUTED" and item.get('from') is not None]
    operations_sort.sort(key=lambda x: x.get('date'), reverse=True)

    return operations_sort


def return_last_operations(operations_sort):
    """Функция возвращает список последних 5 операций"""


    result_operations = []
    for item in operations_sort[0:5]:
        result_operations.append(item)

    return result_operations


def format_output_data():
    pass
def format_card_number():
    pass

def format_card_account():
    pass
