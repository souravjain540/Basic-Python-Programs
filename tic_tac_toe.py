from tkinter import *
from tkinter import messagebox
import random as r
import functools


def button(f):
    button1 = Button(f, text=" ", fg="Black", font="Arial 20 bold", height=1, width=2, padx=25, pady=20, bg="White", borderwidth=0,
                         activebackground="White", cursor="hand2", state=NORMAL)
    return button1


def full():
    for row in range(3):
        for col in range(3):
            if b[row][col]['text'] == " ":
                return False
    return True


def empty():
    for row in range(3):
        for col in range(3):
            b[row][col].config(text=" ", state=NORMAL)


def winner(s):
    return b[0][0]['text'] == b[0][1]['text'] == b[0][2]['text'] == s or b[1][0]['text'] == b[1][1]['text'] == b[1][2]['text'] == s\
            or b[2][0]['text'] == b[2][1]['text'] == b[2][2]['text'] == s or b[0][0]['text'] == b[1][0]['text'] == b[2][0]['text'] == s\
            or b[0][1]['text'] == b[1][1]['text'] == b[2][1]['text'] == s or b[0][2]['text'] == b[1][2]['text'] == b[2][2]['text'] == s\
            or b[0][0]['text'] == b[1][1]['text'] == b[2][2]['text'] == s or b[0][2]['text'] == b[1][1]['text'] == b[2][0]['text'] == s


user_checked = []
com_checked = []


def click(event, param1, param2):
    sign = 0
    if (param1, param2) in user_checked or (param1, param2) in com_checked:
        messagebox.showwarning("Warning", "Select Another Box.")
    else:
        user_checked.append((param1, param2))
        b[param1][param2]['text'] = 'O'

        if winner("O"):
            messagebox.showinfo("Winner", "You Won...")
            user_score.set(user_score.get() + 1)
            empty()
            user_checked.clear()
            com_checked.clear()
            sign = 1

        if full():
            messagebox.showinfo("Tie", "Match Tie...!")
            tie_score.set(tie_score.get() + 1)
            empty()
            user_checked.clear()
            com_checked.clear()
            sign = 1

        if sign == 0:
            unchecked = []
            for row in range(3):
                for col in range(3):
                    if b[row][col]['text'] == " ":
                        unchecked.append([row, col])
            index = r.sample(unchecked, 1)
            b[index[0][0]][index[0][1]].config(text="X", state=DISABLED)
            com_checked.append((index[0][0], index[0][1]))
            if winner("X"):
                messagebox.showinfo("Winner", "Computer Won...")
                com_score.set(com_score.get() + 1)
                empty()
                user_checked.clear()
                com_checked.clear()
        else:
            pass


root = Tk()
root.title("Tic Tac Toe")
root.geometry("420x500")
root.resizable(0, 0)
root.configure(bg="Black")
Label(root, text="TIC TAC TOE", fg="White", bg="Black", font="times 25 bold").pack()

Frame(root, bg="White").pack(fill=X, pady=10)
frame = Frame(root, bg="Black")
Label(frame, text="YOU", fg="Yellow", bg="Black", font="System 10 bold", padx=50, pady=5).pack(side=LEFT)
Label(frame, text="TIE", fg="Yellow", bg="Black", font="System 10 bold", padx=48, pady=5).pack(side=LEFT)
Label(frame, text="COMPUTER", fg="Yellow", bg="Black", font="System 10 bold", padx=30, pady=5).pack(side=LEFT)
frame.pack(pady=5)

frame = Frame(root, bg="Black")
user_score = IntVar()
tie_score = IntVar()
com_score = IntVar()
user_score.set(0)
tie_score.set(0)
com_score.set(0)
user = Entry(frame, textvariable=user_score, fg="white", bg="Black", font="System 10 bold", width=10, borderwidth=0,
      justify=CENTER)
user.pack(side=LEFT, padx=35)
tie = Entry(frame, textvariable=tie_score, fg="white", bg="Black", font="System 10 bold", width=10, borderwidth=0,
      justify=CENTER)
tie.pack(side=LEFT, padx=15)
com = Entry(frame, textvariable=com_score, fg="white", bg="Black", font="System 10 bold", width=10, borderwidth=0,
      justify=CENTER)
com.pack(side=LEFT, padx=50)
frame.pack(pady=10)

Frame(root, bg="White").pack(fill=X, pady=15)

b = [[], [], []]
for i in range(3):
    frame = Frame(root, highlightbackground="Black", highlightthickness=3, bg="Black")
    for j in range(3):
        b[i].append(button(frame))
        b[i][j].bind("<Button-1>", functools.partial(click, param1=i, param2=j))
        b[i][j].pack(side=LEFT, padx=5)
        frame.pack()

root.mainloop()
