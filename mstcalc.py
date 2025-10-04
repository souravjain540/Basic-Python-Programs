########################################
#### Run using `python mstcalc.py` ####
########################################

import tkinter as tk

precedence = {
    '^': 8,
    '*': 4, '/': 4, '%': 4,
    '+': 2, '-': 2,
    '(': 1,
    '#': 0
}

def split_exp(expression):
    nums = []
    num = ""
    prev_char = None
    i = 0

    while i < len(expression):
        ch = expression[i]

        if ch.isdigit() or ch == '.':
            num += ch
        elif ch == '-' and (prev_char is None or prev_char in ('(', '+', '-', '*', '/', '^', '%')):
            if i + 1 < len(expression) and expression[i+1] == '(':
                nums.append('-1')
                nums.append('*')
            else:
                num = ch
        else:
            if num != "":
                nums.append(num)
                num = ""
            if ch.strip():
                nums.append(ch)

        if ch.strip():
            prev_char = ch
        i += 1

    if num != "":
        nums.append(num)

    return nums

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def infix_to_postfix(expression):
    postfix = []
    st = ['#']

    spl = split_exp(expression)

    for i in spl:
        if is_number(i):
            postfix.append(i)
        elif i == '(':
            st.append(i)
        elif i == ')':
            while st[-1] != '#' and st[-1] != '(':
                postfix.append(st.pop())
            if st[-1] == '(':
                st.pop()
        else:
            while st[-1] != '#' and ((precedence[st[-1]] > precedence.get(i, 0)) or (precedence[st[-1]] == precedence.get(i, 0) and i != '^')):
                postfix.append(st.pop())
            st.append(i)

    while st[-1] != '#':
        postfix.append(st.pop())

    return postfix

def stack_eval(expression):
    postfix = infix_to_postfix(expression)
    
    st = []
    for i in postfix:
        if is_number(i):
            st.append(float(i))
        else:
            a = st.pop()
            b = st.pop()
            
            if i == '+':
                st.append(b + a)
            elif i == '-':
                st.append(b - a)
            elif i == '*':
                st.append(b * a)
            elif i == '/':
                st.append(b / a)
            elif i == '%':
                st.append(b % a)
            elif i == '^':
                st.append(b ** a)
            else:
                raise ValueError(f"Unknown operator: {i}")
            
    return st[0]

def press_enter(event):
    click("=")

def click(button_text = None, event = None):
    if button_text == "=":
        try:
            expr = entry.get()
            result = stack_eval(expr)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            if entry.get() == "Error":
                root.after(500, lambda: entry.delete(0, tk.END))
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "√":
        entry.insert(tk.END, "^(1/2)")
    elif button_text == "1/x":
        entry.insert(tk.END, "^(-1)")
    elif button_text is not None:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Stack-Based Calculator")

root.bind("<Return>", press_enter)
root.bind("<BackSpace>", lambda e: entry.delete(len(entry.get())-1, tk.END))
root.bind("<Escape>", lambda e: entry.delete(0, tk.END))

entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+',
    '%','^','√','1/x',
    'C'
]

row = 1
col = 0
for b in buttons:
    action = lambda x=b: click(x)
    tk.Button(root, text=b, width=6, height=2, command=action, font=('Arial', 12), padx=3, pady=3).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
