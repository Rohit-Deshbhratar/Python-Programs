# Set Methods
# Original set declared for this program
mySet = {12, 56, 47, 97, 61}
print(f"type: {type(mySet)}, Values: {mySet}")

# add()
mySet.add(79)
print(f"New value added is: {mySet}")

# copy()
print(f"Copied set: {mySet.copy()}")

# difference() => Returns only those number that exist only in first set
diff_1 = {1, 2, 3, 8, 7, 5, 9, 17}
diff_2 = {8, 7, 5, 11, 13, 15, 17, 3}

print(f"First set: {diff_1}, Second set: {diff_2}")
print(f"Difference between above two sets: {diff_1.difference(diff_2)}")

# difference_update() => Removes the item that exist in both sets.
print(f"First set: {diff_1}, Second set: {diff_2}")
diff_1.difference_update(diff_2)
print(f"Difference update: {diff_1}")

# discard()
mySet.discard(47)
print(f"Set after discarding: {mySet}")

# intersection()
int_1 = {1, 4, 9}
int_2 = {0, 9, 4}
intersect = int_1.intersection(int_2)
print(f"Intersection of two sets: {intersect}")

# isdisjoint()
print(f"No similar items are present in both sets?: {int_1.isdisjoint(int_2)}")

# issubset()
print(f"All items of first set are present in second set?: {int_1.issubset(int_2)}")

# issuperset()
print(f"All items of first set are present in second set?: {int_2.issuperset(int_1)}")

# pop()
print(f"Before popping an element: {mySet}")
print(f"After popping an element: {mySet.pop(), mySet}")

# remove()
print(f"Before removing an item: {mySet}")
mySet.remove(12)
print(f"After removing an item: {mySet}")

# symmetric_difference()
symmetric = diff_1.symmetric_difference(diff_2)
print(f"Symmetric difference: {symmetric}")

# symmetric_difference_update()
diff_1.symmetric_difference_update(diff_2)
print(f"Updated set: {diff_1}")

# union()
union = int_1.union(int_2)
print(f"union(): {union}")

# update()
int_1.update(int_2)
print(f"update(): {int_1}")