#Leetcode 238. Product of Array Except Self

#Descriprion:
#Given an integer array nums, return an array answer 
# such that answer[i] is equal to the product of all 
# the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=1
        b=1
        if nums.count(0)>1:
            return [0]*len(nums)
        for x in nums:
            if x!=0:
                b*=x
            a*=x
        for x in range(len(nums)):
            p=nums[x]
            if p!=0:
                nums[x]=int(a/p)
            else:
                nums[x]=b
        return 
#done
        