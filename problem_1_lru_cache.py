"""
Design a data strcuture for least recently used (LRU) cache, 
to remove the least recently used entry from cache memory when
it reaches limit
- add get() & set() operations
- place upper bound on cache size (assume 5 for example)
- set()
    - used to insert an element
    - if cache is full and new entry is to be added, 
        remove old element and then insert
- get()
    - in case of cache-hit, return value of entry found & rearrange
    - in case of cache miss, return -1

all operations have to be O(1)
"""
##################################
class DoubleNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

##################################
class LRU_Cache(object):
    #--------
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = dict()

    #--------
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if (self.capacity == 0):
            # print("ERROR: [set] LRU-Cache capacity not definited")
            return -1
        
        if ((key is None) or (not bool(key)) or (value is None)):
            # print("ERROR: [set] Key or Value cannot be None")
            return -1

        if key in self.cache:
            # inesrt this occurance and remove previous
            node = self.cache[key]
            node.value = value
            if node !=self.head:
                self.remove_node(node)
                self.add_node(node)
        else:
            # add new node
            node = DoubleNode(key, value)
            self.add_node(node)
            self.cache[key] = node

        self.check_capacity()

        return

    #--------
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if ((key is None) or (not bool(key)) or (key not in self.cache)):
            # print("ERROR: [get] Key not found in cache")
            return -1

        node = self.cache[key]
        # print((node.value, self.tail.value, self.head.value))
        if (node != self.head):
            self.remove_node(node)
            self.add_node(node)
        
        return node.value

    #--------
    def remove_node(self, node):
        if (node != self.tail):
            p_node = node.prev
            n_node = node.next

            p_node.next = n_node
            n_node.prev = p_node
        else:
            self.tail = node.prev
            self.tail.next = None

        return

    #--------
    def remove_oldest_node(self):
        node = self.tail
        self.tail = node.prev
        self.tail.next = None

        del self.cache[node.key]
        return

    #--------
    def add_node(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        return

    #--------
    def check_capacity(self):
        if (self.capacity < len(self.cache)):
            self.remove_oldest_node()
        return
  
############## main ############
if __name__ == "__main__":
    # test - 1
    print("---------- test - 1: default sample provided")
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print("Pass" if our_cache.get(1)==1 else "FAIL")
    print("Pass" if our_cache.get(2)==2 else "FAIL")
    print("Pass" if our_cache.get(9)==-1 else "FAIL")
    our_cache.set(5, 5) 
    our_cache.set(6, 6)
    print("Pass" if our_cache.get(3)==-1 else "FAIL")

    # # # print nodes from recent to last used
    # print('===== cache values in order ====')
    # node = our_cache.head
    # while node:
    #     # if node.prev is not None:
    #     #     print((node.value, node.prev.value))
    #     print(node.value)
    #     node = node.next

    # test - 2
    print("---------- test - 2: zero capacity case")
    zero_chache = LRU_Cache(0)
    print("Pass" if zero_chache.set(1,1)==-1 else "FAIL")
    print("Pass" if zero_chache.set(2,2,)==-1 else "FAIL")
    print("Pass" if zero_chache.get(1)==-1 else "FAIL")

    # test - 3
    print("---------- test - 3: incorrect data types")
    data_cache = LRU_Cache(5)
    data_cache.set(1, 1)
    data_cache.set(2, 2)
    data_cache.set(3, 3)
    data_cache.set(4, 4)

    print("Pass" if data_cache.get(None)==-1 else "FAIL")
    print("Pass" if data_cache.get(False)==-1 else "FAIL")
    print("Pass" if data_cache.get('')==-1 else "FAIL")
    print("Pass" if data_cache.get(0)==-1 else "FAIL")
    print("Pass" if data_cache.set('', 1)==-1 else "FAIL")

    # test - 4
    print("---------- test - 4: random tests")
    my_cache = LRU_Cache(5)
    my_cache.set(1, 1)
    my_cache.set(2, 2)
    my_cache.set(3, 3)
    my_cache.set(4, 4)
    my_cache.set(5, 5)
    my_cache.set(6, 6)
    my_cache.set(7, 7)

    print("Pass" if my_cache.get(5)==5 else "FAIL")
    print("Pass" if my_cache.get(1)==-1 else "FAIL")
    print("Pass" if my_cache.get(-2)==-1 else "FAIL")

    my_cache.set(8, 1)
    my_cache.set(9, 9)

    print("Pass" if my_cache.get(5)==5 else "FAIL")
    print("Pass" if my_cache.get(4)==-1 else "FAIL")
    print("Pass" if my_cache.get(8)==1 else "FAIL")
