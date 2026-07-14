#imports
from password_manager import *
from storage import loadPasswords
from authentication import Authentication

def startMenu(manager):
    while True:
        print(" ==== Password Manager ==== ")
        print("1. Add Password \n2. View Password \n3. Search \n4. Update Password \n5. Remove Password\n6. Reveal Passwords\n7. Quit \n ")

        selection = input("Select a number: ")

        match selection:
            case "1":
                manager.addPassword()
            case "2":
                manager.viewPasswords()
            case "3":
                manager.searchPasswords()
            case "4":
                manager.updatePassword()
            case "5":
                manager.deletePassword()
            case "6":
                manager.revealPassword()
            case "7":
                return
            case _:
                print("Invalid Choice")

# main function
def main():
    auth = Authentication()

    while True:
        if not auth.hasMasterPassword():
            auth.createMasterPassword()

        while not auth.verifyPassword():
            print("Incorrect password")

        manager = PasswordManager()
        startMenu(manager)

main()
