# Given a list, write a Python program to swap first and last element of the list.

list_example = [1, 4, 9, 16, 25]
list_size = len(list_example)

# print list before swappint
print(list_example)

temp = list_example[0]
list_example[0] = list_example[list_size - 1]
list_example[list_size - 1] = temp

#print list after swapping
print(list_example)
