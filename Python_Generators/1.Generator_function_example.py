# Generator function example

def generator_function():
    yield 'A'
    yield 'B'
    yield 'C'

# Returning iterator instance
iter1 = generator_function()
# When line 11 called, starts executing "generator_function()" and pause after first "yield" statement "yield "A""
print(iter1.__next__())
# When line 13 executed result is same as above, but this time execution begins from "yield "B""
print(next(iter1))
# When line 15 executed result is same as above, and executes "yield "C""
print(iter1.__next__())