def reverse_each_word(input_string):
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    reversed_string = ' '.join(reversed_words)
    return reversed_string

# Example string
text = "Hello world, how are you?"

reversed_text = reverse_each_word(text)
print("String with reversed words:", reversed_text)
