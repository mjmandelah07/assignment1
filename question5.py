# Given a list of numbers, return True if first and last number of a list is same
list1 = [10, 20, 30, 40, 10]

print("Given list is ", list1)
first_num = list1[0]
last_num = list1[-1]
if first_num == last_num:
    print(True)
else:
    print(False)

# printing a False output
list2 = [10, 20, 30, 40, 50]

print("Given list is ", list2)
first_num = list2[0]
last_num = list2[-1]
if first_num == last_num:
    print(True)
else:
    print(False)
