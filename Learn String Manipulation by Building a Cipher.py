text = 'Hello Zaira'    # Enter text
custom_key = 'python' # Enter custom key for decryption
def vigenere(message, key, direction):   # Define a custom function, indent all following blocks. Use parameters message and key and direction for reusability
    key_index = 0   # Since the key is shorter than the text, we need this index to repeat the key to generate the whole encrypted text
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # Alphabet for cipher
    encrypted_text=''   # String to store the encrypted text
    for char in message.lower():  # Loop to go through every letter sequentially. requires indented block. P.S. Specified to go for lowercase ver
        if char == ' ':  # Check if the character is equal to a space using the == boolean operator
            encrypted_text += char  # Add the afforementioned space to our encrypted text, if `char` is a space
        else:   # If `char` is not a space
            # Find the right key character to use to encode, starting from index 0 to 11, and then going back to the first character
            key_char = key[key_index % len(key)]    
            key_index += 1
            # Define the offset and the encrypted letter
            offset = alphabet.index(key_char)   # Find where in `alphabet` `key_char` is and assign it to our offset
            index = alphabet.find(char) # Find the index of `char` in the alphabet and assign to variable
            new_index = (index + offset) % len(alphabet)   # Assign to variable `new_index` the shifted version of `index`, then retrieve remainder of division by the length of `alphabet` in case of exceeding 26
            encrypted_text = encrypted_text + alphabet[new_index]  # Assign to variable `encrypted_text` its current value plus the value at `new_index` in `alphabet`
    return encrypted_text   # Return value to be used in other parts of code


# encryption = vigenere(text, custom_key) # Call our function with parameters `text` and `custom_key`, and assign our returned value to `encryption`
# print(encryption)







# Strings are immutable - they cannot be changed once created, however they can be reassigned (will use later). Thus, we cannot simply alter the 'H' in text to a new value.