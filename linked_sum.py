# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=ListNode()
        root=a
        s1=0
        s2=0
        while l1!=None:
            s1=(s1*10)+l1.val
            l1=l1.next
        while l2!=None:
            s2=(s2*10)+l2.val
            l2=l2.next
        s1+=s2
        for x in str(s1):
            a.val=int(x)
            b=ListNode()
            c=a
            a.next=b
            a=b
        c.next=None
        return root