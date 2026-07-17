import tkinter as tk

class ToDoGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do List")
        self.window.geometry("400x300")
        self.window.resizable(False, False)

        self.createWidgets()
        self.window.mainloop()
    
    # home page
    def createWidgets(self):
        font = ("Arial", 12)

        # title frame/label
        titleFrame = tk.Frame(self.window)
        titleFrame.pack()
        titleLabel = tk.Label(
            titleFrame,
            text = "To-Do List",
            font = ("Arial", 20)
        ) 
        titleLabel.pack()

        # input frame/label
        inputFrame = tk.Frame(self.window)
        inputFrame.pack()
        self.inputEntry = tk.Entry(inputFrame, width = 20, font = font)
        self.inputEntry.pack(side = "left", padx = 5, pady = 10)
        self.inputEntry.bind(
            "<Return>",
            self.addItem
        )
        inputButton = tk.Button(
            inputFrame,
            text = "Add Item",
            font = font,
            width = 20,
            command = self.addItem
        )
        inputButton.pack(side = "right", pady = 5)

        # list frame/box
        listFrame = tk.Frame(self.window)
        listFrame.pack()
        self.todoList = tk.Listbox(
            listFrame,
            width = 30,
            height = 5,
            font = font
        )
        self.todoList.pack()
        self.todoList.bind(
            "<Delete>",
            self.removeItem
        )
        self.todoList.bind(
            "<Backspace>",
            self.removeItem
        )

        buttonsFrame = tk.Frame(self.window)
        buttonsFrame.pack()
        removeButton = tk.Button(
            buttonsFrame,
            text = "Remove Selected",
            font = font,
            width = 20,
            command = self.removeItem
        )
        removeButton.pack(pady = 2)
        clearButton = tk.Button(
            buttonsFrame,
            text = "Clear All",
            font = font,
            width = 20,
            command = self.clearAll
        )
        clearButton.pack(pady = 2)

        exitButton = tk.Button(
            buttonsFrame,
            text = "Exit",
            font = font,
            width = 20,
            command = self.exit
        )
        exitButton.pack(pady = 2)


    def addItem(self, event = None):
        item = self.inputEntry.get()

        self.todoList.insert(
            tk.END,
            item
        )

        self.inputEntry.delete(
            0, tk.END
        )

    def removeItem(self, event = False):
        selected = self.todoList.curselection() # returns index of selected item

        if selected:
            self.todoList.delete(selected)

    def clearAll(self):
        self.todoList.delete(
            0,
            tk.END
        )

    def exit(self):
        self.window.destroy()
