text = 'Pdnh vxuh wr fkhfn rxw pb rwkhu surmhfwv'   # Enter your text
shift = -3   # Enter your shift. Positive if you wish to encode, negative if you wish to decode.
def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text=''
    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted/decrypted text:', encrypted_text)
caesar(text, shift)