class Solution:
    def isValid(self, s: str) -> bool:
        listed = list(s)
        if not len(listed) % 2 == 0:
            return False
        types = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        for i in range(2):
            for _ in listed:
                for opening_bracket_index, opening_bracket in enumerate(listed):
                    if opening_bracket in types.values():
                        if opening_bracket_index == 0:
                            return False
                        continue
                    try:
                        closing_bracket_index = listed.index(types[opening_bracket])
                    except ValueError:
                        return False # means closing bracket doesn't exist in list
                    if closing_bracket_index == opening_bracket_index+1:
                        listed.pop(closing_bracket_index)
                        listed.pop(opening_bracket_index)
        
        return True if len(listed) == 0 else False

print(Solution().isValid("()([{}])()") == True)
print(Solution().isValid("()") == True)
print(Solution().isValid("()[]{}") == True)
print(Solution().isValid("{[()]}") == True)
print(Solution().isValid("({})[]") == True)
print(Solution().isValid("({[)}") == False)
print(Solution().isValid("({[}])") == False)
print(Solution().isValid("]") == False)
print(Solution().isValid("((()))") == True)
print(Solution().isValid("[") == False)
print(Solution().isValid("(]") == False)
