head = [1,2,6,3,4,5,6]
val = 6


for i in range(len(head)):
    if head[i] == val:
        head.pop(i)
        break


# Remove Linked List Elements

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        while head.val == val:
            head = head.next
            if head is None:
                return None
        cur = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head







        