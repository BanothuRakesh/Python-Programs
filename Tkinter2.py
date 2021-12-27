import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
master=tk.Tk()
master.title("scrolltext")
master.geometry("500x500")
ttk.Label(master,text="Tkinter life",background="blue",foreground="white",
         font=("times new remoes",10)).grid(row=0,column=1)

#Scrolltext

SpecialForm1=scrolledtext.ScrolledText(master,wrap=tk.WORD,width=20,height=20)
SpecialForm1.grid(column=1,padx=10,pady=10)
SpecialForm1.focus()


master.mainloop()

