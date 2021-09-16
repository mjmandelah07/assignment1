# Exercise 7: Given two sets, Checks if One Set is a subset or superset of another Set.
# if the subset is found delete all elements from that set.
x = {57, 83, 29}
y = {67, 73, 43, 48, 83, 57, 29}

subset_x = x.issubset(y)
subset_y = y.issubset(x)

superset_x = x.issuperset(y)
superset_y = y.issuperset(x)

print("First set are:", x)
print("Second set are:", y)
print("\n")
print("x is subset of y:", subset_x)
print("y is subset of x:", subset_y)
print("\n")
print("x is superset of y:", superset_x)
print("y is superset of x:", superset_y)

if subset_x is True:
    x.clear()

if subset_y is True:
    y.clear()

print("\n")

print("First set are cleared:", x)
print("Second set are:", y)