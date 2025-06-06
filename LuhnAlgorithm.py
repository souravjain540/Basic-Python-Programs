"""
Luhn Algorithm for Credit Card Number Validation

Luhn algorithm is a checksum formula used to validate identification numbers, 
        including credit card numbers.

How it works:
1. Traverse digits from right to left
2. Double every second digit
3. If doubling result > 9, subtract 9
4. Sum all digits
5. If sum % 10 == 0, the number is valid

Author: matei
Date: 2025
"""

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    
    checksum = sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(digit * 2))
    
    return checksum % 10


def is_luhn_valid(card_number):
    """
    Check if a card number is valid according to the Luhn algorithm.
    
    """
    card_str = str(card_number).replace(" ", "").replace("-", "")
    
    if not card_str.isdigit():
        return False
    
    if len(card_str) < 13 or len(card_str) > 19:
        return False
    
    return luhn_checksum(card_str) == 0


def identify_card_type(card_number):
    """
    Identify card type based on prefix and length.

    """
    card_str = str(card_number).replace(" ", "").replace("-", "")
    
    if not card_str.isdigit():
        return "Invalid format"
    
    length = len(card_str)
    
    if card_str.startswith('4') and length in [13, 16, 19]:
        return "Visa"
    elif (card_str.startswith(('51', '52', '53', '54', '55')) or 
          (card_str.startswith('2') and 2221 <= int(card_str[:4]) <= 2720)) and length == 16:
        return "MasterCard"
    elif card_str.startswith(('34', '37')) and length == 15:
        return "American Express"
    else:
        return "Unknown card type"


def generate_luhn_valid_number(prefix, length):
    """
    Generate a Luhn-valid number with given prefix.
    
    """
    import random
    
    if len(prefix) >= length:
        return "Prefix too long for desired length"
    
    number = prefix
    for _ in range(length - len(prefix) - 1):
        number += str(random.randint(0, 9))
    
    for check_digit in range(10):
        test_number = number + str(check_digit)
        if is_luhn_valid(test_number):
            return test_number
    
    return "Could not generate valid number"


def format_card_number(card_number, hide_middle=True):
    """
    Format card number for display.
    
    Args:
        card_number (str): Card number
        hide_middle (bool): Whether to hide middle digits
    
    """
    card_str = str(card_number).replace(" ", "").replace("-", "")
    
    if hide_middle and len(card_str) >= 8:
        return card_str[:4] + " **** **** " + card_str[-4:]
    else:
        return ' '.join([card_str[i:i+4] for i in range(0, len(card_str), 4)])


def validate_and_analyze(card_number):
    """
    Validate and provide detailed analysis of a card number.
    
    """
    card_str = str(card_number).replace(" ", "").replace("-", "")
    
    result = {
        'original': card_number,
        'cleaned': card_str,
        'formatted': format_card_number(card_str, hide_middle=False),
        'is_valid': False,
        'card_type': 'Unknown',
        'length': len(card_str),
        'checksum': None,
        'errors': []
    }
    
    if not card_str.isdigit():
        result['errors'].append("Contains non-digit characters")
        return result
    
    if len(card_str) < 13 or len(card_str) > 19:
        result['errors'].append(f"Invalid length: {len(card_str)} (should be 13-19)")
        return result
    
    result['checksum'] = luhn_checksum(card_str)
    result['is_valid'] = result['checksum'] == 0
    
    if result['is_valid']:
        result['card_type'] = identify_card_type(card_str)
    else:
        result['errors'].append(f"Failed Luhn check (checksum: {result['checksum']})")
    
    return result


def main():

    print("=" * 65)
    print("       CREDIT CARD VALIDATOR - LUHN ALGORITHM")
    print("=" * 65)
    
    test_cards = [
        ("4532015112830366", "Visa - Valid"),
        ("4532015112830367", "Visa - Invalid"),
        ("5555555555554444", "MasterCard - Valid"),
        ("5555555555554443", "MasterCard - Invalid"),
        ("378282246310005", "American Express - Valid"),
        ("371449635398431", "American Express - Valid"),
        ("1234567890123456", "Invalid number"),
    ]
    
    print("\n TESTING CARD NUMBERS:")
    print("-" * 65)
    print(f"{'Card Number':<20} | {'Status':<10} | {'Type':<15} | {'Note'}")
    print("-" * 65)
    
    for card, note in test_cards:
        analysis = validate_and_analyze(card)
        formatted_card = format_card_number(card, hide_middle=True)
        
        status = "VALID, we good bro" if analysis['is_valid'] else "INVALID, not good bro"
        card_type = analysis['card_type'] if analysis['is_valid'] else "N/A"
        
        print(f"{formatted_card:<20} | {status:<10} | {card_type:<15} | {note}")
    
    print("\n" + "=" * 65)
    
    print("\n GENERATING VALID CARD NUMBERS:")
    print("-" * 65)
    
    examples = [
        ("4532", 16, "Visa"),
        ("5555", 16, "MasterCard"),
        ("3782", 15, "American Express"),
    ]
    
    for prefix, length, card_type in examples:
        generated = generate_luhn_valid_number(prefix, length)
        formatted = format_card_number(generated, hide_middle=False)
        is_valid = is_luhn_valid(generated)
        
        print(f"{card_type}: {formatted} {'hehe' if is_valid else 'no'}")
    
    print("\n" + "=" * 65)
    print("\n DETAILED ANALYSIS EXAMPLE:")
    print("-" * 65)
    
    example_card = "378282246310005"
    analysis = validate_and_analyze(example_card)
    
    print(f"Original input: {analysis['original']}")
    print(f"Cleaned number: {analysis['cleaned']}")
    print(f"Formatted: {analysis['formatted']}")
    print(f"Length: {analysis['length']} digits")
    print(f"Luhn checksum: {analysis['checksum']}")
    print(f"Is valid: {'YES, we good' if analysis['is_valid'] else 'NO, :('}")
    print(f"Card type: {analysis['card_type']}")
    
    if analysis['errors']:
        print(f"Errors: {', '.join(analysis['errors'])}")
    
    print("\n" + "=" * 65)
    print("\n INTERACTIVE TESTING:")
    print("Enter a card number to validate (or 'exit' to quit)")
    
    while True:
        user_input = input("\nCard number: ").strip()
        
        if user_input.lower() == 'exit':
            print("bye bye")
            break
        
        if not user_input:
            continue
        
        analysis = validate_and_analyze(user_input)
        
        print(f"\nAnalysis for: {format_card_number(user_input, hide_middle=True)}")
        print("-" * 40)
        
        if analysis['is_valid']:
            print(f"Status: VALID")
            print(f"Type: {analysis['card_type']}")
            print(f"Length: {analysis['length']} digits")
        else:
            print(f"Status: INVALID")
            if analysis['errors']:
                print(f"Issues: {', '.join(analysis['errors'])}")


if __name__ == "__main__":
    main()