import re

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.mapping = {}
        self.head = self.tail = None

    def __insert_to_head(self, node):
        saved_head = self.head
        self.head = node
        node.prev = None
        node.next = saved_head
        saved_head.prev = node        

    def __move_to_head(self, node):
        # node is already the head
        if node.prev is None: 
            return
        # link node's neighbors
        node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            # tail was this node, moving it will cause tail change.
            self.tail = node.prev
        self.__insert_to_head(node)

    def __cut_tail(self):
        if self.tail is None:
            return
        saved_tail = self.tail
        saved_key = saved_tail.key
        self.tail = saved_tail.prev
        self.tail.next = None
        del saved_tail
        del self.mapping[saved_key]

    def __competitor_joined(self, key, value):
        node = Node(key, value)
        self.__insert_to_head(node)
        self.size += 1
        if self.size > self.capacity:
            self.__cut_tail()

    # @return an integer
    def get(self, key):
        node = self.mapping.get(key)
        if node is not None:
            self.__move_to_head(node)
            return node.value
        else: 
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.mapping.has_key(key):
            node = self.mapping(key)
            node.value = value
            self.__move_to_head(node)
        else:
            self.__competitor_joined(key, value)

# Parse the input method string
def parse(string):
    sl = string.split('),')
    res = []
    for item in sl:
        if item[0:3] == 'set':
            r = re.match('set\((\d+),(\d+)', item)
            res.append(('set',(int(r.groups(0)[0]),int(r.groups(0)[1]))))
        elif item[0:3] == 'get':
            r = re.match('get\((\d+)', item)
            res.append(('get',int(r.groups(0)[0])))
    return res

if __name__ == '__main__':

    test = 'set(2,1),set(2,2),get(2),set(1,1),set(4,1),get(2)'
    test = parse(test)
    cache = LRUCache(2)
    for method in test:
        m = getattr(cache,method[0])
        print method
        if type(method[1]) is int:
            m(method[1])
        else: m(method[1][0], method[1][1])