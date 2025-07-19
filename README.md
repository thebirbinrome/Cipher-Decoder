```markdown
# 🔐 Cipher Decoder

A beginner-friendly Python tool for encrypting and decrypting messages using **Caesar** and **Vigenère** ciphers.

This repo contains two separate scripts:
- `Vigenere Cipher Encoder-Decoder.py` – encrypts/decrypts text with a custom key, harder to crack!
- `Caesar Cipher Encoder-Decoder.py` – uses a basic shift cipher with user-defined offset

---

## 📂 Files Included

### `Vigenere Cipher Encoder-Decoder.py`

Encrypts or decrypts messages using the **Vigenère cipher**, which relies on a key to shift letters by varying amounts.

**How to use:**

Edit the following variables at the top of the file:

```python
text = 'uprola wps kyfdszoh wlu ng gsprvdu!'  # Your encrypted/decrypted message
custom_key = 'birb'                           # Your decryption/encryption key
setting = 'decrypt'                           # Set to 'encrypt' or 'decrypt'
```

Then run the script:

```bash
python vigenere.py
```

### `Caesar Cipher Encoder-Decoder.py`

A simple Caesar cipher decoder/encoder that shifts each letter by a fixed number of positions in the alphabet.

**How to use:**

Edit the following at the top of the file:

```python
text = 'Pdnh vxuh wr fkhfn rxw pb rwkhu surmhfwv'  # Message to encode/decode
shift = -3                                        # Shift value (positive = encode, negative = decode)
```

Then run the script:

```bash
python caesar.py
```

---

## ✅ Features

- Caesar cipher (with customizable shift)
- Vigenère cipher (with custom key, supports encryption/decryption)
- Easy to modify or expand
- No external libraries needed

---

## 📌 To-Do / Planned Features

- Brute-force Caesar attack (try all 26 shifts)
- Auto-detect Caesar key using frequency analysis
- GUI version using Tkinter
