import datetime
from project_kr3.utils import (sort_operations, return_last_operations)


operations_sort = sort_operations()
last_operations = return_last_operations(operations_sort)
for item in last_operations:
    print(f"{item['date']} {item['description']}\n{item['from']} -> {item['to']}\n"
          f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n")
