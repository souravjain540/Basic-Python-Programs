def suma(slist): #  SUMMATORY
    sum = 0
    for x in slist: 
        if not (type(x) == int and type(x) == float): 
            sum += x
        else:
            raise ValueError("Item in list wasn't a number")
    return sum
