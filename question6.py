# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

my_list = [10, 20, 33, 46, 55]
print("Given list is ", my_list)
print("Divisible of 5 in a list")
for a in my_list:
    if a % 5 == 0:
        print(a)
