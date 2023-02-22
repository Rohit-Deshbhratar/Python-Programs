# Can you change the values inside a list which is contained in set S = {8, 7, 12, “Harry”, [1, 2]}

# Reason ==>

# LIST => Lists are mutable and hence "UNHASHABLE" objects 
# SET => Sets are unordered and "DISTINCT HASHABLE" objects.
#
# SOLUTION => No, Python does not allow to store LIST inside SET.
#             But you can add TUPLE to a SET using "update()" method.