import json
from datetime import datetime
# def sort_data_by_datetime():
"""Функция сортровки json файла с данными"""


with open("operations.json", "r", encoding='utf8') as json_file:
    tranzaction_list = json.load(json_file)
    for i in tranzaction_list:
        data = datetime.strptime(i['date'],'%Y-%m-%dT%H:%M:%S.%f')
        print(i)
        # print(type(data))