class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        prev, current = None, head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev


s1 = ListNode([1, 2, 3, 4, 5])
print(Solution)
