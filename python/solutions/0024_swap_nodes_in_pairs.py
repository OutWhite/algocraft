from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = prev.next
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            rest = b.next
            prev.next = b
            b.next = a
            a.next = rest
            prev = a
        return dummy.next