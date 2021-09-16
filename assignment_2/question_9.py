# Iterate a given list and Check if a given element already exists in a dictionary as
# a key’s value if not delete it from the list
roll_Number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_Dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print("Roll_number elements are:", roll_Number)


roll_Number = [a for a in roll_Number if a in sample_Dict.values()]
print("Values after removing unwanted elements:", roll_Number)
