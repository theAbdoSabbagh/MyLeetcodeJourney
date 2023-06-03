class Solution:
    def romanToInt(self, s: str) -> int:
        conversion_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "N/A": 0
        }
        roman_values = [conversion_values[r_num] for r_num in list(s)]
        values = []
        for index, num in enumerate(roman_values):
            if index == len(roman_values)-1:
                values.append(num)
            else:
                values.append(num if roman_values[index+1] <= num else num*-1)

        return sum(values)

if __name__ == "__main__":
    print(Solution().romanToInt("IV")) # 4
    print(Solution().romanToInt("III")) # 3
    print(Solution().romanToInt("LVIII")) # 58
    print(Solution().romanToInt("MCMXCIV")) # 1994
    print(Solution().romanToInt("MMV")) # 2005
    print(Solution().romanToInt("MMVI")) # 2006
    print(Solution().romanToInt("LXIX")) # 69
    print(Solution().romanToInt("CDXX")) # 420
    print(Solution().romanToInt("CXXVIII")) # 128
