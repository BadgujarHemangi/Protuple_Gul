from tkinter import*
import tkinter.messagebox as tmg


root=Tk()
root.title("radio tutorial")
root.geometry("623x354")

def order():
    tmg.showinfo("Order recieve:",f"we have received your order for {var.get()} thank for ordering")

var=StringVar()
#var.set(1)
Label(root,text="What would you like to have sir?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="Idly",padx=14,variable=var,value="Idly").pack(anchor=W)
radio=Radiobutton(root,text="Dosa",padx=14,variable=var,value="Dosa").pack(anchor=W)
radio=Radiobutton(root,text="Paneer",padx=14,variable=var,value="Paneer").pack(anchor=W)

Button(text="order now",command=order).pack()

root.mainloop()