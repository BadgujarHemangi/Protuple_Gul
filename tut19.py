from tkinter import *

def upload():
    statusvar.set("Busy....")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")

root =Tk()
root.title("status bar tutorial")
root.geometry("634x354")

statusvar=StringVar()
statusvar.set("Ready")
sbar=Label(root,textvariable=statusvar,relief=SUNKEN,anchor=W)
sbar.pack(side=BOTTOM,fill=X)

Button(root,text="Upload",command=upload).pack()

root.mainloop()
