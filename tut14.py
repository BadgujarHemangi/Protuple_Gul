from tkinter import *
import tkinter.messagebox as tmg
root=Tk()
root.title("slider tutorial")
root.geometry("455x324")

def getdollar():
    print("we have credited {myslider2.get()}dollars to your bank account")
    tmg.showinfo("amont credited:",f"we have credit{myslider2.get()} dollars to your bank account")


myslider2= Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
#myslider2.set(32)
myslider2.pack()

Button(root,text="GetDollar",pady=10,command=getdollar).pack()

root.mainloop()