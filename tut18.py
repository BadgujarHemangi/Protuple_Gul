from tkinter import *

root = Tk()
root.title("scrollbar tutorial")
root.geometry("634x354")
# for connecting scrollbar to a widget
# 1.widget(vsscrollcommand=scrollbar.set)
# 2.scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END, f"Item{i}")
    listbox.pack(padx=24, pady=35)

    scrollbar.config(command=listbox.yview)
root.mainloop()