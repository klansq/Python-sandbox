"""
Possibly add:
- Clear Passwords
"""

def startMenu(passwords):
    while True:
        print(" ==== Password Manager ==== ")
        print("1. Add Password \n2. View Password \n3. Search \n4.Delete \n5. Quit \n ")

        selection = input("Select a number: ")

        match selection:
            case "1":
                addingInformation(passwords)
            case "2":
                viewPasswords(passwords)
            case "3":
                searchPasswords(passwords)
            case "4":
                print("Choice 4")
                deletePassword(passwords)
            case "5":
                print("Choice 5")
                break
            case _:
                print("Invalid Choice")

# 1
def addingInformation(passwords):
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    print(f"You entered: \nWebsite: {website} \nUsername: {username} \nPassword: {password}")
    storeData(passwords, website, username, password)
    
    return

def storeData(passwords,website, username, password):
    temp = dict({
        "Website" : website,
        "Username" : username,
        "Password" : password
    })
    passwords.append(temp)

    return

# 2
def viewPasswords(passwords):
    print("Passwords: ")
    if len(passwords) == 0: # if no entries in passwords list
        print("No passwords saved. \n")
        return
    
    for password in passwords:
        for key, value in password.items():
            print(f"- {key} : {value} ")
        print("----------------")
        
    return 

# 3
def searchPasswords(passwords):
    if len(passwords) == 0:
        print("No passwords saved \n")
        return
    
    searching = input("Searching for (website): ")
    found = False
    
    for password in passwords:
        if password["Website"] ==  searching:
            print(f"Website : {password['Website']}")
            print(f"Username : {password['Username']}")
            print(f"Password : {password['Password']}")
                  
            found = True

    if not found:
        print("No password found")
    
    return

# 4
def deletePassword(passwords):
    return


# main function
def main():
    passwords = []
    startMenu(passwords);


main()