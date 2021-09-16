# Exercise 4: Iterate a given list and count the occurrence of each element
# and create a dictionary to show the count of each element.
original_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
my_dict = {}

for a in original_list:
    if a in my_dict:
        my_dict[a] += 1
    else:
        my_dict[a] = 1

print("The count of the list:", my_dict)