"""
This program calculates the Euclidean distance between two points in a Cartesian plane.
For more information about Euclidean distance, you can visit: https://en.wikipedia.org/wiki/Euclidean_distance
"""

# Import the module to perform mathematical operations (Square root)
import math


def euclidean_distance(x1, y1, x2, y2):
    """
    Calculates the Euclidean distance between two points (x1, y1) and (x2, y2).
    
    Parameters:
        x1, y1: coordinates of the first point
        x2, y2: coordinates of the second point 
    
    Returns:
        The Euclidean distance between the two points.
    """
    
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    print("=" * 55)
    print("📍 EUCLIDEAN DISTANCE CALCULATOR 📍")
    print("=" * 55)
    print("\nCalculates the distance between two points in a Cartesian plane.\n")
    
    while True:
        try:
            print("\n--- Enter the coordinates of the FIRST POINT ---")
            while True:
                try:
                    x1 = float(input("x1: "))
                    y1 = float(input("y1: "))
                    
                    if x1 < 0 or y1 < 0:
                        print("❌ Error: Numbers cannot be negative. Please enter positive values.")
                        continue
                    break
                except ValueError:
                    print("❌ Error: Please enter valid numbers.")
                    continue
            
            print("\n--- Enter the coordinates of the SECOND POINT ---")
            while True:
                try:
                    x2 = float(input("x2: "))
                    y2 = float(input("y2: "))
                    
                    if x2 < 0 or y2 < 0:
                        print("❌ Error: Numbers cannot be negative. Please enter positive values.")
                        continue
                    break
                except ValueError:
                    print("❌ Error: Please enter valid numbers.")
                    continue
            
            distance = euclidean_distance(x1, y1, x2, y2)
            
            print("\n" + "=" * 55)
            print(f"✅ RESULT:")
            print(f"   Point 1: P1({x1}, {y1})")
            print(f"   Point 2: P2({x2}, {y2})")
            print(f"   Euclidean distance: {distance:.4f} units")
            print("=" * 55)
            
            while True:
                continuar = input("\nDo you want to calculate another distance? (y/n): ").strip().lower()
                if continuar in ["y", "n"]:
                    break
                print("❌ Please enter 'y' or 'n'.")
            
            if continuar == "n":
                print("\n👋 Thank you for using the Euclidean Distance Calculator!")
                break
        
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
