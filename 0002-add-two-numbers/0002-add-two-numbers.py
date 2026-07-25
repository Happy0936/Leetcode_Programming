# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        current=dummy
        carry=0
        while l1 or l2 or carry:
            a1=l1.val if l1 else 0
            a2=l2.val if l2 else 0
            value=a1+a2+carry
            carry =value//10
            res=value%10
            current.next=ListNode(res)
            current=current.next

            if l1:
                l1=l1.next

            if l2:
                l2=l2.next


        return dummy.next


