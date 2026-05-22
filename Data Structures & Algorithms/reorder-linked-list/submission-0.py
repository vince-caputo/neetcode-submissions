# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        curr = head
        at = 0
        while at < length // 2:
            at += 1
            curr = curr.next
        
        
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        
        curr = head
        while curr:
            curr.next, prev = prev, curr.next
            curr = curr.next
        
        curr = prev.next

        
        
        















