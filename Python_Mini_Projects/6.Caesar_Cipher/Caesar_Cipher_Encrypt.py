# The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. 
# It encrypts letters by shifting them over by a certain number of places in the alphabet. 
# We call the length of shift the key. For example, if the key is 3, then A becomes D, 
# B becomes E, C becomes F, and so on. To decrypt the message, you must shift 
# the encrypted letters in the opposite direction. This program lets the user encrypt
# and decrypt messages according to this algorithm.

print("Please enter text to encrypt: ")
plaintext = str(input())
print("Please enter key to encrypt text: ")
key = int(input())

def encrypt(plaintext, key):
    encrypted_text = ""

    for i in range(len(plaintext)):
        ch = plaintext[i]
        # Check if there is a space in plaintext, if it is then simply add space
        if  ch == " ":
            encrypted_text += " "
        # Check if character is upper case
        elif(ch.isupper()):
            encrypted_text += chr((ord(ch) + key - 65) % 26 + 65)          
        # Check if character is lower case
        else:
            encrypted_text += chr((ord(ch) + key - 97) % 26 + 97)
        
    return encrypted_text
print(f"Encrypted text is: {encrypt(plaintext, key)}")        
