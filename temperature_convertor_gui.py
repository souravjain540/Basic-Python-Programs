from tkinter import *
import tkinter.messagebox as tmsg

def calculate():
    c = c_value.get()
    f = f_value.get()
    k = k_value.get()
    if c !=0:
        f = (c*(9/5)) + 32
        k = c + 273.15
        f_value.set(f)
        k_value.set(k)
    elif f != 0:
        c = (f-32) * (5/9)
        k = ((5/9) + f) + 459.67
        c_value.set(c)
        k_value.set(k)
    elif k != 0:
        c = k - 273.15
        f = ((k - 273.15) * (9/5)) + 32
        c_value.set(c)
        f_value.set(f)
    else:
        tmsg.showerror("Error","Enter 1 value and press calculate")

def show():
    show_root = Tk()
    show_root.title("Formula List")
    show_root.geometry("300x300")
    show_root.minsize(300,300)
    show_root.maxsize(300,300)
    show_root.configure(bg = "powder blue")
    lbs = Label(show_root,bg = "powder blue", text="Formulae: " ,font ="comicsansms 12 bold", padx=5, pady=5)
    lbs.grid(row=0, column=3)
    lbs = Label(show_root,bg = "powder blue", text="Celsius conversion: \nF = (9/5 x C) + 32 \nK = C + 273.15 " ,font ="comicsansms 10 bold",padx=5)
    lbs.grid(row=1, column=3)
    lbs = Label(show_root,bg = "powder blue", text="Fahrenheit conversion: \nC = (F - 32) x 5/9 \nK = (5/9 x F) + 459.67 " ,font ="comicsansms 10 bold",padx=5)
    lbs.grid(row=2, column=3)
    lbs = Label(show_root,bg = "powder blue", text="Kelvin conversion: \nC = K - 273.15 \nF = ((K - 273.15) x 9/5) + 32 ", font="comicsansms 10 bold", padx=5)
    lbs.grid(row=3, column=3)
    show_root.mainloop()

def reset():
    c_value.set(0)
    f_value.set(0)
    k_value.set(0)

root = Tk()
root.title("Temperature Converter")
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)
root.configure(bg="orange")

lb = Label(root, text="Temperature converter", bg="orange", fg="white", font = "comicsansms 20 bold", padx=10, pady=20)
lb.grid(row=0,column=3)

lb_c = Label(root, text="Celsius", bg="orange", padx=10, pady=10, font="comicsansms 14", fg="white")
lb_c.grid(row=1, column=2)
lb_f = Label(root, text="Fahrenheit", bg="orange", padx=10, pady=10, font="comicsansms 14", fg="white")
lb_f.grid(row=2, column=2)
lb_k = Label(root, text="Kelvin", bg="orange", padx=10, pady=10, font="comicsansms 14", fg="white")
lb_k.grid(row=3, column=2)

c_value = IntVar()
f_value = IntVar()
k_value = IntVar()

c_entry = Entry(root,textvariable=c_value)
c_entry.grid(row=1,column=3)
f_entry = Entry(root,textvariable=f_value)
f_entry.grid(row=2,column=3)
k_entry = Entry(root,textvariable=k_value)
k_entry.grid(row=3,column=3)

fr = Frame(root)
fr.grid(row=5,column=3)
l = Label(bg="orange")          #Empty label
l.grid(row=4)
b = Button(fr, text="Calculate", command=calculate, width=15)
b.grid(row=5, column=3)

fr = Frame(root)
fr.grid(row=7,column=3)
l = Label(bg="orange")          #Empty label
l.grid(row=6)
b = Button(fr, text="Reset", command=reset, width=15)
b.grid(row=7, column=3)

fr = Frame(root)
fr.grid(row=5,column=2)
b = Button(fr, text="Show conversion formulas", command=show)
b.grid(row=5, column=2)

root.mainloop()
