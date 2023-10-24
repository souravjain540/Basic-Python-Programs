from tkinter import *

class Calculator:
    
    def __init__(self,win):
        win.title("Calculator")
        win.geometry("357x420")
        win.config(bg='black')
        win.resizable(0,0)
        
        self.expression=StringVar()
        self.input_value=""
        Entry(width=17,bg='#fff',font=('Arial Bold',28),textvariable=self.expression).place(x=0,y=0)
        
        
        
        Button(width=11,height=4,text='7',relief='flat',bg='white',command=lambda:self.show(7)).place(x=0,y=125)
        Button(width=11,height=4,text='8',relief='flat',bg='white',command=lambda:self.show(8)).place(x=90,y=125)
        Button(width=11,height=4,text='9',relief='flat',bg='white',command=lambda:self.show(9)).place(x=180,y=125)
        Button(width=11,height=4,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=0,y=200)
        Button(width=11,height=4,text='5',relief='flat',bg='white',command=lambda:self.show(5)).place(x=90,y=200)
        Button(width=11,height=4,text='6',relief='flat',bg='white',command=lambda:self.show(6)).place(x=180,y=200)
        Button(width=11,height=4,text='1',relief='flat',bg='white',command=lambda:self.show(1)).place(x=0,y=275)
        Button(width=11,height=4,text='3',relief='flat',bg='white',command=lambda:self.show(3)).place(x=180,y=275)
        Button(width=11,height=4,text='2',relief='flat',bg='white',command=lambda:self.show(2)).place(x=90,y=275)
        Button(width=11,height=4,text='0',relief='flat',bg='white',command=lambda:self.show(0)).place(x=90,y=350)
        Button(width=11,height=4,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=180,y=350)
        Button(width=11,height=4,text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=270,y=275)
        Button(width=11,height=4,text='-',relief='flat',bg='white',command=lambda:self.show('-')).place(x=270,y=200)
        Button(width=11,height=4,text='/',relief='flat',bg='white',command=lambda:self.show('/')).place(x=270,y=50)
        Button(width=11,height=4,text='x',relief='flat',bg='white',command=lambda:self.show('x')).place(x=270,y=125)
        Button(width=11,height=4,text='=',relief='flat',bg='white',command=self.solve).place(x=270,y=350)
        Button(width=11,height=4,text='C',relief='flat',bg='white',command=self.clear).place(x=0,y=350)
    
    def show(self,input):
        self.input_value+=str(input)
        self.expression.set(self.input_value)

    def clear(self):
        self.input_value=''
        self.expression.set(self.input_value)

    
    def solve(self):
        result=eval(self.input_value)
        self.expression.set(result)
        
    def calculate(self):
        result=eval(self.input_value)
        self.expression.set(result)
        
    


win=Tk()
calculator=Calculator(win)
win.mainloop()