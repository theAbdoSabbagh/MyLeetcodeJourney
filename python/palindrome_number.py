# Since negative numbers do not have the negative symbol on both sides
# it means all negative numbers cannot be palindromes

# I cant figure out a way to reverse it without converting to a string
# so ill just solve the main problem only, not the followup

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

print(Solution().isPalindrome(121)) # True
print(Solution().isPalindrome(263)) # False
print(Solution().isPalindrome(2632938)) # False
print(Solution().isPalindrome(12321)) # True
print(Solution().isPalindrome(-12321)) # False
print(Solution().isPalindrome(10)) # False
