# Given a string and an integer number n, remove characters from a string starting from zero up to n
# and return a new string

# Firstly
name = "Hello World"
nth = 4
print("Removing nth number of characters from the string")
print(name[nth:])

# or
name = input("Enter a name")
n = int(input("Input a number less than 3"))
print("Removing nth number of characters from the string")
print(name[n:])

