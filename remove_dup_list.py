# 83. Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates such that 
# each element appears only once. Return the linked list sorted as well.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        p=head
        q=head.next
        while q!=None:
            if q.val==p.val:
                m=q.next
                p.next=m
                q=m
            else:
                m=q.next
                p=q
                q=m
        return head