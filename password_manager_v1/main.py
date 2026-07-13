#imports
from password_manager import *
from storage import loadPasswords

def startMenu(manager):
    while True:
        print(" ==== Password Manager ==== ")
        print("1. Add Password \n2. View Password \n3. Search \n4. Update Password \n5. Remove Password\n6. Quit \n ")

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
                return
            case _:
                print("Invalid Choice")

# main function
def main():
    manager = PasswordManager()
    startMenu(manager);

main()
