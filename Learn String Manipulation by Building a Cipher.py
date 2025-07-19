text = 'mrttaqrhknsw ih puggrur'    # Enter text
custom_key = 'happycoding' # Enter custom key for decryption

def vigenere(message, key, direction=1):   # Define a custom function, indent all following blocks. Use parameters message and key and direction for reusability. By default, direction has a value of 1 (encrypt), meaning that we don't always need to enter it.
    key_index = 0   # Since the key is shorter than the text, we need this index to repeat the key to generate the whole encrypted text
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # Alphabet for cipher
    final_message = ''   # String to store the encrypted/decrypted text
    for char in message.lower():  # Loop to go through every letter sequentially. requires indented block. P.S. Specified to go for lowercase ver
        # Append any non-letter character to the message
        if not char.isalpha():  # Check if all character in `char` are not letters
            final_message += char  # Add the afforementioned space to our encrypted/decrypted text, if `char` is a space
        else:   # If `char` is not a space
            # Find the right key character to use to encode/decode, starting from index 0 to 11, and then going back to the first character
            key_char = key[key_index % len(key)]    
            key_index += 1
            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)   # Find where in `alphabet` `key_char` is and assign it to our offset
            index = alphabet.find(char) # Find the index of `char` in the alphabet and assign to variable
            new_index = (index + offset * direction) % len(alphabet)   # Assign to variable `new_index` the shifted version of `index` along with what direction it was shifted in, then retrieve remainder of division by the length of `alphabet` in case of exceeding 26
            final_message += alphabet[new_index]  # Assign to variable `final_message` its current value plus the value at `new_index` in `alphabet`
    return final_message   # Return value to be used in other parts of code
def encrypt(message, key):  # Defining encryption function
    return vigenere(message, key)  # Make the result of the function `encrypt` the result of vigenere with direction = 1 
def decrypt(message, key):
    return vigenere(message, key, -1)   # Same, opposite direction

print(f'Encrypted text: {text}')    # Print out our original encrypted text, using an f-string
print(f'Key: {custom_key}') # Print out our key
decryption = decrypt(text, custom_key)  # Decrypt a text by using the vigenere function with parameters message = text, key = custom_key)
print(f'\nDecrypted text: {decryption}\n')







# Strings are immutable - they cannot be changed once created, however they can be reassigned (will use later). Thus, we cannot simply alter the 'H' in text to a new value.