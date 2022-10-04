import time
from tkinter import *


def click(event):
    global strval
    text = event.widget.cget("text")
    if text == "=":
        if strval.get().isdigit():
            strval.set((strval.get()))
        elif strval.get() == "":
            pass
        else:
            try:
                print(strval.get())
                strval.set(eval(strval.get()))
            except Exception as e:
                strval.set("Error")
                screen.update()
                print(e)
                time.sleep(1)
                strval.set("")
        screen.update()
    elif text == "C":
        strval.set("")
        screen.update()
    elif text == "←":
        value = strval.get()
        strval.set(value[:-1])
        screen.update()
    else:
        strval.set(strval.get() + text)
        screen.update()


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("270x490")

    @staticmethod
    def createbutton(frame, t, ifont, x, y, iside, ix):
        button = Button(frame, text=t, font=ifont, padx=x, pady=y)
        button.pack(side=iside, padx=ix)
        button.bind("<Button-1>", click)


if __name__ == '__main__':
    root = GUI()
    root.title("Calculator")
    root.resizable(0, 0)

    strval = StringVar()
    strval.set("")
    screen = Entry(root, textvar=strval, font="system 25", borderwidth=3, relief=SUNKEN, justify=RIGHT, insertwidth=0)
    screen.pack(fill=X, pady=5, padx=3)

    num = 9
    for _ in range(3):
        f = Frame(root, bg="black")
        for _ in range(3):
            root.createbutton(f, f"{num}", "times 20 bold", 15, 5, RIGHT, 3)
            num = num - 1
        f.pack(pady=5)

    f = Frame(root, bg="black")
    root.createbutton(f, ".", "times 20 bold", 18, 5, LEFT, 3)
    root.createbutton(f, "0", "times 20 bold", 15, 5, LEFT, 3)
    root.createbutton(f, "C", "times 20 bold", 11, 5, LEFT, 3)
    f.pack(pady=5)

    f = Frame(root, bg="black")
    root.createbutton(f, "+", "times 20 bold", 14, 5, LEFT, 3)
    root.createbutton(f, "=", "times 20 bold", 15, 5, LEFT, 3)
    root.createbutton(f, "←", "times 20 bold", 8, 5, LEFT, 3)
    f.pack(pady=5)

    f = Frame(root, bg="black")
    root.createbutton(f, "-", "times 20 bold", 17, 5, LEFT, 3)
    root.createbutton(f, "*", "times 20 bold", 15, 5, LEFT, 3)
    root.createbutton(f, "/", "times 20 bold", 18, 5, LEFT, 3)
    f.pack(pady=5)

    root.mainloop()
