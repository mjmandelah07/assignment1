# Given a two list of numbers create a new list such that new list should contain
# only odd numbers from the first list and even numbers from the second list:

list1 = [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]
list3 = []

print("First List ", list1)
print("Second List ", list2)

for x in list1:
    if x % 2 != 0:
        list3.append(x)
for x in list2:
    if x % 2 == 0:
        list3.append(x)
print("result List is", list3)
