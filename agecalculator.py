import tkinter as tk # import tkinter
from tkinter import messagebox # import messagebox to show messages
from datetime import date # import date


main_window = tk.Tk()
main_window.title("Age Calculator") # window title
main_window.geometry("600x500+500+200") # the size and positioning
main_window.configure(bg="pink") # backgroundcolor
main_window.resizable(False,False) # window not resizable

def calculateage():
    '''
    Gets year, month, day from the user
    :return: the age
    '''
    try:
        if first_entry.get() == "" or second_entry.get() == "" or third_entry.get() == "":
            messagebox.showerror("Error", "data not entered")
        else:
            years = int(first_entry.get())
            months = int(second_entry.get())
            days = int(third_entry.get())
            year = date.today().year - years
            month = date.today().month - months
            day = date.today().day - days
            statement = "You are " + str(year)\
                        + " years " + str(month) + " month " + " and " + str(day) + " days old "
            messagebox.showinfo("message", statement)
    except ValueError:
        messagebox.showinfo("Error", "Input integers")
    except:
        messagebox.showerror("Error", "You have an error")

# widget and their positioning

title_label = tk.Label(text="AGE CALCULATOR!!!", font=("Algerian",17))
title_label.place(x=170,y=2)

first_label = tk.Label(text="Input year of birth", font=("Algerian",17))
first_label.grid(row=1,column=0,pady=40)

first_entry = tk.Entry(font=("Algerian",17))
first_entry.grid(row=1,column=1)

second_label = tk.Label(text="Input month of birth", font=("Algerian",17))
second_label.grid(row=2,column=0,pady=40,padx=5)

second_entry = tk.Entry(font=("Algerian",17))
second_entry.grid(row=2,column=1)

third_label = tk.Label(text="Input day of birth", font=("Algerian",17))
third_label.grid(row=3,column=0,pady=40)

third_entry = tk.Entry(font=("Algerian",17))
third_entry.grid(row=3,column=1)

age_button = tk.Button(text="Calculate Age",font=("Algerian",17), command=calculateage)
age_button.grid(row=4,column=1)

main_window.mainloop()