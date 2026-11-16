class Node:
    def __init__(self, val=0, left=None, right=None):
        self.key = 0
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {} # map key to node

        self.head = Node()
        self.tail = Node()

        self.head.right = self.tail
        self.tail.left = self.head

        self.capacity = capacity

    def get(self, key: int) -> int:

        if key not in self.keys:
            return -1

        # we want to move the key to the front of the linked list, because it is used

        # remove node from where it is in the list, connect its 2 neighbors
        node = self.keys[key]
        left_node = node.left
        right_node = node.right
        left_node.right = right_node
        right_node.left = left_node
        
        # move the node to the beginning of the list, beside head
        curr_top = self.head.right
        self.head.right = node
        node.left = self.head
        node.right = curr_top
        curr_top.left = node

        return node.val

    def put(self, key: int, value: int) -> None:
        
        # if the key exists, we just want to update the value and move it to the front
        if key in self.keys:
            self.keys[key].val = value
            self.get(key)
            return
        
        # check if we are at capacity, we will evict the LRU if so
        if len(self.keys) == self.capacity:
            lru_node = self.tail.left
            lru_node_left = lru_node.left
            lru_node_left.right = self.tail
            self.tail.left = lru_node_left
            lru_node.left = None
            lru_node.right = None
            del self.keys[lru_node.key]
        
        # add key to the beginning
        new_node = Node()
        new_node.key = key
        new_node.val = value
        
        curr_top_node = self.head.right
        self.head.right = new_node
        new_node.left = self.head
        new_node.right = curr_top_node
        curr_top_node.left = new_node

        self.keys[key] = new_node
        return 


