import tkinter as tk
from tkinter import ttk
master=tk.Tk()
master.title("combobox")
master.geometry("100x100")
ttk.Label(master,text="Tkinter life",background="blue",foreground="white",
         font=("times new remoes",10)).grid(row=0,column=1)

#Combobox

K=tk.StringVar()
SpecialForm=ttk.Combobox(master,w=20,textvariable=K)
SpecialForm['values']=("DATA","AI&ML","BANK")
SpecialForm.grid(column=1,row=4)
SpecialForm.current
master.mainloop()

