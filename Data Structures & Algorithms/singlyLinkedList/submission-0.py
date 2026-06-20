class ListNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        curr = self.head
        at = 0
        while at < index:
            curr = curr.next
            at += 1

        return curr.val

    def insertHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.head.next = self.head
            self.head.prev = self.head
            self.length = 1
            return


        new_head = ListNode(val, self.head.prev, self.head)
        self.head.prev.next = new_head
        self.head.prev = new_head
        self.head = new_head
        self.length += 1
            
        

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.insertHead(val)
            return

        new_tail = ListNode(val, self.head.prev, self.head)
        self.head.prev.next = new_tail
        self.head.prev = new_tail
        self.length += 1
        

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False

        if self.head is self.head.next:
            self.head = None
            self.length = 0
            return True

        if index == 0:
            self.head = self.head.next
            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head
            self.length -= 1
            return True

        curr = self.head
        at = 0
        while at < index:
            curr = curr.next
            at += 1

        curr.next.prev = curr.prev
        curr.prev.next = curr.next

        self.length -= 1
        return True
        

    def getValues(self) -> List[int]:

        if not self.head:
            return []

        res = [self.head.val]
        curr = self.head.next

        while curr is not self.head:
            res.append(curr.val)
            curr = curr.next

        return res
        
