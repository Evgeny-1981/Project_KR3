import json


def sort_operations():
    """Функция сортирует json файл и возвращает последние пять операций"""
    result_operations = []
    with open("operations.json", "r", encoding='utf8') as json_file:
        operations = json.load(json_file)
        operations_sort = [item for item in operations if item.get('state') == "EXECUTED" and item.get('from') is not None]
        operations_sort.sort(key=lambda x: x.get('date'), reverse=True)
    for item in operations_sort[0:5]:
        result_operations.append(item)

    return result_operations
