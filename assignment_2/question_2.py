# Exercise 2: Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list
original_list = [34, 54, 67, 89, 11, 43, 94]

print("original list:", original_list)
index_4 = original_list.pop(4)
print("List After removing element at index 4:", original_list)
second_position = original_list.insert(2, index_4)
print("List after Adding element at index 2:", original_list)
last_position = original_list.append(index_4)
print("List after Adding element at last:", original_list)
