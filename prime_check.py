# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.).
#  You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.

def check_prime(n):
    for x in range(2, ((n//2)+1)):
        if(n%x == 0):
            print("The number is not prime")
            return
    print("The number is prime")

input_number = int(input("Enter number:"))
print(input_number)
check_prime(input_number)