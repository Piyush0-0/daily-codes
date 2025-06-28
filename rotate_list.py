# 61. Rotate List
# Given the head of a linked list, rotate the list 
# to the right by k places.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a=0
        p=head
        while p!=None:
            a+=1
            p=p.next
        if a==0:
            return None
        elif a==1 or k==0 or k%a==0:
            return head
        q=k%a
        r=a-q
        p=head
        for x in range(r-1):
            p=p.next
        m=p.next
        n=m
        p.next=None
        while m.next!=None:
            m=m.next
        m.next=head
        head=n
        return head
