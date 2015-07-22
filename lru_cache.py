import re

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.size = capacity
        self.DATA_STORE = {}
        self.pos = []
    # @return an integer

    def __sliding_window(self, size, last, lastw):
        if size <= 4: return (0,size-1)
        l = pow(lastw,2)
        if last-1 < l: return (0, last-1)
        else: return (last-1-l, last-1)

    def __place_to_end(self, key):
        last = len(self.pos)-1
        lastw = 2
        i = -1
        while last >= 0:
            try:
                w = self.__sliding_window(len(self.pos), last, lastw)
                i = self.pos.index(key, w[0], w[1])
            except ValueError:
                if last == 0: break
                last = w[0]
                lastw = w[1]-w[0]
            else:
                break
        if i > -1:
            self.pos.pop(i)
            self.pos.append(key)

    def __competitor_joined(self, key, value):
        self.pos.append(key)
        if len(self.pos) > self.size:
            poor_man = self.pos.pop(0)
            self.DATA_STORE.pop(poor_man)
        self.DATA_STORE[key] = value

    def get(self, key):
        ret = self.DATA_STORE.get(key)
        if ret is not None:
            self.__place_to_end(key)
            return ret
        else: return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.DATA_STORE.has_key(key):
            self.DATA_STORE[key] = value
            self.__place_to_end(key)
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