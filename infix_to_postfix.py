Operators= set(["+","-","*","/","(",")","^"])
Priority = {"-":1,"+":1,"*":2,"/":2,"^":3}

def infix_to_postfix(expression):
    stack=[]
    output =""

    for character in expression:
        if character not in Operators:
            output+=character
        elif character == "(":
            stack.append("(")
        elif character==")":
            while stack and stack[-1] != "(":
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(" and Priority[character] <= Priority[stack[-1]]:
                output += stack.pop()

            stack.append(character)

    while stack:
        output+=stack.pop()
    return output

expression= input("Enter infix expression ")

print("infix notation: ",expression)
      
print("postfix notation: ",infix_to_postfix(expression))            
            

        
            
