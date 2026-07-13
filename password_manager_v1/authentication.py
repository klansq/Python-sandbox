import hashlib
import json


class Authentication:
    def __init__(self):
        self.__masterHash = self.loadMasterHash()

    def createMasterPassword(self):
        if self.__masterHash is None:
            masterPassword = input("Enter New Master Password: ")
            confirm = input("Confirm New Master Password: ")

            if (masterPassword == confirm):
                hashed = self.hashPassword(masterPassword)

                self.saveMasterHash(hashed)
                self.__masterHash = hashed
            else:
                print("Passwords do not match")
        return

    def verifyPassword(self):
        masterPassword = input("Enter Master Password: ")
        hashed = self.hashPassword(masterPassword)
        
        return hashed == self.__masterHash

    def hasMasterPassword(self):
        return self.__masterHash is not None

    @staticmethod # means function does not need to access the self object 
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
