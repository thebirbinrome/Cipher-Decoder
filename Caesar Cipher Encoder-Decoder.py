text = ''    # Enter initial text
shift = 0   # Enter shift of cipher (<0 for shift to the left, >0 for shift to the right(typically, to decode use negative numbers))
def caesar(message, offset):   # Define a custom function, indent all following blocks. Use paramters message and offset for reusability
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # Alphabet for cipher
    encrypted_text=''   # String to store the encrypted text
    for char in message.lower():  # Loop to go through every letter sequentially. requires indented block. P.S. Specified to go for lowercase ver
        if char == ' ':  # Check if the character is equal to a space using the == boolean operator
            encrypted_text += char  # Add the afforementioned space to our encrypted text, if `char` is a space
        else:   # If `char` is not a space
            index = alphabet.find(char) # Find the index of `char` in the alphabet and assign to variable
            new_index = (index + offset) % len(alphabet)   # Assign to variable `new_index` the shifted version of `index`, then retrieve remainder of division by the length of `alphabet` in case of exceeding 26
            encrypted_text = encrypted_text + alphabet[new_index]  # Assign to variable `encrypted_text` its current value plus the value at `new_index` in `alphabet`
    print('plain text:', message)  # Print the inital `text`
    print('encrypted text:', encrypted_text)    # Print the final encrypted text once
caesar(text, shift)    # Call on our function using paramters `text` for message and `shift` for offset