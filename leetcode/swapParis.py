# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(-1)
        pre.next = head
        temp = pre
        while temp.next and temp.next.next:
            a, b = temp.next, temp.next.next
            temp.next = b
            a.next = b.next
            b.next = a
            temp = temp.next.next
        return pre.next
