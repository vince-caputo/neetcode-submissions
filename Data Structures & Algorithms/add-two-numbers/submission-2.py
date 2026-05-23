# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carrying = False
        while curr1.next and curr2.next:
            temp = (curr1.val + curr2.val + int(carrying))
            if temp>= 10:
                carrying = True
            else:
                carrying = False
            curr1.val = temp % 10
            curr1 = curr1.next
            curr2 = curr2.next
        
        temp = (curr1.val + curr2.val + int(carrying))
        if temp >= 10:
            carrying = True
        else:
            carrying = False
        curr1.val = temp % 10
        if curr2.next:
            curr1.next = curr2.next

        while curr1.next:
            if carrying:
                if curr1.next.val == 9:
                    curr1.next.val = 0
                else:
                    carrying = False
                    curr1.next.val += 1
            curr1 = curr1.next

        if carrying:
            curr1.next = ListNode(1)
        return l1
        













