from tkinter import*
def hema(event):
    print(f"you clicked on the button at {event.x},{event.y}")


root=Tk()
root.title("Event in tkinter")
root.geometry("644x345")


widget=Button(root,text="Click me please")
widget.pack()

widget.bind('<Button-1>',hema)

root.mainloop()