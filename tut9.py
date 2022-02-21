from tkinter import *

root=Tk()
Canvas_width=800
Canvas_height=400
root.geometry(f"{Canvas_width}x{Canvas_height}")
root.title("Canvas tkinter")
Can_widget=Canvas(root,width=Canvas_width,height=Canvas_height)
Can_widget.pack()

#The line goes from the point x1,y1 to x2,y2
Can_widget.create_line(0,0,800,400,fill="red")
Can_widget.create_line(0,400,800,0,fill="red")

#to create a rectangle specify parameters in this order _coors of Top left,coors of Bottom right
Can_widget.create_rectangle(3,5,700,300,fill="blue")
Can_widget.create_text(200,200,text="python")

Can_widget.create_oval(344,233,244,355)

root.mainloop()