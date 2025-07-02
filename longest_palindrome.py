# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        a=""
        for y in range(len(s)):
            for x in range(y,len(s)):
                p=s[y:x+1]
                if p==p[::-1] and len(p)>len(a):
                    a=p
        return a