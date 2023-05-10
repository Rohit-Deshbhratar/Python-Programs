# Destructors are the opposite of constructors—they are executed when an instance is 
# deleted or destroyed. In Python, destructors are hardly used because Python has a garbage 
# collector that handles the deletion of the instances that are no longer referenced by any 
# other instance or program. 

class DestructorExample:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

    def __del__(self):
        print("Object is deleted.")

dest = DestructorExample("Rohit", "Deshbhratar")
print(f"{dest.first} {dest.last}")