# Given a range of first 10 numbers, Iterate from start number to the end number and
# print the sum of the current number and previous number:
# HINT : Python range() function
def number(num):
    previous_num = 0
    for a in range(num):
        sum_num = previous_num + a
        print("Current Number", a, "Previous Number ", previous_num, " Sum: ", sum_num)
        previous_num = a


print("Printing current and previous number sum in a given range(10)")
number(10)
