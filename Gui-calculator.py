from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(scvalue.get())
            except Exception as e:
                  scvalue.set("Math Error!!!")
                  screen.update()
              
        scvalue.set(value)
        screen.update()
    elif text=="c"or text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
root=Tk()
root.geometry('400x600')
root.title('Hamza calculator')

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

#button making using for loop
f=Frame(root,bg='grey')
for i in range(7,11):
    if i !=10:
         b=Button(f,text=str(i),padx=10,pady=5 ,font="lucida 30 bold")
    else:
        b=Button(f,text='*',padx=12,pady=5 ,font="lucida 30 bold")
    b.pack(side=LEFT,padx=10,pady=5)
    b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg='grey')
for i in range(4,8):
    if i !=7:
         b=Button(f,text=str(i),padx=10,pady=5 ,font="lucida 30 bold")
    else:
        b=Button(f,text='/',padx=15,pady=5 ,font="lucida 30 bold")
    b.pack(side=LEFT,padx=10,pady=5)
    b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg='grey')
for i in range(1,5):
    if i !=4:
         b=Button(f,text=str(i),padx=10,pady=5 ,font="lucida 30 bold")
    else:
        b=Button(f,text='+',padx=10.4,pady=5 ,font="lucida 30 bold")
    b.pack(side=LEFT,padx=10,pady=5)
    b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg='grey')
for i in range(0,4):
    if i ==0:
         b=Button(f,text='00',padx=0,pady=5 ,font="lucida 30 bold")
    elif i==1:
        b=Button(f,text='0',padx=10,pady=5 ,font="lucida 30 bold")
    elif i==2:
        b=Button(f,text='.',padx=15,pady=5 ,font="lucida 30 bold")
    elif i==3:
        b=Button(f,text='-',padx=15,pady=5 ,font="lucida 30 bold")
    b.pack(side=LEFT,padx=10,pady=5)
    b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg='grey')
for i in range(0,4):
    if i ==0:
         b=Button(f,text='%',padx=5,pady=5 ,font="lucida 30 bold")
    elif i==1:
        b=Button(f,text='C',padx=6,pady=5 ,font="lucida 30 bold")
    elif i==2:
        b=Button(f,text='**',padx=5,pady=5 ,font="lucida 30 bold")
    elif i==3:
        b=Button(f,text='=',padx=10,pady=5 ,font="lucida 30 bold")
    b.pack(side=LEFT,padx=10,pady=5)
    b.bind("<Button-1>",click)
f.pack()

root.mainloop()