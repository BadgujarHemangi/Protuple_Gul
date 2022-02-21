from tkinter import *
import tkinter.messagebox as tmg

root=Tk()
root.title("pycharm")
root.geometry("623x345")

def myfunc():
    print("this is an tkinter software in laptop")

def help():
    print("I will help you")
    tmg.showinfo("Help","hema help you")

def rate():
     print("Rate us")
     value= tmg.askquestion("was your experince good?", "you used thid gui...was your experience good?")
     if value=="yes":
         msg="Great.Rate us "
     else:
         msg="Tell us went wrong "
         tmg.showinfo("Experience",msg)

def divya():
    ans=tmg.askretrycancel("divya as be friendship","sorry divya does not accept your friendship")
    if ans:
        print("Retry this")
    else:
        print("most better cancel")


mainmenu= Menu(root)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save As",command=myfunc)
m1.add_command(label="Print",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_separator()
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Find",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="menu",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate",command=rate)
m3.add_command(label="Divya",command=divya)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m3)



root.mainloop()