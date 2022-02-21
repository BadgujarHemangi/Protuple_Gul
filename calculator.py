from tkinter import*
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

            scvalue.set(value)
            screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("500x700")
root.minsize(200,100)
root.maxsize(300,600)

root.title("Calculator")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar= scvalue,font="lucida 30 bold")
screen.pack(fill=X,ipadx =7,pady=5,padx=5)
f = Frame(root,bg="grey")
b = Button(f,text="9",padx=8,pady=5,font="lucida 26 bold")
b.bind("<Button-1>",click)

b.pack(side = LEFT, padx=18,pady=5)
b = Button(f,text="8",padx=8,pady=5,font="lucida 25 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT, padx= 18, pady=5)

b = Button(f,text="7",padx=8,pady=5,font="lucida 25 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT,padx=18 ,pady=5)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="6",padx=8,pady=5,font="lucida 26 bold")
b.bind("<Button-1>",click)

b.pack(side = LEFT, padx=18,pady=5)
b = Button(f,text="5",padx=8,pady=5,font="lucida 25 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT, padx= 18, pady=5)

b = Button(f,text="4",padx=8,pady=5,font="lucida 25 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT,padx=18 ,pady=5)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="3",padx=8,pady=5,font="lucida 26 bold")
b.bind("<Button-1>",click)

b.pack(side = LEFT, padx=18,pady=5)
b = Button(f,text="2",padx=8,pady=5,font="lucida 25 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT, padx= 18, pady=5)

b = Button(f,text="1",padx=8,pady=5,font="lucida 25 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT,padx=18 ,pady=5)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="0",padx=8,pady=5,font="lucida 25 bold")
b.bind("<Button-1>",click)

b.pack(side = LEFT, padx=19,pady=5)
b = Button(f,text="+",padx=8,pady=5,font="lucida 25 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT, padx=19, pady=5)

b = Button(f,text="-",padx=8,pady=5,font="lucida 26 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT,padx=19,pady=5)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="*",padx=8,pady=5,font="lucida 28 bold")
b.bind("<Button-1>",click)

b.pack(side = LEFT, padx=19,pady=5)
b = Button(f,text="/",padx=8,pady=5,font="lucida 25 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT, padx=19, pady=5)

b = Button(f,text="%",padx=8,pady=5,font="lucida 24 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT,padx=18,pady=5)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="=",padx=8,pady=5,font="lucida 25 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT,padx=18 ,pady=5)
f.pack()

b = Button(f,text="C",padx=8,pady=5,font="lucida 23 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT,padx=18 ,pady=5)
f.pack()

b = Button(f,text=".",padx=8,pady=5,font="lucida 29 bold")
b.bind("<Button-1>",click)
b.pack(side = LEFT,padx=18 ,pady=5)
f.pack()

root.mainloop()
