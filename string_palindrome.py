# String Palindrome
input_string = input("Enter your string: ")
if(input_string == input_string[::-1]):
    print("The string is palindrome")
else:
    print("The string is not palindrome")



# List (Create a list with even numbers of given list)
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [number for number in a if number%2==0 ]
print(b)

