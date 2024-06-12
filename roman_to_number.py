
def solution(roman):
    '''
    Psudocode -->
    if current value is less than the next value:
        subtract from the total
    else:
        add to the total
    
    '''
    numeral = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    the_int = 0
    
    for i in range(len(roman)):
        if i + 1 < len(roman) and numeral[roman[i]] < numeral[roman[i+1]]:
            the_int -= numeral[roman[i]]
        else:
            the_int += numeral[roman[i]]
    return the_int


# Test cases
print(solution('IV'))
print(solution('MCCXXXIV'))
print(solution('V'))
print(solution('CCC'))
