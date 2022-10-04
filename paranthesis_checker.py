"""
Paranthesis checker checks to see if in a given array all paranthesis
are closed, if so the function returns true otherwise false. 
i.e. {}, [], (), and ([]) would return true, }, or ([)] would return  
false. A stack is implemented to check only when a }, ], or ) are 
present in array.
Note that if nothing is entered the function returns true.
"""

def parenthesis_check(parenthesis_array):

    stack = []
    for parenthesis in parenthesis_array:
        if parenthesis == '}':
            if len(stack) == 0:
                return False
            prev_parenthesis = stack.pop()
            if prev_parenthesis != '{':
                return False
        elif parenthesis == ']':
            if len(stack) == 0:
                return False
            prev_parenthesis = stack.pop()
            if prev_parenthesis != '[':
                return False
        elif parenthesis == ')':
            if len(stack) == 0:
                return False
            prev_parenthesis = stack.pop()
            if prev_parenthesis != '(':
                return False  
        else: stack.append(parenthesis)
    
    if len(stack) > 0:
        return False
    else:
        return True

str = input("Input: ")
arr = list(str)
print(parenthesis_check(arr))