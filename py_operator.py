# Examples of Arithmetic Operator
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

# Addition of numbers
add = a + b

# Subtraction of numbers
sub = a - b

# Multiplication of number
mul = a * b

# Division(float) of number
# Division(int) of number
# Modulus of number
if(b==0):
    print("Division not possible")
else:
    div1 = a / b
    div2 = a // b
    mod = a % b

# Power
p = a ** b

print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)
print(p)

print("\t")


# Examples of Relational Operators
a = 13
b = 33

# a > b is False
print(a > b)
# a < b is True
print(a < b)
# a == b is False
print(a == b)
# a != b is True
print(a != b)
# a >= b is False
print(a >= b)
# a <= b is True
print(a <= b)
