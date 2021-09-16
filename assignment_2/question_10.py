#  Remove duplicate from a list and create a tuple and find the minimum and maximum number.
sample_List = [87, 45, 41, 65, 94, 41, 99, 94]

print("Original list", sample_List)
sample_List = set(sample_List)

sample = list(sample_List)
print("List of elements:", sample)

tupl_e = tuple(sample)
print("This is tuple:", tupl_e)

mini_mum = min(tupl_e)
maxi_mum = max(tupl_e)

print("The minimum of the tuple are:", mini_mum)
print("The maximum of the tuple are:", maxi_mum)
