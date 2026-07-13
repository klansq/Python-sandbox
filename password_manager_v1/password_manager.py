from password import Password
from storage import savePasswords, loadPasswords

class PasswordManager:
    def __init__(self):
        self.__passwords = loadPasswords()
        self.__masterPassword = None

    def __str__(self):
        return f"The password manager holds {len(self.__passwords)} passwords"

    def getPasswords(self):
        return self.__passwords.copy() # a copy
    
    def save(self):
        savePasswords(self.__passwords)

    # 1
    def addPassword(self):
        website = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")

        temp = Password(website, username, password)

        self.__passwords.append(temp)
        self.save()

    # 2
    def viewPasswords(self):
        print("Passwords: ")
        if len(self.__passwords) == 0: # if no entries in passwords list
            print("No passwords saved. \n")
            return
        
        for password in self.__passwords:
            print(password)
        return 
    
    # 3
    def searchPasswords(self):
        if len(self.__passwords) == 0:
            print("No passwords saved \n")
            return
        
        searching = input("Searching for (website): ")

        for password in self.__passwords:
            if password.website ==  searching:
                print(password)
                return
            
        print("No password found")
        return
    
    # 4
    def updatePassword(self):     
        website = input("Website: ")

        for password in self.__passwords:
            if password.website == website:
                newUsername = input("Username: ")
                newPassword = input("Password: ")
                password.setUsername(newUsername)
                password.setPassword(newPassword)

                self.save()
                return
        print("Website not found")

    # 5
    def deletePassword(self):
        website = input("Website: ")

        for password in self.__passwords:
            if password.website == website:
                self.__passwords.remove(password)
                self.save()

                print("Password deleted")
                return

        print("Website not found")