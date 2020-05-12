from tkinter import *
import tkinter as tk
from tkinter.ttk import *

root=tk.Tk()
style=Style()
root.title('stopwatch')
root.geometry("240x140")
root.configure(bg='black')
style.configure('TButton',font=('arial',10,'bold'),borderwidth="5")

second=0;minute=0;hour=0;stop=True

def start():
    global second,minute,hour,stop
    
    second += 1
    if second==60:
        minute += 1
        second =0
    if minute == 60:
        hour += 1
        minute=0    
    if stop==True:
        lbl=Label(root,text='%s:%s:%s'%(hour,minute,second),font=('arial',30,'bold'),foreground='red',width=10,background='black')
        lbl.after(1000,start)
        lbl.place(x=50,y=60)

 
def stopped():
    global stop
    stop=False
    
         
start_button=Button(root,text="Start",command=start)
stop_button=Button(root, text="Stop",command=stopped)

start_button.grid(row=0, column=0)
stop_button.grid(row=0 ,column=1)

root.mainloop()
