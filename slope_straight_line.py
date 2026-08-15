"""
Interactive program to calculate the slope of a straight line
Formula: m = (y2 - y1) / (x2 - x1)
"""

def calcular_pendiente():
    """Calculates the slope between two points."""
    print("=" * 50)
    print("Slope Calculator for a Straight Line")
    print("=" * 50)
    
    try:
        # Get coordinates of the first point
        print("\nEnter the coordinates of the first point (x1, y1):")
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        
        # Get coordinates of the second point
        print("\nEnter the coordinates of the second point (x2, y2):")
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        
        # Validate that x1 and x2 are different
        if x1 == x2:
            print("\n❌ Error: x1 and x2 cannot be equal (vertical line).")
            return
        
        # Calculate slope
        pendiente = (y2 - y1) / (x2 - x1)
        
        # Display results
        print("\n" + "=" * 50)
        print("RESULTS:")
        print("=" * 50)
        print(f"Point 1: ({x1}, {y1})")
        print(f"Point 2: ({x2}, {y2})")
        print(f"\nSlope (m) = ({y2} - {y1}) / ({x2} - {x1})")
        print(f"Slope (m) = {pendiente:.4f}")
        print("=" * 50)
        
    except ValueError:
        print("\n❌ Error: Please enter valid numeric values.")

def main():
    """Main function."""
    while True:
        calcular_pendiente()
        
        # Ask if you want to calculate another slope
        respuesta = input("\nDo you want to calculate another slope? (y/n): ").lower().strip()
        if respuesta != 'y':
            print("\nThank you for using the slope calculator!")
            break

if __name__ == "__main__":
    main()
