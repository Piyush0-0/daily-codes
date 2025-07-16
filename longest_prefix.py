# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst 
# an array of strings.
# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        a=""
        for x in range(len(min(strs))):
            flag=0
            char=strs[0][x]
            for y in strs:
                if y[x]==char:
                    flag+=1
            if flag==len(strs):
                a+=char
            else:
                break
        return(a)