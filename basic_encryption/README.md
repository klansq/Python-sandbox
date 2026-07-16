# Caesar Cipher Encryption

A basic Python encryption and decryption program using the **Caesar Cipher** technique.

## What Is a Caesar Cipher?

A Caesar Cipher is a simple substitution cipher where each letter in a message is shifted by a fixed number of positions in the alphabet.

For example, with a key of `3`:

```text
A → D
B → E
C → F
```

Therefore:

```text
Hello → Khoor
```

The key determines how many positions each letter is shifted.

## Features

* Encrypt text using a numerical key
* Decrypt encrypted text using the same key
* Supports uppercase and lowercase letters
* Preserves spaces, punctuation, and numbers
* Wraps around the alphabet using modulo arithmetic
* Includes a basic Tkinter GUI

## Example

### Encryption

```python
message = "Hello World!"
key = 3
```

Output:

```text
Khoor Zruog!
```

### Decryption

```python
encrypted = "Khoor Zruog!"
key = 3
```

Output:

```text
Hello World!
```

## How It Works

The program checks each character individually.

### Lowercase letters

```python
shifted = (ord(character) - ord("a") + key) % 26
```

The character is converted to a numerical position within the alphabet, shifted by the key, and then converted back into a character.

### Uppercase letters

The same process is used, but with `"A"` as the starting point:

```python
shifted = (ord(character) - ord("A") + key) % 26
```

### Non-alphabetic characters

Spaces, punctuation, and numbers are left unchanged:

```text
Hello, World! 123
```

After encryption:

```text
Khoor, Zruog! 123
```

## Encryption Function

```python
def encrypt(message, key):
    encrypted = ""

    for character in message:
        if character.islower():
            shifted = (ord(character) - ord("a") + key) % 26
            encrypted += chr(shifted + ord("a"))

        elif character.isupper():
            shifted = (ord(character) - ord("A") + key) % 26
            encrypted += chr(shifted + ord("A"))

        else:
            encrypted += character

    return encrypted
```

## Decryption Function

Decryption reverses the process by subtracting the key instead of adding it:

```python
def decrypt(encrypted, key):
    decrypted = ""

    for character in encrypted:
        if character.islower():
            shifted = (ord(character) - ord("a") - key) % 26
            decrypted += chr(shifted + ord("a"))

        elif character.isupper():
            shifted = (ord(character) - ord("A") - key) % 26
            decrypted += chr(shifted + ord("A"))

        else:
            decrypted += character

    return decrypted
```

## Project Structure

```text
basic_encryption/
│
├── encryption.py
├── gui.py
├── main.py
└── README.md
```

## Running the Project

Activate the virtual environment:

```powershell
.\.venv\Scripts\activate
```

Then run the program:

```powershell
python main.py
```

## Important Note

The Caesar Cipher is **not secure for real-world encryption**. It is extremely easy to break because there are only 26 possible shifts.

This project is intended for learning and demonstrates the basic concepts behind substitution ciphers and simple encryption algorithms.
