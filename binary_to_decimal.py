import math as m

def binary_to_decimal(n, binary_input):
    binary_int = int(binary_input)
    i = 0
    decimal_output = 0
    while i in range(n):
        rem = binary_int%10
        decimal_output = decimal_output + (rem*m.pow(2,i))
        i = i+1
        binary_int = binary_int//10
    return int(decimal_output)

def max_binary_number(n, binary_input):
    cyclic_decimal_dictonary = {}
    for j in range(n):
        cyc1 = cyclicshift(binary_input)
        cyclic_decimal_dictonary[cyc1] = binary_to_decimal(n, cyc1)
        j = j+1
        binary_input = cyc1
    print(cyclic_decimal_dictonary)
    max_key = max(cyclic_decimal_dictonary, key=cyclic_decimal_dictonary.get)
    print(max_key)


def cyclicshift(input_binary):
    r_rot = 1
    l_rot = 0
    output_binary = (input_binary * 3)[len(input_binary) + r_rot : 2 * len(input_binary) + r_rot]
    return output_binary


binary_input = input()
n = len(binary_input)
max_binary_number(n, binary_input)

