from time import strftime
from tkinter import *
import tkinter as tk
from tkinter.ttk import *



root=tk.Tk()
root.title()

def time():
    string=strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(100,time)



lbl=Label(root,font=('arial',30,'bold'),background='black',foreground='white')
lbl.pack(anchor=CENTER)

time()

root.mainloop()