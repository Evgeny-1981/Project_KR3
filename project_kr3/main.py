import datetime
from project_kr3.utils import(sort_data_by_datetime)
# s1 = "2019-07-12T20:41:47.882230"
# s2 = "2018-12-20T16:43:26.929246"
# d1 = datetime.datetime.strptime(s1, "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')
# d2 = datetime.datetime.strptime(s2, "%Y-%m-%dT%H:%M:%S.%f").strftime('%d.%m.%Y')
#
# print(d1)
# print(d2)

list_data = sort_data_by_datetime()
print(list_data)
