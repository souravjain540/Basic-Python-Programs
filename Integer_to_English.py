from collections import deque
from string import digits

def number2words(num):

    int_to_word = {
        1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five', 6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten',
        11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen', 15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen',
        18 : 'Eighteen', 19 : 'Nineteen', 20 : 'Twenty', 30 : 'Thirty', 40 : 'Fourty', 50 : 'Fifty', 60 : 'Sixty',
        70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety'
    }

    digits_to_word = {
        3 : 'Thousand', 6 : 'Million', 9 : 'Billion', 12 : 'Trillion', 15 : 'Quadrillion', 18 : 'Quintillion', 21 : 'Sextillion',
        24 : 'Septillion', 27 : 'Octillion', 30 : 'Nontillion'
    }

    english = deque()
    digits = 0
    if num == 0:
        return "Zero"

    while num:
        num, section = divmod(num, 1000)        #section in the block of 3 digits
        hundreds, tens = divmod(section, 100)

        if section and digits > 0:
            english.appendleft(digits_to_word[digits])
        digits += 3

        if tens >= 20:
            if tens%10:
                english.appendleft(int_to_word[tens % 10])
            english.appendleft(int_to_word[10 * (tens // 10)])
        elif tens:
            english.appendleft(int_to_word[tens])

        if hundreds:
            english.appendleft("Hundred")
            english.appendleft(int_to_word[hundreds])

    return " ".join(english)


"""
Example test case -->
Input: num = 1234567
"""

print(number2words(num = 1234567))

"""
Output: One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
"""