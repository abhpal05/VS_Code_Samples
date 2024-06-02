# Print Name 1000 times without loop

# Input name
input_name = input("Enter your name: ")

str = "X"
str = str.replace("X", "XXXXXXXXXX")
str = str.replace("X", "XXXXXXXXXX")
str = str.replace("X", "XXXXXXXXXX")
str = str.replace("X", input_name + "\n")

print(str)
