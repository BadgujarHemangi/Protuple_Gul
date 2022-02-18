from tkinter import*

root = Tk()
#width x height
root.geometry("644x766")

#width , height
root.minsize(400,300)

#width , height
root.maxsize(1200,1000)

hemangi = Label(text="this is calculator")
hemangi.pack()

root.mainloop()