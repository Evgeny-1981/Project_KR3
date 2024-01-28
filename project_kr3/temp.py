import json
from datetime import datetime

with open("operations.json", "r", encoding='utf8') as file:
    operations = json.load(file)
    operations_sorted_data = []
    for item in operations:
        if item.get('id') is not None:
            operations_sorted_data.append(item)
    print(operations_sorted_data)
    operations_sorted_data.sort(key='date', reverse=True)






