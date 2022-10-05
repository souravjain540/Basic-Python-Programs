def romanToInt(s: str) -> int:
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000
                  }

    sum = 0
    for i in range(len(s)):
        if len(s)-1 != i:
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                sum -= roman_dict[s[i]]

            elif roman_dict[s[i]] == roman_dict[s[i+1]]:
                sum += roman_dict[s[i]]
            else:
                sum += roman_dict[s[i]]
        else:
            sum += roman_dict[s[i]]

    return sum


u_roman = input("Enter Roman Numeral: ")
print(romanToInt(u_roman))
