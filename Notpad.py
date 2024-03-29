from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled-Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file == asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                  filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        # save as new file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + "-Notepad")
        print("Files saved")



def separatorFile():
    pass


def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))


def about():
    showinfo("Notepad", "Notepad by code with Hema")


root = Tk()
root.title("Untitled - Notepad")
root.geometry("644x788")

# Add TextArea
TextArea = Text(root, font="lucida 13")
file = None
TextArea.pack(expand=True, fill=BOTH)

# Lets create a MenuBar
MenuBar = Menu(root)
# files menu start
FileMenu = Menu(MenuBar, tearoff=0)
# To open new file
FileMenu.add_command(label="New", command=newFile)

# to open already exisiting file
FileMenu.add_command(label="Open", command=openFile)

# To save curent file
FileMenu.add_command(label="Save", command=saveFile)
FileMenu.add_command(label="Separator", command=separatorFile)
FileMenu.add_command(label="Exit", command=quitApp)
MenuBar.add_cascade(label="File", menu=FileMenu)

# File menu end

# Edit menu starts
EditMenu = Menu(MenuBar, tearoff=0)
# To give a feature of
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)
MenuBar.add_cascade(label="Edit", menu=EditMenu)
# Edit menu end

# Help menu starts
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label="About Notepad", command=about)
MenuBar.add_cascade(label="help", menu=HelpMenu)
# Help menu end


root.config(menu=MenuBar)

# adding scrollbar using
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()