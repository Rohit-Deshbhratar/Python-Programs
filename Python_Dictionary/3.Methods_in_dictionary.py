# Applying methods of dictionary from python

books = {'name' : 1984,
         'author' : 'George Orwell',
         'publisher' : 'aarushi book enterprises',
         'ISBN' : '978-81-94215-81-3'}

print(f"Actual dictionary: {books}")

# copy()
print(f"copy(): {books.copy()}")

# fromkeys()
print(f"fromkeys(): {books.fromkeys('publish_year', 2020)}")

# get() returns value of specified key
print(f"get(): {books.get('name')}")

# items()
print(f"items(): {books.items()}")

# keys()
print(f"keys(): {books.keys()}")

# pop()
print(f"pop(): {books.pop('ISBN')}")
print(f"Dictionary after item popped: {books}")

# popitem()
print(f"popitem(): {books.popitem()}")
print(f"Dictionary after item popped: {books}")

# setdefault()
print(f"setdefault(): {books.setdefault('author')}")

# update()
print(f"update(): {books.update(books)}")
print(books)

# values()
print(f"values(): {books.values()}")

# clear()
print(f"clear(): {books.clear()}")
print(books)