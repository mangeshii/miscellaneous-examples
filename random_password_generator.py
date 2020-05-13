import random
import string
import tkinter as tk
from tkinter import *




root=tk.Tk()



def generate_password():
    password = []


    for i in range(3):
        character = random.choice(string.ascii_letters)
        punctuation = random.choice(string.punctuation)
        digit = random.choice(string.digits)
        password.append(character)
        password.append(punctuation)
        password.append(digit)

        z = "".join((x) for x in password)
        lbl.config(text=z)
        

button = Button(root, text="Generate password", command=generate_password)
button.grid(row=0,column=0)

lbl=Label(root,font=('serif',20,'bold'))
lbl.grid(row=1,column=0)

root.mainloop()
