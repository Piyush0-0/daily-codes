# 113. Path Sum II
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree and an integer targetSum, return all
# root-to-leaf paths where the sum of the node values in the path equals targetSum.
# Each path should be returned as a list of the node values, not node references.
# A root-to-leaf path is a path starting from the root and ending at 
# any leaf node. A leaf is a node with no children.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def lol(arr,sum1,current):
            arr.append(current.val)
            if sum(arr)==sum1 and current.left==None and current.right==None:
                piyu.append(arr)
                return
            if current.left!=None:
                lol(list(arr),sum1,current.left)
            if current.right!=None:
                lol(list(arr),sum1,current.right)      
        piyu=[]
        p=root
        if p!=None:
            lol([],targetSum,p)
        return piyu
        