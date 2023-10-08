import tkinter as tk
from time import strftime

# Create a function to get the current time
def time():
    string = strftime('%H:%M:%S %p')  # Format time as 'HH:MM:SS AM/PM'
    label.config(text=string)
    label.after(1000, time)  # Update time every 1000ms (1 second)

# Create a Tkinter window
root = tk.Tk()
root.title("Digital Clock")

# Create a label widget for displaying the time
label = tk.Label(root, font=('arial', 40, 'bold'), background="#ADD8E6", foreground="#F08080")
label.pack(anchor='center')

# Run the time function to display the initial time and update it
time()

# Run the Tkinter event loop
root.mainloop()
