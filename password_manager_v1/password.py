from encryption import encryptData, decryptData
import random
import string

class Password:
    def __init__(self, website, username, password = None):
        self.website = website
        self.username = username

        if password is None:
            self.password = encryptData(self.generatePassword(12))
        else:
            self.password = encryptData(password)

    def toDictionary(self):
        return { 
            "Website" : self.website,
            "Username" : self.username,
            "Password" : self.password.decode()
        }
    
    def __str__(self):
        return f"Website: {self.website}\nUsername: {self.username}\nPassword: {self.getPassword()}"

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = encryptData(password)

    def getPassword(self):
        return decryptData(self.password)

    # password generation
    def generatePassword(self, length = 12):
        characters = string.ascii_letters + string.digits + string.punctuation 
        password = ""

        for i in range(length):
            password += random.choice(characters)

        return password
    
    def display(self):
        print(f"Website: {self.website}\nUsername: {self.username}\nPassword: {self.getPassword()}\n----------------")
    
    @classmethod # class itself, not exist obj
    def fromDictionary(cls, data):
        password = cls.__new__(cls) 

        password.website = data["Website"]
        password.username = data["Username"]
        password.password = data["Password"].encode()

        return password
