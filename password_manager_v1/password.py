import random
import string

class Password:
    def __init__(self, website, username, password = None):
        self.website = website
        self.username = username

        if password is None:
            self.password = self.generatePassword(12)
        else:
            self.password = password

    def toDictionary(self):
        return { 
            "Website" : self.website,
            "Username" : self.username,
            "Password" : self.password
        }
    
    def __str__(self):
        return f"Website: {self.website}\nUsername: {self.username}\nPassword: {self.password}"

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    # password generation
    def generatePassword(self, length = 12):
        characters = string.ascii_letters + string.digits + string.punctuation 
        self.password = ""

        for i in range(length):
            self.password += random.choice(characters)
