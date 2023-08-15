def reverse_words(input_string):
    words = input_string.split()
    reversed_words = words[::-1]  # Reverse the list of words
    reversed_string = ' '.join(reversed_words)
    return reversed_string

# Example string
text = "This is an example sentence."

reversed_text = reverse_words(text)
print("Reversed string:", reversed_text)
