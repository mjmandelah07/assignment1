# Given two integer numbers print their product and  if the product is greater than 1000, then return their sum
print("Given two integer numbers print their product and  if the product is greater than 1000, then return their sum")


num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

product = num1 * num2


if product > 1000:
    print("Sum is:", num1 + num2)
else:
    print("Product is:", product)
