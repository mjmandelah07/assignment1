#  Given a dictionary get all values from the dictionary and add them to a list but don’t add duplicates
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

dictionary = speed.values()
print("Speed values are:", dictionary)

value_list = []
for i in dictionary:
    if i not in value_list:
        value_list.append(i)

print("Values of speed with no duplicates:", value_list)