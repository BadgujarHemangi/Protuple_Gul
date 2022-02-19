from tkinter import *

def getvals():
    print("It work")
    pass

root=Tk()
root.geometry("644x324")
Label(root,text="welcome to hema",font="comicsasms 12 bold",pady=25).grid(row=0,column=3)

name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency Contact")
paymentmode=Label(root,text="Payment Mode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)
paymentmodeentry=Entry(root,textvariable=paymentmodevalue)
foodserviceentry=Entry(root,textvariable=foodservicevalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

foodservice=Checkbutton(text="want to prebook your meal?",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

Button(text="submit",command=getvals).grid(row=7,column=3)

root.mainloop()