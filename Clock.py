from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock-By-KRP")
root.geometry("550x125")
root.configure(bg="black")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor="center")
time()

mainloop()