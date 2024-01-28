import json
from datetime import datetime

# with open("operations.json", "r", encoding='utf8') as file:
#     operations = json.load(file)
#     operations_sorted_data = []
#     for item in operations:
#         if item.get('id') is not None:
#             operations_sorted_data.append(item)
#     print(operations_sorted_data)
#     operations_sorted_data.sort(key='date', reverse=True)


with open("data/operations.json", "r", encoding='utf8') as file:
    operations = json.load(file)
operations_sort = [item for item in operations if item.get('state') == "EXECUTED" and item.get('from') is not None]
operations_sort.sort(key=lambda x: x.get('date'), reverse=True)

result_operations = []
for item in operations_sort[0:5]:
    result_operations.append(item)

print(result_operations)




