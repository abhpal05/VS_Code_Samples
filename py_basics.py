#Variable Declaration

myNumber = 3
print(myNumber)
myNumber = 4.5
print(myNumber)
myNumber = "Hello World"
print(myNumber)

print("\t")

#python program to illustrate a list

nums = []
nums.append(21)
nums.append(40.5)
nums.append("String")

print("\t")

# Python program to illustrate getting input from user
name = input("Enter your name: ") 
# user entered the name 'harssh'
print("hello", name)

print("\t")

# Python3 program to get input from user
  
# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
  
num3 = num1 * num2
print("Product is: ", num3)

print("\t");

# Python program to illustrate
# selection statement
  
num1 = 34
if(num1>12):
    print("Num1 is good")
elif(num1>35):
    print("Num2 is not gooooo....")
else:
    print("Num2 is great")

print("\t")

# Python program to illustrate
# functions
def hello():
    print("hello")
    print("hello again")
hello()
  
# calling function
hello()   

print("\t")


# Python program to illustrate 
# function with main
def getInteger():
    result = int(input("Enter integer: "))
    return result
  
def Main():
    print("Started")
  
    # calling the getInteger function and 
    # storing its returned value in the output variable
    output = getInteger()     
    print(output)
  
# now we are required to tell Python 
# for 'Main' function existence
if __name__=="__main__":
    Main()

print("\t")

# Python program to illustrate
# a simple for loop

loop = int(input("Enter integer for loop: "))  
for step in range(loop):    
    print(step)

print("\t")