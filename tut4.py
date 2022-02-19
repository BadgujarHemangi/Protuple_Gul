from tkinter import*

root=Tk()
root.geometry("655x455")
f1=Frame(root, bg="grey",borderwidth=5,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
f2=Frame(root, bg="grey",borderwidth=5,relief=SUNKEN)
f2.pack(side=RIGHT,fill="x")
l=Label(f1,text="project tkinter _ pycharm")
l.pack(pady=142)
l1=Label(f2,text="welcome project",font="helvetica 16 bold",fg="green",bg="blue")
l1.pack(pady=156)

root.mainloop()