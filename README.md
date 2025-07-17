# Cipher Decoder

**Cipher Decoder** is a lightweight Python tool for decoding encrypted messages using two classic ciphers: **Caesar** and **Vigenère**. It supports both encoding and decoding when the correct key is provided.

## ✨ Features

- 🔓 Caesar Cipher — encrypt or decrypt using a numeric shift key
- 🔐 Vigenère Cipher — encrypt or decrypt using an alphabetic keyword
- ✅ Simple command-line interface
- 🧠 Supports both uppercase and lowercase letters, ignores non-alphabetic characters

---

## 🔧 How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cipher-decoder.git
cd cipher-decoder
```

### 2. Run the Python Script

```bash
python main.py
```

You'll be prompted to:

- Choose the cipher type (Caesar or Vigenère)
- Choose to encode or decode
- Enter the message
- Enter the key

---

## 🧪 Example

### Caesar Cipher (Decode)

- **Message**: `Khoor Zruog!`
- **Key**: `3`
- **Output**: `Hello World!`

### Vigenère Cipher (Decode)

- **Message**: `Lxfopv Ef rnhr`
- **Key**: `LEMON`
- **Output**: `Attack At Dawn`

---

## 📁 File Structure

```
cipher-decoder/
├── main.py          # Main Python script
├── README.md        # This file
├── LICENSE          # MIT License
└── .gitignore       # Ignores Python-related cache files
```

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 📬 Contributions

Pull requests are welcome! If you'd like to suggest improvements or additional ciphers (e.g., Atbash, Playfair, etc.), feel free to fork the repo and submit a PR.

```

---

Once you add more ciphers or a GUI later, we’ll upgrade this. Let me know when it’s uploaded — we’ll make sure your `main.py` is structured properly for real-world readability and reuse.
