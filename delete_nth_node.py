class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        dummy = ListNode(0, head)
        curr = tail = dummy
        steps = 0

        while curr and steps < n:
            curr = curr.next
            steps += 1
        while curr.next:
            curr = curr.next
            tail = tail.next
        tail.next = tail.next.next
        return dummy.next


l1 = ListNode(1, (ListNode(2, (ListNode(3, (ListNode(4)))))))

s1 = Solution()
a = s1.removeNthFromEnd(l1, 2)

curr = a
while curr:
    print(curr.val, end="->")
    curr = curr.next
print("None")
