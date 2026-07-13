import hashlib
import json


class Authentication:
    def __init__(self):
        self.__masterHash = self.loadMasterHash()
        self.__unlocked = False

    def isUnlocked(self):
        return self.__unlocked

    def createMasterPassword(self):
        while True:
            if self.__masterHash is None:
                masterPassword = input("Enter New Master Password: ")
                confirm = input("Confirm New Master Password: ")

                if (masterPassword == confirm):
                    hashed = self.hashPassword(masterPassword)

                    self.saveMasterHash(hashed)
                    self.__masterHash = hashed
                    break
                
                else:
                    print("Passwords do not match")

    def verifyPassword(self):
        masterPassword = input("Enter Master Password: ")
        if self.__masterHash == self.hashPassword(masterPassword):
            self.__unlocked = True
            return True
        return False

    def hasMasterPassword(self):
        return self.__masterHash is not None

    @staticmethod # function does not need to access the self object 
    def hashPassword(masterPassword):
        return hashlib.sha256(masterPassword.encode()).hexdigest()

    def saveMasterHash(self, masterHash):
        data = {
            "masterHash" : masterHash
        }

        with open("master.json", "w") as file:
            json.dump(data, file, indent=4)

    def loadMasterHash(self):
        try:
            with open("master.json", "r") as file: 
                data = json.load(file)
                return data["masterHash"]
                    
        except FileNotFoundError:
            return None
