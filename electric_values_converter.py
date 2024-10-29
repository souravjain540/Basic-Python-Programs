def convert_electric_values():
    """
    This program compute electric values. User enter 2 values and
    the program compute the unknown values.
    """
    
    print("Enter 2 of this 4 following values:")
    print("1. Current (I -> A)")
    print("2. Voltage (V -> V)")
    print("3. Resitance (R -> Ω)")
    print("4. Power (P -> W)")
    
    I = None
    V = None
    R = None
    P = None

    while True:
        input_number = 0
        try:
            I_input = input("Enter current value (I -> A) or hit 'enter' if unknown : ")
            if I_input.strip() != "":
                I = float(I_input)
                input_number += 1
            V_input = input("Enter voltage value (V -> V) or hit 'enter' if unknown : ")
            if V_input.strip() != "":
                V = float(V_input)
                input_number += 1
            R_input = input("Enter resitance value (R -> Ω) or hit 'enter' if unknown : ")
            if R_input.strip() != "":
                R = float(R_input)
                input_number += 1
            P_input = input("Enter power value (P -> W) or hit 'enter' if unknown : ")
            if P_input.strip() != "":
                P = float(P_input)
                input_number += 1

            if(input_number > 2):
                print("You have entered more than 2 values! Please enter exactly 2 values")
                continue
            if(input_number < 2):
                print("You have entered less than 2 values! Please enter exactly 2 values")
                continue
            break
        except ValueError:
            print("Please enter a valid value!")

    # Calcul des valeurs manquantes
    if I is not None and V is not None:
        R = V / I  
        P = I * V  

    elif I is not None and R is not None:
        V = I * R  
        P = I * V  

    elif V is not None and R is not None:
        I = V / R 
        P = I * V  

    elif I is not None and V is not None:
        P = I * V  
        R = V / I  

    elif I is not None and P is not None:
        V = P / I  
        R = V / I if I != 0 else float('inf')  

    elif V is not None and P is not None:
        I = P / V 
        R = V / I if I != 0 else float('inf')  

    elif R is not None and P is not None:
        I = P / (V if V is not None else (R * I if I is not None else float('inf')))  
        V = P / I if I != 0 else float('inf')  

    
    print("\nResults :")
    if I is not None:
        print(f"Current (I) : {I:.2f} A")
    if V is not None:
        print(f"Voltage (V) : {V:.2f} V")
    if R is not None:
        print(f"Resistance (R) : {R:.2f} Ω")
    if P is not None:
        print(f"Power (P) : {P:.2f} W")
        

if __name__ == "__main__":
    while True:
        convert_electric_values()
        
        convert_again = input("\nConvert again? yes / no: ").lower()
        if convert_again != "yes":
            break
