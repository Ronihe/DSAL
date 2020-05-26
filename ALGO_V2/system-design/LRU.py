# design a data structure for LRU
# get(key): return value or -1
# set(key, value) Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new ite

# 涉及删除和移动操作，使用链表，链表是有序的，一直维护，近期最多使用的放于尾部，那么每次缓存达到上限的时候，删除头部即可，其余为链表的基础操作模拟即可。


# cache:A cache is just fast storage. Reading data from a cache takes less time than reading it from something else (like a hard disk).
#
# Here's the cache catch: caches are small. You can't fit everything in a cache, so you're still going to have to use larger, slower storage from time to time.
#
# If you can't fit everything in the cache, how do you decide what the cache should store?




class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.key_to_previous = {}  # key : previous node

    def push_back(self, node):
        #     add the node to the bottom and add to the self.key_to_previous
        self.key_to_previous[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        head = self.dummy.next
        del self.key_to_previous[head.key]
        self.dummy.next = head.next
        self.key_to_previous[head.next.key] = self.dummy

    def kick_to_tail(self, key):
        previous_node = self.key_to_previous[key]
        curr_node = previous_node.next
        if curr_node == self.tail:
            return

        previous_node.next = curr_node.next
        self.key_to_previous[curr_node.key] = previous_node

        curr_node.next = None
        self.push_back(curr_node)

    def get(self, key):
        if key not in self.key_to_previous:
            print("-1")
            return -1

        curr_node = self.key_to_previous[key].next
        self.kick_to_tail(key)
        print(curr_node.value)
        return curr_node.value

    def set(self, key, value):
        if key in self.key_to_previous:
            self.kick_to_tail(key)
            self.key_to_previous[key].next.value = value
            return

        new_node = LinkedNode(key=key, value=value)
        self.push_back(new_node)

        if len(self.key_to_previous) > self.capacity:
            self.pop_front()


n1 = LinkedNode(key=1, value="one")
lru = LRUCache(2)
lru.set(2, 1)
lru.set(1, 1)
lru.get(2)
lru.set(4, 1)
lru.get(1)
lru.get(2)

