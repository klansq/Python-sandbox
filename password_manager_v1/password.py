from encryption import encryptData, decryptData
import random
import string

class Password:
    def __init__(self, website, username, password = None):
        self.__website = website
        self.__username = username

        if password is None:
            self.__password = encryptData(self.generatePassword(12))
        else:
            self.__password = encryptData(password)

    def toDictionary(self):
        return { 
            "Website" : self.__website,
            "Username" : self.__username,
            "Password" : self.__password.decode()
        }
    
    # getters
    def getWebsite(self): 
        return self.__website
    
    def getUsername(self):
        return self.__username
    
    def getPassword(self):
        return self.__password
    
    # setters
    def setWebsite(self, website):
        self.__website = website

    def setUsername(self, username):
        self.__username = username
    
    def __str__(self):
        return f"Website: {self.__website}\nUsername: {self.__username}\nPassword: {'*' * 12}"

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = encryptData(password)

    def getPassword(self):
        return decryptData(self.__password)

    # password generation
    def generatePassword(self, length = 12):
        characters = string.ascii_letters + string.digits + string.punctuation 
        password = ""

        for i in range(length):
            password += random.choice(characters)

        return password
    
    def display(self):
        print(f"Website: {self.__website}\nUsername: {self.__username}\nPassword: {self.getPassword()}\n----------------")
    
    @classmethod # class itself, not exist obj
    def fromDictionary(cls, data):
        password = cls.__new__(cls) 

        password.website = data["Website"]
        password.username = data["Username"]
        password.password = data["Password"].encode()

        return password
