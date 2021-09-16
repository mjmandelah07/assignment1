# Exercise 5: Given a two list of equal size create a Python set such that it shows the element
# from both lists in the pair
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = zip(first_list, second_list)

print("This is the First list", first_list)
print("This is the Second list", second_list)

print(set(result))
