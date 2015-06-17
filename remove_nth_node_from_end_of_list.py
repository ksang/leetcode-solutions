# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        node = head
        nnode = node
        if node.next is None:
            return None
        for i in range(0,n):
            nnode = nnode.next
        if nnode is None:
            return head.next
        while nnode.next is not None:
            node = node.next
            nnode = nnode.next
        node.next = node.next.next
        return head


