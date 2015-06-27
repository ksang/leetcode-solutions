# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1
        if l1.val > l2.val:
            temp = l1
            l1 = l2
            l2 = temp
        head = l1
        while l1.next is not None:
            while l2 is not None:
                if l2.val < l1.next.val:
                    l1_saved = l1.next
                    l1.next = l2
                    l2_saved = l2.next
                    l2.next = l1_saved
                    l1 = l1.next
                    l2 = l2_saved
                else:
                    break
            l1 = l1.next
        l1.next = l2
        return head



        