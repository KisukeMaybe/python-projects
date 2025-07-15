# 🔐 Simple Password Manager

A basic command-line password manager written in Python using `cryptography.fernet` for encryption.

This tool allows you to securely store and view passwords for different accounts using a master password.

## 🚀 Getting Started

### 1. Install Dependencies

You'll need the `cryptography` library:

```bash
pip install cryptography
```

### 2. Generate an Encryption Key

Uncomment and run the `write_key()` function in the script once to generate your encryption key:

```python
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
```

This will create a file called `key.key` which stores the encryption key.

## 🔧 How It Works

- On launch, you’ll be prompted for your master password.
- The master password is combined with the key in `key.key` to derive the encryption key.
- Passwords are encrypted and stored in `passwords.txt`.
- You can add or view stored passwords through the menu.

## ✨ Features

- Encrypts passwords using `cryptography.fernet`
- Master password-based encryption key
- Stores credentials in a local `passwords.txt` file
- Add new credentials via command line
- View decrypted passwords via command line
- Input validation for options
- Saves encrypted passwords per account

## ⚠️ Warning

- This script is for educational purposes only.
- It stores data locally and lacks advanced security features such as:
  - Password hashing
  - Salting
  - File encryption
  - User authentication
- Use at your own risk.

## 📄 Files Used

- `passwords.txt`: Stores encrypted credentials
- `key.key`: Stores the encryption key (must be kept safe!)
