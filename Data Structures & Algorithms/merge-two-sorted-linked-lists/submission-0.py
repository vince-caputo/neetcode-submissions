# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        curr1 = list1
        curr2 = list2
        switched = False
        if list1.val > list2.val:
            switched = True
            curr1 = list2
            curr2 = list1

        while curr1.next and curr2:
            if curr2.val <= curr1.next.val:
                curr1.next, curr2 = curr2, curr1.next
                curr1 = curr1.next
            else:
                curr1 = curr1.next
        curr1.next = curr2

        if switched:
            return list2
        return list1





            