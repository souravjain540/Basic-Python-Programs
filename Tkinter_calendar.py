from tkinter import *
from tkcalendar import *


win = Tk()
cal = Calendar(win, setmode='date', dateformat='d/m/yy')
cal.pack(padx=15,pady=15)
win.geometry("300x300")
win.title("Calendar")
win.config(bg='gray')
win.resizable(0, 0)



win.mainloop()
