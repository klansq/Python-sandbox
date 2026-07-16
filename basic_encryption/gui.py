import tkinter as tk
from encryption import encrypt, decrypt

class EncryptionGUI: 
    def __init__(self):
        self.window = tk.Tk()   
        self.window.title("Caesar Cipher")
        self.window.geometry("350x200")
        self.window.resizable(False, False)

        self.createWidgets()

    def createWidgets(self):
        # main page
        title = tk.Label(
            self.window,
            text = "Caesar Cipher",
            font = ("Arial", 20)
        )
        title.pack(pady = 20)

        encryptButton = tk.Button(
            self.window,
            text = "Encrypt",
            width = 15,
            command = self.showEncryptWindow
        )
        encryptButton.pack(pady = 5)

        decryptButton = tk.Button(
            self.window,
            text = "Decrypt",
            width = 15,
            command = self.showDecryptedWindow
        )
        decryptButton.pack(pady = 5)

        exitButton = tk.Button(
            self.window,
            text = "Exit",
            width = 15,
            command = self.exit
        )
        exitButton.pack()

        # needs to be put last
        self.window.mainloop()

    # show windows
    def showEncryptWindow(self):
        window = tk.Toplevel(self.window)
        window.resizable(False, False)
        window.title("Encrypt")
        window.geometry("245x100")

        self.messageEntry = tk.Entry(window)
        self.messageEntry.grid(row = 0, column = 0)
        
        self.keyEntry = tk.Entry(window)
        self.keyEntry.grid(row = 0, column = 1)

        encryptButton = tk.Button(
            window,
            text = "Encrypt",
            command = self.encryptMessage
            )
        encryptButton.grid(row = 1, column = 0, columnspan = 2)

        self.encryptResultLabel = tk.Entry(
            window,
            width = 20,
            state = "readonly"
        )
        self.encryptResultLabel.grid(row = 2, column = 0, columnspan = 2)

    def showDecryptedWindow(self):
        window = tk.Toplevel(self.window)
        window.resizable(False, False)
        window.title("Decryption")
        window.geometry("245x100")

        self.encryptedEntry = tk.Entry(window)
        self.encryptedEntry.grid(row = 0, column = 0)

        self.encryptedKeyEntry = tk.Entry(window)
        self.encryptedKeyEntry.grid(row = 0, column = 1)

        decryptButton = tk.Button(
            window,
            text = "Decrypt",
            command = self.decryptMessage
        )
        decryptButton.grid(row = 1, column = 0, columnspan = 2)

        self.decryptResultLabel = tk.Entry(
            window,
            width = 20,
            state = "readonly"
        )
        self.decryptResultLabel.grid(row = 2, column = 0, columnspan = 2)
    # methods
    def encryptMessage(self):
        message = self.messageEntry.get()
        key = int(self.keyEntry.get())
        encrypted = encrypt(message, key)

        self.encryptResultLabel.config(state = "normal")
        self.encryptResultLabel.delete(0, tk.END)
        self.encryptResultLabel.insert(0, encrypted)
        self.encryptResultLabel.config(state = "readonly")

    def decryptMessage(self):
        message = self.encryptedEntry.get()
        key = int(self.encryptedKeyEntry.get())
        decrypted = decrypt(message, key)

        self.decryptResultLabel.config(
            text = decrypted
        )
        self.decryptResultLabel.config(state = "normal")
        self.decryptResultLabel.delete(0, tk.END)
        self.decryptResultLabel.insert(0, decrypted)
        self.decryptResultLabel.config(state = "readonly")
    
    def exit(self):
        self.window.destroy()
    
    