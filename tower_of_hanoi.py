"""
Tower of Hanoi - Classic recursive problem
Move n disks from source to destination using auxiliary rod
Rules: Only one disk can be moved at a time, and larger disk cannot be on smaller disk
"""

def tower_of_hanoi(n, source, destination, auxiliary, moves=None):
    """
    Solve Tower of Hanoi puzzle
    
    Args:
        n: Number of disks
        source: Source rod name
        destination: Destination rod name
        auxiliary: Auxiliary rod name
        moves: List to store moves (optional)
    """
    if moves is None:
        moves = []
    
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        moves.append(move)
        return moves
    
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination, moves)
    
    # Move the largest disk from source to destination
    move = f"Move disk {n} from {source} to {destination}"
    print(move)
    moves.append(move)
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source, moves)
    
    return moves


def calculate_minimum_moves(n):
    """Calculate minimum number of moves required"""
    return 2**n - 1


if __name__ == "__main__":
    print("=" * 50)
    print("TOWER OF HANOI SOLVER")
    print("=" * 50)
    
    try:
        n = int(input("\nEnter number of disks: "))
        
        if n <= 0:
            print("Please enter a positive number!")
        else:
            print(f"\nMinimum moves required: {calculate_minimum_moves(n)}")
            print("\nSolution:")
            print("-" * 50)
            
            moves = tower_of_hanoi(n, 'A', 'C', 'B')
            
            print("-" * 50)
            print(f"\nTotal moves: {len(moves)}")
            
    except ValueError:
        print("Invalid input! Please enter a valid number.")
