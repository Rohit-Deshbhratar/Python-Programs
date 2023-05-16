# The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. 
# It encrypts letters by shifting them over by a certain number of places in the alphabet. 
# We call the length of shift the key. For example, if the key is 3, then A becomes D, 
# B becomes E, C becomes F, and so on. To decrypt the message, you must shift 
# the encrypted letters in the opposite direction. This program lets the user encrypt
# and decrypt messages according to this algorithm.

print("Please enter decrypted message: ")
encrypted_message = input()
print("Please enter key to encrypt text: ")
key = int(input())

def decrypt(encrypted_message, key):
    decrypted_text =""

    for i in range(len(encrypted_message)):
        ch = encrypted_message[i]

        # Check if there is a space in encrypted_message, if it is then simply add space
        if ch == " ":
            decrypted_text += " "
        # Check if character is upper case
        elif(ch.isupper()):
            decrypted_text += chr((ord(ch) - key - 65) % 26 + 65)
        # Check if character is lower case
        else:
            decrypted_text += chr((ord(ch) - key - 97) % 26 + 97)
    
    return decrypted_text

print(f"Decrypted text: {decrypt(encrypted_message, key)}")
    