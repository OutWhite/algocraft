from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        new_head = self.reverseList(slow.next)
        while new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True


