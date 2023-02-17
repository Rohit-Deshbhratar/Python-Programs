# Tuple basics

empty_tuple = ()

print(f"Empty tuple: {empty_tuple}")
print(f"Type of tuple: {type(empty_tuple)}")

tupleWithOneEle1 = (1,)
tupleWithOneEle2 = (1)
print(f"Only one element in tuple with comma: {tupleWithOneEle1}")
print(f"Only one element in tuple without comma: {tupleWithOneEle2}")

myTuple = (1, 15, 62, 1, 81, 79, 1)
print(f"Count element '1' in tuple: {myTuple.count(1)}")