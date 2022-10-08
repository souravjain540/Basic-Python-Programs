#LeetCode problem 12 Integer to Roman
class Solution:
    def intToRoman(self, input):
        numeral= [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman= ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        romanLower= list(map(lambda x: x.lower(), roman)) 
        res=""
        for tmp in range(len(numeral)):
            while input >= numeral[tmp]:
                res= res+roman[tmp]
                input-= numeral[tmp]

        return res
