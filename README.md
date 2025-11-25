# Password Manager in Python

A simple local password manager written in pure Python.  
It stores passwords in encrypted form and lets you add and view entries through a console interface.

> This project is intended for learning and experimentation.  
> Do not use it to store real sensitive passwords in production.

---

## Features

* Store account passwords in an encrypted text file
* Use a single master key to encrypt and decrypt all saved passwords
* Add new credentials from the terminal
* View previously stored credentials in decrypted form
* Minimal dependencies and small codebase that is easy to read and extend

---

## How it works

The password manager uses symmetric encryption to protect your data.

* A secret key is generated once and stored locally in a file named `key.key`
* Password entries are stored in `passwords.txt` in encrypted form
* When you run the program it
  * loads the encryption key from `key.key`
  * decrypts existing entries from `passwords.txt` when you choose to view them
  * encrypts new passwords before appending them to `passwords.txt`

Everything is stored locally on your machine.  
There is no network communication or remote storage.

---

## Requirements

* Python 3.8 or later
* The `cryptography` library

Install the dependency with:

```bash
pip install cryptography
