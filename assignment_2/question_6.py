# Given the following two sets find the intersection and remove those elements from the first set
x = {65, 42, 78, 83, 23, 57, 29}
y = {67, 73, 43, 48, 83, 57, 29}

print("The first Set are:", x)
print("The second Set are:", y)

intersection = x.intersection(y)
print("Intersection are:", intersection)
for a in intersection:
  x.remove(a)

print("Result after removing the common elements", x)