
"""
This module allows solving any problem about the Pythagorean theorem, it also verifies if three numbers meet the relationship a² + b² = c².
For more information about the Pythagorean theorem, you can visit: https://en.wikipedia.org/wiki/Pythagorean_theorem

"""

# Import the module to perform mathematical operations (Square root)
import math

def pythagorean_theorem(a=None, b=None, c=None):
    """
    Solves the Pythagorean theorem: a² + b² = c²
    
    Parameters:
        a: side a (or None if you want to calculate it)
        b: side b (or None if you want to calculate it)
        c: hypotenuse (or None if you want to calculate it)
    
    Returns:
        Tuple with the values (a, b, c)
    """
    if a is None:
        if b is not None and c is not None:
            a = math.sqrt(c**2 - b**2)
        else:
            raise ValueError("At least two values are needed")
    elif b is None:
        if a is not None and c is not None:
            b = math.sqrt(c**2 - a**2)
        else:
            raise ValueError("At least two values are needed")
    elif c is None:
        if a is not None and b is not None:
            c = math.sqrt(a**2 + b**2)
        else:
            raise ValueError("At least two values are needed")
    
    return (a, b, c)


def verify_pythagorean(a, b, c):
    """
    Verifies if three numbers satisfy the Pythagorean theorem. 
    They are normally called Pythagorean triples.
    parameters:
        a: side a
        b: side b
        c: hypotenuse
    Returns:
        True if they satisfy the theorem, False otherwise.
    """
    return abs(a**2 + b**2 - c**2) < 1e-10


if __name__ == "__main__":
    print("=" * 50)
    print("🔺 PYTHAGOREAN THEOREM CALCULATOR 🔺")
    print("=" * 50)
    print("\nPythagorean Theorem: a² + b² = c²\n")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Calculate the hypotenuse (c) knowing the legs (a, b)")
        print("2. Calculate a leg knowing the other and the hypotenuse")
        print("3. Verify if three numbers form a right triangle")
        print("4. Exit")
        
        opcion = input("\nSelect an option (1-4): ").strip()
        
        if opcion == "1":
            print("\n--- Calculate Hypotenuse ---")
            try:
                a = float(input("Enter the value of leg a: "))
                b = float(input("Enter the value of leg b: "))
                
                if a <= 0 or b <= 0:
                    print("\u274c Values must be greater than 0")
                    continue
                
                a, b, c = pythagorean_theorem(a=a, b=b)
                print(f"\n✅ Results:")
                print(f"   Leg a: {a:.2f}")
                print(f"   Leg b: {b:.2f}")
                print(f"   Hypotenuse c: {c:.2f}")
                print(f"   Verification: a² + b² = c² → {a**2:.2f} + {b**2:.2f} = {c**2:.2f} ✓")
            except ValueError as e:
                print(f"\u274c Error: {e}")
            except Exception as e:
                print(f"\u274c Invalid input. Please enter valid numbers.")
        
        elif opcion == "2":
            print("\n--- Calculate a Leg ---")
            print("Which leg do you want to calculate?")
            print("a) Calculate leg a")
            print("b) Calculate leg b")
            
            cateto_opcion = input("Select (a/b): ").strip().lower()
            
            try:
                if cateto_opcion == "a":
                    b = float(input("Enter the value of leg b: "))
                    c = float(input("Enter the value of hypotenuse c: "))
                    
                    if b <= 0 or c <= 0 or b >= c:
                        print("\u274c Invalid values. The hypotenuse must be greater than the leg.")
                        continue
                    
                    a, b, c = pythagorean_theorem(b=b, c=c)
                    print(f"\n✅ Results:")
                    print(f"   Leg a: {a:.2f}")
                    print(f"   Leg b: {b:.2f}")
                    print(f"   Hypotenuse c: {c:.2f}")
                    print(f"   Verification: a² + b² = c² → {a**2:.2f} + {b**2:.2f} = {c**2:.2f} ✓")
                
                elif cateto_opcion == "b":
                    a = float(input("Enter the value of leg a: "))
                    c = float(input("Enter the value of hypotenuse c: "))
                    
                    if a <= 0 or c <= 0 or a >= c:
                        print("\u274c Invalid values. The hypotenuse must be greater than the leg.")
                        continue
                    
                    a, b, c = pythagorean_theorem(a=a, c=c)
                    print(f"\n✅ Results:")
                    print(f"   Leg a: {a:.2f}")
                    print(f"   Leg b: {b:.2f}")
                    print(f"   Hypotenuse c: {c:.2f}")
                    print(f"   Verification: a² + b² = c² → {a**2:.2f} + {b**2:.2f} = {c**2:.2f} ✓")
                else:
                    print("\u274c Invalid option")
            except ValueError:
                print("\u274c Invalid input. Please enter valid numbers.")
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif opcion == "3":
            print("\n--- Verify Right Triangle ---")
            try:
                a = float(input("Enter the value of a: "))
                b = float(input("Enter the value of b: "))
                c = float(input("Enter the value of c (hypotenuse): "))
                
                if a <= 0 or b <= 0 or c <= 0:
                    print("\u274c Values must be greater than 0")
                    continue
                
                es_rectangulo = verify_pythagorean(a, b, c)
                
                print(f"\n✅ Analysis:")
                print(f"   a² + b² = {a**2:.2f} + {b**2:.2f} = {(a**2 + b**2):.2f}")
                print(f"   c² = {c**2:.2f}")
                
                if es_rectangulo:
                    print(f"   ✓ YES, it is a right triangle (Pythagorean triple)!")
                else:
                    diferencia = abs(a**2 + b**2 - c**2)
                    print(f"   ✗ NO, it is not a right triangle (difference: {diferencia:.2f})")
            except ValueError:
                print("\u274c Invalid input. Please enter valid numbers.")
        
        elif opcion == "4":
            print("\n👋 Thank you for using the Pythagorean Calculator! See you soon!")
            break
        
        else:
            print("\u274c Invalid option. Please select 1, 2, 3, or 4.")
