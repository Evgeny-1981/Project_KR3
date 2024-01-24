import datetime
from project_kr3.utils import (sort_operations)

data_sort = sort_operations()
for item in data_sort:
    print(f"{item['date']} {item['description']}\n{item['from']} -> {item['to']}\n"
          f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n")
