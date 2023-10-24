# Dictionary of exchange rates (as of a specific date)
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.73,
    'JPY': 109.29,
    'CAD': 1.25,
}

# Function to convert an amount from one currency to another
def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates:
        rate_from = exchange_rates[from_currency]
        rate_to = exchange_rates[to_currency]
        converted_amount = amount * (rate_to / rate_from)
        return converted_amount
    else:
        return "Invalid currency code(s)."

# Main program loop
while True:
    print("\nCurrency Converter")
    print("Available Currencies:")
    for currency in exchange_rates:
        print(currency, end=' ')
    print()
    
    from_currency = input("Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()
    
    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        continue
    
    result = convert_currency(amount, from_currency, to_currency)
    
    if isinstance(result, (float, int)):
        print(f"{amount} {from_currency} is equal to {result} {to_currency}")
    else:
        print(result)

    another_conversion = input("Do another conversion? (yes/no): ").lower()
    if another_conversion != "yes":
        print("Goodbye!")
        break
