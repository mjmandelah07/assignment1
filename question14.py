# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return base * exponent(base, exp - 1)


base = int(input("Enter base: "))
exp = int(input("Enter exponential value: "))
result = exponent(base, exp)
print("Result:", exponent(base, exp))
