from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        while True:
            probe = group_prev
            for i in range(k):
                probe = probe.next
                if not probe:
                    return dummy.next
            group_next = probe.next
            group_start = group_prev.next
            prev = group_next
            cur = group_start
            while cur != group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            group_prev.next = probe
            group_prev = group_start

