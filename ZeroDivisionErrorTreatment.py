# Function below:
def division(x: int, y: int):
    try:
        return x / y
    except ZeroDivisionError:
        return None # Error Handled

# tests
print(division(2, 3)) # 0.66666666...
print(division(6, 0)) # None