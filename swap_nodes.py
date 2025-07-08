# 24. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes 
# and return its head. You must solve the problem without 
# modifying the values in the list's nodes 
# (i.e., only nodes themselves may be changed.)
# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        elif head.next==None:
            return head
        a=head
        bhead=a.next
        c=bhead.next
        bhead.next=a
        a.next=c
        flag=a
        a=c
        while a!=None:
            if a.next==None:
                break
            b=a.next
            c=b.next
            flag.next=b
            b.next=a
            flag=a
            a.next=c
            a=c
        return bhead