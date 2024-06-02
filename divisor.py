# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

input_number = int(input("Enter number: "))
x = range(1, input_number)
output_list = list()
number_dictonary = {}

for elem in x:
    if(input_number%elem == 0):
        output_list.append(elem)

number_of_divisor = len(output_list)

print(output_list)
print(number_of_divisor)


number_dictonary[input_number] = number_of_divisor
print(number_dictonary)