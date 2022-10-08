#LeetCode problem 13 Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict= {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        numeral= 0
        string = s.replace("CD", "CCCC").replace("CM", "DCCCC").replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX")
        for i in string:
            numeral = numeral + roman_dict[i]
        return numeral