# Write a code to extract each digit from an integer, in the reverse order
num1 = 7455
print("Given number", num1)
while num1 > 0:
    digit = num1 % 10

    num1 = num1 // 10
    print(digit, end=" ")

