from tkinter import*

root = Tk()
root.geometry("444x233")
root.title("my document with hema")

#Important label options
#Text-adds the text
#BG-BACKGROUND
#FG=FORGROUND
#FRONT=SETS THE FRONT
#1.font=("comicsasms 19 bold")
#2.font=("comicsasms,19,bold")
#PADX=PADDINGX
#PADY=pADDINGY

title_label = Label(text='''The son of film director David Dhawan, he studied business management from the Nottingham
\nTrent University. He began his work in the film industry as an assistant director to Karan Johar on the drama film My Name
\nIs Khan (2010), and subsequently made his acting debut in 2012 with Johar's teen drama Student of the Year. 
\nDhawan has been featured in eleven consecutive box-office successes between 2012 and 2018.[2][3][4][5]''',bg="pink",padx=28,pady=44,
font=("comicsasms 19 bold"),borderwidth=3,relief=SUNKEN)

#important pck
# anchor=NW
#side=top,bottom,left,right
#fill

title_label.pack(side=TOP,anchor=NW,fill=X)


root.mainloop()