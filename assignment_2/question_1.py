# Exercise 1: Given two lists create a third list by picking an odd-index element from the first list
# and even index elements from the second.
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

li_1 = listOne[1::2]
li_2 = listTwo[0::2]

listThree = li_1 + li_2

print("Example 1:")
print("Odd index elements for listOne are: ", li_1)
print("Even index elements for listTwo are: ", li_2)
print("This are the combination of listOne elements  and listTwo elements: ", listThree )
print("\n")


# OR
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
list_odd = []
count = 0
for i in listOne:
    if count % 2 == 1:
        list_odd.append(i)
    count += 1

list_even = []
count = 0
for x in listTwo:
    if count % 2 == 0:
        list_even.append(x)
    count += 1

print("Example 2:")
print("Odd index elements for listOne are: ", list_odd)
print("Even index elements for listTwo are: ", list_even)
print("This are the combination of listOne elements  and listTwo elements: ", list_odd + list_even)
