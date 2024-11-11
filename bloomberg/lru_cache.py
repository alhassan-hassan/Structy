class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def _add(self, node: Node): # adding right after the dummy head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            element = self.cache[key]
            self._remove(element)
            self._add(element)
            return element.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        elif len(self.cache) == self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
        
        newNode = Node(key, value)
        self._add(newNode)
        self.cache[key] = newNode


from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ordered = OrderedDict()
        
    def get(self, key: int) -> int:
        if key in self.ordered:
            self.ordered.move_to_end(key)
            return self.ordered[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.ordered:
            self.ordered.move_to_end(key)
            self.ordered[key] = value
        else:
            self.ordered[key] = value
            if len(self.ordered) > self.capacity:
                self.ordered.popitem(last = False)
        
# HEYYE
class LRUCache:

    def __init__(self, capacity: int):
        self.lru = collections.OrderedDict()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.move_to_end(key)
            return self.lru[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru.move_to_end(key)

        self.lru[key] = value
        if len(self.lru) > self.capacity:
            self.lru.popitem(last = False)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)