import json
from password import Password

# save passwords to json file
def savePasswords(passwords):
    data = []

    for password in passwords:
        data.append(password.toDictionary())

    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)


# load saved passwords from json file
def loadPasswords():
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            passwords = []

            for item in data:
                password = Password.fromDictionary(item)
                passwords.append(password)

            return passwords
        
    except FileNotFoundError:
        print("File does not exist")
        return []