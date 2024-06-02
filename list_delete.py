from typing import List


list = ['a', 'b', 'c', 'd']

for l in list:
    list.remove(list[len(list)-2])
    print(list)