from tkinter import*
import math
#import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator By KRP")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "File", menu=filemenu)
filemenu.add_cascade(label= "Standerd")
filemenu.add_cascade(label= "Scientific")
filemenu.add_separator()
filemenu.add_cascade(label= "Exit")

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label= "Edit", menu=filemenu)
filemenu.add_cascade(label= "Cut")
filemenu.add_cascade(label= "Copy")
filemenu.add_separator()
filemenu.add_cascade(label= "Paste")

root.config(menu=menubar)
root.mainloop()