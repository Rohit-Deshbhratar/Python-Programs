import string
from sys import stdin


def countWords(str):
    final_count = str.split()
    return len(final_count)

#main
string = stdin.readline().strip();
count = countWords(string)
print(count)
