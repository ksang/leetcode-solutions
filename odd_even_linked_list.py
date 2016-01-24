class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        i = 3
        n1 = head
        h2 = n2 = head.next
        if n2 is not None:
            node = n2.next
        else:
            return head
        while node is not None:
            if i % 2 == 0:
                n2.next = node
                n2 = n2.next
            else:
                n1.next = node
                n1 = n1.next
            node = node.next
            i += 1
        n1.next = h2
        n2.next = None
        return head

def create_list(l):
    h = ListNode(l[0])
    node = h
    for v in l[1:]:
        node.next = ListNode(v)
        node = node.next
    return h

def print_list(n):
    while n is not None:
        print n.val
        n = n.next

if __name__ == '__main__':
    node = create_list([1,2,3])
    print_list(Solution().oddEvenList(node))
