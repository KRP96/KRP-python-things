from tkinter import*
import math
import parser
import tkinter.messagebox

#create, sized, background color changed, change can't resizeble and add title name. If we want to change the name root we can change any name of it
root = Tk()
root.title("Scientific Calculator By KRP")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("472x497+0+0")

calc = Frame(root)
calc.grid()

menubar = Menu(calc)

txtDisplay = Entry(calc, font=('arial', 20, 'bold'), bg="white", width=31, justify=RIGHT, bd=2)
txtDisplay.grid(row=0, column=0, columnspan=4 , padx=1)
txtDisplay.insert(0,"0")

#=========================Standerd calculaotr==============================================================
#Create buttons
numberpad = "789456123"
i=0
btn= []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd=2, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)

        i +=1

btnClear =Button(calc, text=chr(67), width=6  , height=2, font=('arial', 20, 'bold'), bd=2, 
                        bg="powder blue").grid(row=1, column=0, pady=1)

btnAllClear =Button(calc, text=chr(67) +chr(69), width=6  , height=2, font=('arial', 20, 'bold'), bd=2, 
                        bg="powder blue").grid(row=1, column=1, pady=1)

btnSq =Button(calc, text="√", width=6  , height=2, font=('arial', 20, 'bold'), bd=2, 
                        bg="powder blue").grid(row=1, column=2, pady=1)

btnAdd =Button(calc, text="+", width=6  , height=2, font=('arial', 20, 'bold'), bd=2, 
                        bg="powder blue").grid(row=1, column=3, pady=1)

btnSub =Button(calc, text="-", width=6  , height=2, font=('arial', 20, 'bold'), bd=2, 
                        bg="powder blue").grid(row=2, column=3, pady=1)

btnMult =Button(calc, text="x", width=6  , height=2, font=('arial', 20, 'bold'), bd=2, 
                        bg="powder blue").grid(row=3, column=3, pady=1)

btnDiv =Button(calc, text="÷", width=6  , height=2, font=('arial', 20, 'bold'), bd=2, 
                        bg="powder blue").grid(row=4, column=3, pady=1)

btnZero =Button(calc, text="0", width=6  , height=2, font=('arial', 20, 'bold'), bd=2, 
                        bg="powder blue").grid(row=5, column=0, pady=1)

btnDot =Button(calc, text=".", width=6  , height=2, font=('arial', 20, 'bold'), bd=2, 
                        bg="powder blue").grid(row=5, column=1, pady=1)

btnNegative =Button(calc, text=chr(177), width=6  , height=2, font=('arial', 20, 'bold'), bd=2, 
                        bg="powder blue").grid(row=5, column=2, pady=1)

btnEqual =Button(calc, text="=", width=6  , height=2, font=('arial', 20, 'bold'), bd=2, 
                        bg="powder blue").grid(row=5, column=3, pady=1)

#==================================Scientific calculator===================================================

btnPi= Button(calc, text="π", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=1, column=4, pady=1)

btnCos= Button(calc, text="Cos", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=1, column=5, pady=1)

btnTan= Button(calc, text="Tan", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=1, column=6, pady=1)

btnSin= Button(calc, text="Sin", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=1, column=7, pady=1)

#===========================================================================================================

btn2Pi= Button(calc, text="2π", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=2, column=4, pady=1)

btnCosh= Button(calc, text="Cosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=2, column=5, pady=1)

btnTanh= Button(calc, text="Tanh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=2, column=6, pady=1)

btnSinh= Button(calc, text="Sinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=2, column=7, pady=1)

#===========================================================================================================

btnlog= Button(calc, text="Log", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=3, column=4, pady=1)

btnExp= Button(calc, text="Exp", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=3, column=5, pady=1)

btnMod= Button(calc, text="Mod", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=3, column=6, pady=1)

btnE= Button(calc, text="e", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=3, column=7, pady=1)

#===========================================================================================================

btnlog2= Button(calc, text="Log2", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=4, column=4, pady=1)

btnDeg= Button(calc, text="Deg", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=4, column=5, pady=1)

btnacosh= Button(calc, text="acosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=4, column=6, pady=1)

btnasinh= Button(calc, text="asinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=4, column=7, pady=1)

#===========================================================================================================

btnlog10= Button(calc, text="Log10", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=5, column=4, pady=1)

btnlog1p= Button(calc, text="Log1p", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=5, column=5, pady=1)

btnExpm1= Button(calc, text="Exmp1", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=5, column=6, pady=1)

btnlgamma= Button(calc, text="lgamma", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                        ).grid(row=5, column=7, pady=1)

#================================Menu and function=========================================================

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator By KRP", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x497+0+0")

def Standerd():
    root.resizable(width=False, height=False)
    root.geometry("472x497+0+0")

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