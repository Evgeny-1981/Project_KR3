import json
from datetime import datetime


# def sort_data_by_datetime():
"""Функция сортровки json файла с данными"""

    # list_data = []
with open("operations.json", "r", encoding='utf8') as json_file:
    data = json.loads()
    data_list = sorted(data, key=lambda x:datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
print(data)

