"""
This module provides a function to determine the number of days in a given month. 
"""


def days_in_month(month):
    """
    Returns the number of days in a given month.
    
    Args:
        month: int (1-12) or str (month name in Spanish or English)
    
    Returns:
        int: number of days in the month
    """
    
    months_days = {
        1: 31, 'enero': 31, 'january': 31,
        2: 28, 'febrero': 28, 'february': 28,
        3: 31, 'marzo': 31, 'march': 31,
        4: 30, 'abril': 30, 'april': 30,
        5: 31, 'mayo': 31, 'may': 31,
        6: 30, 'junio': 30, 'june': 30,
        7: 31, 'julio': 31, 'july': 31,
        8: 31, 'agosto': 31, 'august': 31,
        9: 30, 'septiembre': 30, 'september': 30,
        10: 31, 'octubre': 31, 'october': 31,
        11: 30, 'noviembre': 30, 'november': 30,
        12: 31, 'diciembre': 31, 'december': 31
    }
    
    if isinstance(month, str):
        month = month.lower()
    
    if month in months_days:
        return months_days[month]
    else:
        return "Invalid month. Use a number (1-12) or month name."


def main():
    """Main interactive function."""
    print("=" * 60)
    print("📅 DAYS IN MONTH CALCULATOR 📅")
    print("=" * 60)
    print("\nYou can enter a month as:")
    print("  • Number (1-12)")
    print("  • Month name in Spanish (enero, febrero, etc.)")
    print("  • Month name in English (January, February, etc.)\n")
    
    while True:
        try:
            # Get user input
            user_input = input("Enter a month (or type 'exit' to quit): ").strip()
            
            # Check if user wants to exit
            if user_input.lower() == 'exit':
                print("\n👋 Thank you for using the Days in Month Calculator! Goodbye!")
                break
            
            # Try to convert to integer
            try:
                month_num = int(user_input)
                result = days_in_month(month_num)
            except ValueError:
                # If not a number, treat as month name
                result = days_in_month(user_input)
            
            # Display result
            if isinstance(result, int):
                print(f"\n✅ Result: {result} days\n")
                print("=" * 60 + "\n")
            else:
                print(f"\n❌ {result}\n")
                print("Examples: 1, January, Enero, 6, June, Junio")
                print("=" * 60 + "\n")
        
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
