# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        f = 0
        first = True
        res = None
        while True:
            if l1 is None and l2 is None and f == 0:
                break
            if l1 is not None:
                n1 = l1.val
            else:
                n1 = 0
            if l2 is not None:
                n2 = l2.val
            else:
                n2 = 0
            r = n1 + n2 + f
            if r < 10:
                cr = ListNode(r)
                f = 0
            else:
                cr = ListNode(r-10)
                f = 1
            if first:
                pr = cr
                pr.next = None
                res = pr
            else:
                pr.next = cr
                pr = cr
            pr = cr
            if l1 is not None:
                    l1 = l1.next
            if l2 is not None:
                    l2 = l2.next
            first = False
        return res

