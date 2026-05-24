from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0)
        local = dummy
        fast = dummy
        local.next = head
        fast.next = head
        while fast and fast.next:
            local = local.next
            fast = fast.next.next
            if (local == fast):
                return True
            
        return False
