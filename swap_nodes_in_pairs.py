# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head is None: return None
        if head.next is None: return head
        node = head
        head = head.next
        while node.next is not None:
            saved_first = node
            saved_third = node.next.next
            node.next.next = node
            node.next = saved_third
            node = saved_third
            if node is None: break
            if node.next is not None:
                saved_first.next = node.next
        return head