# Passing dictionary to function as an argument

bookAuthors = {"1984" : "George Orwell", "Wings of fire" : "APJ Abdul Kalam", "Indira Gandhi" : "Pupul Jaikar"}

def passDict(bookAuthors):
    for key in bookAuthors:
        print(f"Book name: {key}, Author: {bookAuthors[key]}")

passDict(bookAuthors)

# Passing DICTIONARY as **kwargs
def book(**bookAuthors):
    print(bookAuthors["book_name"]+", "+bookAuthors["author"])
    #pass

book(book_name = "1984", author = "George Orwell")
