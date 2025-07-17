text = 'Hello World'    # Initial text
shift = 3   # Shift of cipher
alphabet = 'abcdefghijklmnopqrstuvwxyz' # Alphabet for cipher
index = alphabet.find(text[0])  # Find the index of the first occurence of the character under index 0 in text in alphabet and assign it to variable index (will NOT work for uppercase letters)
index = alphabet.find(text[0].lower())  # Fix line above
shifted = alphabet[index]   # Acess value of alphabet at the index of 'index'
print(shifted)  # Print variable shifted
print(index)    # Print variable index