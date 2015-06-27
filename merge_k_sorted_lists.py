# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def node_cmp(self, e1, e2):
        return cmp(e1.val, e2.val)

    def bin_insert(self, cmp_list, start, end, node):
        if start > end:
            cmp_list.insert(start,node)
            return
        mid = (start+end)/2
        if cmp_list[mid].val < node.val:
            self.bin_insert(cmp_list, mid+1, end, node)
        elif cmp_list[mid].val > node.val:
            self.bin_insert(cmp_list, start, mid-1, node)
        else:
            cmp_list.insert(mid,node)
            return

    def mergeKLists(self, lists):
        if len(lists) == 0 : return None
        # initialize the candidate list using python's quick sort
        cmp_list = []
        node = head = None
        for n in lists:
            if n is not None: cmp_list.append(n)
        cmp_list.sort(self.node_cmp)
        if len(cmp_list) == 0: return None
        head = node = cmp_list[0]
        cmp_list = cmp_list[1:]
        while len(cmp_list) > 0:
            saved = node
            node = node.next
            if node is not None: 
                self.bin_insert(cmp_list, 0, len(cmp_list)-1, node)
            saved.next = node = cmp_list[0]
            cmp_list = cmp_list[1:]
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
    l = Solution().mergeKLists([gen_list([-2,-1,-1,-1]),gen_list([-5,-3])])
    print print_list(l)
    l2 = Solution().mergeKLists([gen_list([1,2,2]),gen_list([1,1,2])])
    print print_list(l2)