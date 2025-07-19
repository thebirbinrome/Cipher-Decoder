text = 'uprola wps kyfdszoh wlu ng gsprvdu!'    # Enter your encrypted text
custom_key = 'birb' # *Enter your key for decryption*
setting = 'decrypt'   # Set to 'encrypt' or 'decrypt'


def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]    
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
def decrypt(message, key):
    return vigenere(message, key, -1)
print(f'Entered text: {text}')
print(f'Key: {custom_key}')

if setting == 'decrypt':
    decryption = decrypt(text, custom_key)
    print(f'\nDecrypted text: {decryption}\n')
if setting == 'encrypt':
    encryption = encrypt(text, custom_key)
    print(f'\nEncrypted text: {encryption}\n')

# Make sure to save changes before running file! Also, if it doesn't work, try running it in its own dedicated terminal