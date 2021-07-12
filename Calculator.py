from tkinter import*
import math
#import parser
import tkinter.messagebox

#create, sized, background color changed, change can't resizeble and add title name. If we want to change the name root we can change any name of it
root = Tk()
root.title("Scientific Calculator By KRP")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("475x568+0+0")

calc = Frame(root)
calc.grid()

menubar = Menu(calc)

txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg="white", width=31, justify=RIGHT, bd=2)
txtDisplay.grid(row=0, column=0, columnspan=4 , padx=1)
txtDisplay.insert(0,"0")

numberpad = "789456123"
i=0
btn= []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd=2, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)

        i +=1

#================================Menu and function=======================================

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator By KRP", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568+0+0")

def Standerd():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

#create file menubar option
filemenu = Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "File", menu=filemenu)
filemenu.add_cascade(label= "Standerd", command= Standerd)
filemenu.add_cascade(label= "Scientific", command= Scientific)
filemenu.add_separator()
filemenu.add_cascade(label= "Exit", command= iExit)

#create edit menubar option
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label= "Edit", menu=editmenu)
editmenu.add_cascade(label= "Cut")
editmenu.add_cascade(label= "Copy")
editmenu.add_separator()
editmenu.add_cascade(label= "Paste")

#create help menubar option
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label= "Help", menu=helpmenu)
helpmenu.add_cascade(label= "View Help")

#call the window
root.config(menu=menubar)
root.mainloop()