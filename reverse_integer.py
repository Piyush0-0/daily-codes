# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits
# reversed. If reversing x causes the value to go outside the signed
# 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit 
# integers (signed or unsigned).

# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        p=x
        if p<0:
            p=p*-1
        p=str(p)
        p=p[::-1]
        p=int(p)
        if x<0:
            p=p*-1
        if p<-(2**31) or p>=(2**31):
            return 0 
        return p