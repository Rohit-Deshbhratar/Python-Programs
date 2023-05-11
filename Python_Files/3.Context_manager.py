# Context managers
# A context manager is designed to reserve and release resources precisely as per the design. 
# When a context manager is used with the "with" keyword, a statement after the with keyword is 
# expected to return an object that must implement the context management protocol. 
# This protocol requires two special methods to be implemented by the returned object. 
# These special methods are as follows: 
# .__enter__(): This method is called with the with keyword and is used to 
# reserve the resources required as per the statement after the with keyword.
# .__exit__(): This method is called after the execution of the with block and 
# is used to release the resources that are reserved in the .__enter__() method.

# Opening a file using WITH statement

filePath = r"C:\Users\rohit\OneDrive\Documents\poems.txt"
with open(filePath,'r') as file:
    fileContent = file.read()
    print(f"\nContents of a file:\n{fileContent}")
