# 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node 
# from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a=head
        b=0
        while a!=None:
            b+=1
            a=a.next
        b=b-n
        if b==0:
            return head.next
        a=head
        while b!=0:
            flag=a
            a=a.next
            b-=1
        flag.next=a.next
        return head
        