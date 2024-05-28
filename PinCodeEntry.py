#Imports
import tkinter as tk
from tkinter import ttk

#Root setting
root = tk.Tk()
root.title("PIN code entry")

root.geometry("259x203")
root.resizable(False, False)

#PIN system
pin = ""
correctPin = "0110"
showPin = False

#Button press command
def buttonPress(value):
    global pin
    #Add number to pin unless pin is already at max length (37 digits)
    pin += value if len(pin) < 37 else ""
    showPinToggle()

#Delete last digit of pin
def delete():
    "Deletes last digit of pin code"
    global pin
    pin = pin[0:len(pin)-1]
    if showPin: pincodeLabel.config(text=f"Pin: {pin if pin != '' else '_'}")
    else: pincodeLabel.config(text=f"Pin: {'*'*len(pin) if pin != '' else '_'}")

#Chekc the pin entered
def checkPin():
    global pin
    if pin == correctPin:
        showPinToggle(text="Correct pin!")
    
    else:
        pin = ""
        showPinToggle(text="Wrong pin!")

#Toggle showing the pin
def showPinToggle(swap=False, text=None):
    #Make variable global
    global showPin
    global pin

    #Swap states
    if swap:
        showPin = not showPin
        if showPin: showPinButton.config(text="Hide pin")
        else: showPinButton.config(text="Show pin")

    #Show custom text
    if text != None: showText = text

    #Show pin or hide pin
    else:
        #Show pin
        if showPin: showText = f"Pin: {pin if pin != '' else '_'}"
        #Hide pin
        else: showText = f"Pin: {'*'*len(pin) if pin != '' else '_'}"

    pincodeLabel.config(text=showText)



#Automated system
#Button class
class Button():
    def __init__(self, value, column, row, padx, pady):
        self.value = value
        self._button = ttk.Button(root, text=self.value, command=lambda: buttonPress(self.value))
        self._button.grid(column=column, row=row, padx=padx, pady=pady)

#Setup
count = 0
numButtons = [
    [],
    [],
    []
]

#Make buttons
for i in range(3):
    for j in range(3):
        numButtons[i].append(Button(str(count), j, i, 5, 5))
        count += 1
numButtons.append(Button(str(count), 1, 3, 5, 5))

#Label showing pincode
pincodeLabel = ttk.Label(root, text="Pin: _")
pincodeLabel.grid(row=4, columnspan=3, padx=5, pady=5)

#Make the delete button
deleteButton = ttk.Button(root, text="Delete", command=delete)
deleteButton.grid(column=0, row=5, padx=5, pady=5)

#Make the ok button
okButton = ttk.Button(root, text="Ok", command=checkPin)
okButton.grid(column=1,row=5, padx=5, pady=5)

#Button to show / hide pincode
showPinButton = ttk.Button(root, text="Show Pin", command=lambda: showPinToggle(swap=True))
showPinButton.grid(row=5, column=2, padx=5, pady=5)

#Main loop
root.mainloop()
