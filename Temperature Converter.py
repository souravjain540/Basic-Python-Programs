### Temperature Converter

import os

def clear():
    os.system('cls')

clear()

print("Pick a conversion type: F to C, C to F, C to K, K to C, F to K, K to F")
while(True):
    user_input = input()

    if(user_input.lower() == "f to c"):
        print("\nEnter temperature: ")
        fahrenheit = int(input())
        celsius = int((fahrenheit - 32) * 5/9)
        clear()
        print(f"{fahrenheit}°F is {celsius}°C")
    elif(user_input.lower() == "c to f"):
        print("\nEnter temperature: ")
        celsius = int(input())
        fahrenheit = int((celsius * 9/5) + 32)
        clear()
        print(f"{celsius}°C is {fahrenheit}°F")
    elif(user_input.lower() == "c to k"):
        print("\nEnter temperature: ")
        celsius = int(input())
        kelvin = celsius + 273.15
        print(f"{celsius}°C is {kelvin}°K")
        clear()
    elif(user_input.lower() == "k to c"):
        print("\nEnter temperature: ")
        kelvin = int(input())
        celsius = kelvin - 273.15
        clear()
        print(f"{kelvin}°K is {celsius}°C")
    elif(user_input.lower() == "f to k"):
        print("\nEnter temperature: ")
        fahrenheit = int(input())
        kelvin = int((fahrenheit - 32) * 5/9 + 273.15)
        clear()
        print(f"{fahrenheit}°F is {kelvin}°K")
    elif(user_input.lower() == "k to f"):
        print("\nEnter temperature: ")
        kelvin = int(input())
        fahrenheit = int((kelvin - 273.15) * 9/5 + 32)
        clear()
        print(f"{kelvin}°K is {fahrenheit}°F")
    else:
        print("\nInvalid input. Enter supported conversion type: ")
        print("F to C, C to F, C to K, K to C, F to K, K to F")