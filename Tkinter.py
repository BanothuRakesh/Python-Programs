import tkinter 
from tkinter import*
from tkinter import messagebox

master=tkinter.Tk()
master.title("Rakesh")
master.geometry("500x500")
#label
#label=tkinter.Label(master,text="Hello").pack()
'''
#button
b=Button(master,text="Sister",bg="white",fg="red")
b.grid(column=1,row=0)
#radio
r=Radiobutton(master,text="Keerthana",value=1)
r.grid(column=2,row=1)
r1=Radiobutton(master,text="Sravani",value=2)
r1.grid(column=2,row=2)
#entry
K=Entry(master,width=20)
K.grid(column=3,row=0)'''
#message
def Button1():
    messagebox.showinfo("story","two sisters")

b=Button(master,text="Tkinter life",command=Button1)
b.pack()






master.mainloop()
