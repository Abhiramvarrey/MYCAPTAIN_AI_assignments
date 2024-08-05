# Define two sets as lists
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of set1 and set2
union_set = set1.copy()
for elem in set2:
    if elem not in union_set:
        union_set.add(elem)


# Intersection of set1 and set2
intersection_set = []
for elem in set1:
    if elem in set2:
        intersection_set.append(elem)


# Difference of set1 and set2 (elements in set1 but not in set2)
difference_set = []
for elem in set1:
    if elem not in set2:
        difference_set.append(elem)


# Symmetric difference of set1 and set2 (elements in either set1 or set2 but not in both)
symmetric_difference_set = []
for elem in set1:
    if elem not in set2:
        symmetric_difference_set.append(elem)
for elem in set2:
    if elem not in set1:
        symmetric_difference_set.append(elem)

print(f"Union of E and N is {union_set} Intersection of E and N is {set(intersection_set)} Difference of E and N is {set(intersection_set)} Symmetric difference of E and N is {set(symmetric_difference_set)}")
'''
#ALTERNATIVE WAY 
# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of set1 and set2
union_set = set1.union(set2)

# Intersection of set1 and set2
intersection_set = set1.intersection(set2)

# Difference of set1 and set2 (elements in set1 but not in set2)
difference_set = set1.difference(set2)

# Symmetric difference of set1 and set2 (elements in either set1 or set2 but not in both)
symmetric_difference_set = set1.symmetric_difference(set2)

print(f"Union of E and N is {union_set} Intersection of E and N is {intersection_set} Difference of E and N is {intersection_set} Symmetric difference of E and N is {symmetric_difference_set}")
'''
