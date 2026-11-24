from collections import defaultdict , OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.keyfreq = {}
        self.freq = defaultdict(OrderedDict)
        self.minfreq = 0
    def increasefreq(self,key):
        oldfreq = self.keyfreq[key]
        del self.freq[oldfreq][key]
        if not self.freq[oldfreq]:
            del self.freq[oldfreq]
            if self.minfreq == oldfreq :
                self.minfreq +=1
        newfreq = oldfreq + 1
        self.keyfreq[key] = newfreq
        self.freq[newfreq][key] = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.increasefreq(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache[key] = value
            self.increasefreq(key)
            return 
        if len(self.cache) == self.capacity:
            lru , _ = self.freq[self.minfreq].popitem(last = False)
            del self.cache[lru]
            del self.keyfreq[lru]
            if not self.freq[self.minfreq]:
                del self.freq[self.minfreq]
        self.cache[key] = value
        self.keyfreq[key] = 1
        self.freq[1][key] = None
        self.minfreq = 1
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)