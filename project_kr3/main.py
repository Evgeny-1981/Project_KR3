import datetime
from project_kr3.utils import (sort_operations, return_last_operations, format_private_num,
                               format_output_data)


operations = sort_operations()
last_operations = return_last_operations(operations)
for item in last_operations:
    print(f"{format_output_data(item['date'])} {item['description']}\n"
          f"{format_private_num(item['from'])}"
          f" -> {format_private_num(item['to'])}\n"
          f"{item['operationAmount']['amount']}"
          f" {item['operationAmount']['currency']['name']}\n")
