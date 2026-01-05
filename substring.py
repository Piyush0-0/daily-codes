# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring 
# without duplicate characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        l1=0
        for x in range(len(s)-1):
            p=s[x]
            l2=1
            for y in range(x+1,len(s)):
                if s[y] in p:
                    break
                p+=s[y]
                l2+=1
            if l2>l1:
                l1=l2
        return l1
