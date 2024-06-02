# Generates list for divisors against a number
def get_divisor_list(n):
    y = range(1, n)
    range_list = []
    for elem in y:
        if(n%elem == 0):
            range_list.append(elem)
    return range_list

# Generates dictonary
# Key = Number
# Value = Count of divisors
def get_divisor_dictonary(n):
    divisor_dictonary[n] = len(get_divisor_list(n))
    return divisor_dictonary

input_number = int(input("Enter the upper range number: "))
divisor_dictonary = {}
x = range(2, input_number+1)

for element in x:
    output_list = []
    output_list.append(element)
    output_list.append(get_divisor_list(element))
    print(output_list)
    get_divisor_dictonary(element)

max_divisor_number = max(divisor_dictonary, key = divisor_dictonary.get)

print(divisor_dictonary)
print(max_divisor_number)
print(divisor_dictonary[max_divisor_number])