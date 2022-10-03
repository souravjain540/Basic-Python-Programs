class Stack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop_(self):
        if not self.stack:
            return
        else:
            return self.stack.pop()

def posteval(expression):
    stk = Stack()
    for i in expression:
        if i.isdigit():
            stk.push(i)
        else:
            a = int(stk.pop_())
            b = int(stk.pop_())
            if i == '^':
                temp = f'{b}**{a}'
                stk.push(str(eval(temp)))
            else:
                temp = f'{b}{i}{a}'
                stk.push(eval(temp))
    return stk.stack[0]

postfix = input("Enter postfix expression: ")
print(posteval(postfix))