from cryptography.fernet import Fernet
import os

def generateKey():
    key = Fernet.generate_key()

    with open("secret.key", "wb") as file: # write binary
        file.write(key)

def loadKey():
    with open("secret.key", "rb") as file: # read binary
        return file.read() 
    
def getKey():
    if not os.path.exists("secret.key"):
        generateKey()
    return loadKey()
    
def encryptData(message):
    key = loadKey()
    cipher = Fernet(key)

    return cipher.encrypt(message.encode())

def decryptData(encrypted):
    key = loadKey()
    cipher = Fernet(key)

    return cipher.decrypt(encrypted)