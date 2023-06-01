# Since negative numbers do not have the negative symbol on both sides
# it means all negative numbers cannot be palindromes
# we will use the % and // operators to solve this problem without converting it to a string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # negative is not palindrome
            return False # i added this check because its faster than doing the other code and then
        # checking if its a palindrome
        
        original_x = x
        reversed_x = 0
        while x > 0:
            last_digit = x % 10 # % 10 will give the last digit no matter what
            # % 100 would give the last 2 digits, meaning for every 0, u get that amount of last digits
            # if there is more 0s than the amount of the digits, youll just get the whole digits
            # same applies if the 0s are equal to the amount of digits
            
            reversed_x = (reversed_x * 10) + last_digit # the reason i multiple by 10 is
            # lets say the number is 20, if i add the last digit, lets say 5, itll be 25
            # but i dont want it to be 25, i want it to be 205, so what i do is i add an extra zero
            # and u do that by multiplying the original number with 10
            # then i add the number
            # its as if im "placing" the number at the end

            x = x // 10 # here I remove the last digit
            # the normal / operator just divides, and it does floating (float) point dividing
            # but the // operator does "floor dividing"
            # an example is
            # 5 / 2 is is 2.50
            # but 5 // 2 is 2
            # its like converting the number to an int instead of keeping it as a float
            # and instead of rounding the number upwards, u round it downwards

        return reversed_x == original_x # if theyre palindrome, the numbers must be the same, returning True
        # otherwise itll return False meaning the number is not a palindrome


print(Solution().isPalindrome(121)) # True
print(Solution().isPalindrome(263)) # False
print(Solution().isPalindrome(2632938)) # False
print(Solution().isPalindrome(12321)) # True
print(Solution().isPalindrome(-12321)) # False
print(Solution().isPalindrome(10)) # False
