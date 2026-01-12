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


head = ListNode(1, (ListNode(2, ListNode(3))))
s1 = Solution()
reversed_head = s1.reverseList(head)
output = []
current = reversed_head
while current:
    output.append(current.val)
    current = current.next
print(output)
