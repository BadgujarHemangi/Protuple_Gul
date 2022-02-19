from tkinter import *

def getvals():
 print(f"the is username{uservalue.get()}")
 print(f"the is password{passvalue.get()}")

root=Tk()
root.geometry("654x433")


user=Label(root,text="Username")
password=Label(root,text="Password")
user.grid()
password.grid(row=1)

uservalue =StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="submit",command=getvals).grid()

root.mainloop()
