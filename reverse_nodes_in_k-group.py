# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverse(self, start, end):
        if start is end:
            return
        node = start.next
        while node is not None:
            saved_next = node.next
            node.next = start
            start = node
            node = saved_next
            if start is end:
                return

    def reverseKGroup(self, head, k):
        if k <= 1 or head is None:
            return head
        start = node = head
        saved_prev = None
        pos = 1
        while node.next is not None:
            node = node.next
            pos += 1
            if pos == k:
                saved_next = node.next
                if saved_prev is None:
                    head = node
                else: saved_prev.next = node
                saved_prev = start
                self.reverse(start,node)
                start.next = saved_next
                node = start = start.next
                if node is None: break
                pos = 1
        return head

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def gen_list(l):
    if len(l) == 0:
        return None
    head = ListNode(l[0])
    node = head
    for n in l[1:]:
        new_node = ListNode(n)
        node.next = new_node
        node = node.next
    return head

def print_list(node):
    res = []
    while node is not None:
        res.append(node.val)
        node = node.next
    return res

if __name__ == '__main__':
    l = Solution().reverseKGroup(gen_list([1,2,3]),3)
    print print_list(l)