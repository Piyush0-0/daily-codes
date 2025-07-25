# 3487. Maximum Unique Subarray Sum After Deletion
# You are given an integer array nums.
# You are allowed to delete any number of elements from nums 
# without making it empty. After performing the deletions, select
# a subarray of nums such that:
# All elements in the subarray are unique.
# The sum of the elements in the subarray is maximized.
# Return the maximum sum of such a subarray.

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max1=[]
        for x in nums:
            if x not in max1 and x>0:
                max1.append(x)
        if len(max1)==0:
            return max(nums)
        return sum(max1)