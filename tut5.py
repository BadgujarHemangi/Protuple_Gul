from tkinter import*

def hello():
    print("hello tkinter button")
def name():
    print("name is hema")
root=Tk()
root.geometry("644x432")


frame=Frame(root,borderwidth=6,bg="pink",relief=RAISED)
frame.pack(side=LEFT,anchor=NW)

b1= Button(frame,bg="red",text="Print now",command=hello)
b1.pack(side=RIGHT,padx=23,pady=24)

b2= Button(frame,bg="red",text="tell now",command=name)
b2.pack(side=TOP,padx=23,pady=24)

b3= Button(frame,bg="red",text="Print now")
b3.pack(side=BOTTOM,padx=23,pady=24)

root.mainloop()
