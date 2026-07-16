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