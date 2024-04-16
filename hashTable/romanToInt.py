
def romanToIntLR(s):
    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol Value I 1 V 5 X 10 L 50 C 100 D 500 M 1000 For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. X can be placed before L (50) and C (100) to make 40 and 90. C can be placed before D (500) and M (1000) to make 400 and 900. Given a roman numeral, convert it to an integer.

    Example 1:

    Input: s = "III"
    Output: 3
    Explanation: III = 3.

    Example 2:

    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.

    Example 3:

    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    MMMCMXCIX = 3999
    """
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    # from left to right
    # Time: O(n) where n is len(s)
    # Space = O(1) bc the roman_map is fixed size
    prev = ''
    for i, curr in enumerate(s):
        if i == 0: 
            prev = curr
        else:
            if prev:
                if roman_map[prev] < roman_map[curr]:
                    result += roman_map[curr] - roman_map[prev]
                    prev = ''
                else:
                    result += roman_map[prev]

            if prev:
                if i == len(s) - 1:
                    result += roman_map[curr]
                else:
                    prev = curr
    return result

# from right to left
# Time: O(n) where n is len(s)
# Space = O(1) bc the roman_map is fixed size
def romanToIntRL(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = roman_map[s[len(s) - 1]]
    right = result

    for i in range(len(s) - 2, -1, -1):
        cur = roman_map[s[i]]
        if cur < right:
            result -= cur
        else:
            result += cur
        right = cur
    return result 

def intToRoman(n):
    """
    Time: O(1) bc we iterate thru int_map which has a fixed size of 13 
    Space: O(1) since int_map is fixed size
    """
    int_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    s = ""
    
    sorted_keys = sorted(list(int_map.keys()), reverse=True)
    for num in sorted_keys:
        if (n // num) > 0:
            repeats = n // num
            for i in range(repeats): s += int_map[num]
            n -= num * repeats
    
    return s


def main():
    print("Roman to Int: From left to right")
    print(f'{romanToIntLR("MMMCMXCIX")} should be 3999')
    print(f'{romanToIntLR("MCMXCIV")} should be 1994')
    print(f'{romanToIntLR("LVIII")} should be 58')
    print(f'{romanToIntLR("IV")} should be 4')
    print(f'{romanToIntLR("III")} should be 3')

    print("\nRoman to Int: From right to left")
    print(f'{romanToIntRL("MMMCMXCIX")} should be 3999')
    print(f'{romanToIntRL("MCMXCIV")} should be 1994')
    print(f'{romanToIntRL("LVIII")} should be 58')
    print(f'{romanToIntRL("IV")} should be 4')
    print(f'{romanToIntRL("III")} should be 3')

    print("\nInt to Roman")
    print(intToRoman(3999) == "MMMCMXCIX")
    print(intToRoman(1994) == "MCMXCIV")
    print(intToRoman(58) == "LVIII")
    print(intToRoman(4) == "IV")
    print(intToRoman(3) == "III")


if __name__ == "__main__":
    main()