# 11. Container With Most Water
# You are given an integer array height of length n. There are n 
# vertical lines drawn such that the two endpoints of the ith line are 
# (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.
# Return the maximum amount of water a container can store.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        water=0
        a,b=0,len(height)-1
        while a<b:
            x=(b-a)*min(height[a],height[b])
            if x>water:
                water=x
            if height[a]>=height[b]:
                b-=1
            else:
                a+=1
        return water