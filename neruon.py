import tkinter as tk
from tkinter import simpledialog 
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Show an input dialog
count = simpledialog.askstring("Input", "Enter the amount of denderites: ",)
if count is None or not count.isdigit():  # Check if input is valid
    messagebox.showerror("Error", "Invalid input! Please enter a valid number.")
    root.destroy()  # Close the application if input is invalid
    exit()
count = int(count)
vol = [0] * count
w = [0] * count
ans = [0] * count

for x in range(count):
    vol[x] = simpledialog.askstring("Input", "Enter the voltage of denderite")
    vol[x] = float(vol[x])
    w[x] = simpledialog.askstring("Input", "Enter the weight of denderite")
    w[x] = float(w[x])
    x = x + 1
b = simpledialog.askstring("Input", "Enter the bias: ")
b = float(b)
#math time

for x in range(count): #This is for the multiplication
    ans[x] = vol[x] * w[x]

total = sum(ans) + b
print("The output voltage of the neruon is", total)

#step function

if total >= -0.055:
    binary = True
else:
    binary = False


messagebox.showinfo("Output", "The output voltage of the neruon is " + str(total) + " and the binary output is " + str(binary))
question = simpledialog.askstring("Question", "Do you want the data to be saved?")


if question == "yes":
    file = open("data.txt", "w")
    file.write("The amount of dentrdrites is " + str(count) + "\n")
    for x in range(count):
        file.write("The voltage of dendrite " + str(count) + " is " + str(vol[x]) + "\n")
        file.write("The weight of dendrite " + str(count) + " is " + str(w[x]) + "\n")
        x = x + 1
    file.write("The output voltage of the neruon is " + str(total) + " and the binary output is " + str(binary) +"\end" )
    file.close()    
elif question == "no":
    messagebox.showinfo("Output", "The data was not saved")
else:
    messagebox.showinfo("Error", "Invalid input")
root.deiconify()  # Show the main window
root.title("Neruon")
root.geometry("400x400")
root.configure(bg="white")


text_box = tk.Text(root, height=10, width=40, font=("Arial", 12))
text_box.pack(pady=10)

text_box.insert("1.0", "The amount of dentrdrites is " + str(count) + "\n")
for x in range(count):
    text_box.insert("end", "The voltage of dendrite " + str(x) + " is " + str(vol[x]) + "\n")
    text_box.insert( "end " ,"The weight of dendrite " + str(x) + " is " + str(w[x]) + "\n")
    x = x + 1
text_box.insert("end ", "The output voltage of the neruon is " + str(total) + " and the binary output is " + str(binary) +"\n" )
root.mainloop()  # Start the main loop
