"""
This LRU Cache implementation utilizes a doubly-linked list with two sentinel
nodes, head and tail, to manage cache entries efficiently based on usage. The
list includes:

- Head Node: A sentinel marking the list's start, leading to the LRU cache
  entry right after it.
- Cache Nodes: Each holds a key-value pair, dynamically managed (added, 
  removed, moved) based on cache operations. Their order reflects usage 
  history, with MRU items near the tail and LRU items near the head.
- Tail Node: A sentinel at the list's end, simplifying the addition of new MRU 
  items before it.

Head and tail sentinel nodes eliminate null checks for list modifications, 
enabling constant-time operations for adding MRU items, removing LRU items, 
and maintaining efficient LRU cache eviction policy. With full capacity, the 
list totals 7 nodes: 1 head, 5 cache nodes, and 1 tail:
Head <-> Cache1 <-> Cache2 <-> Cache3 <-> Cache4 <-> Cache5 <-> Tail
"""


# Create a node of a doubly-linked list
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# Create a LRU Cache using a doubly-linked list and a dictionary
class LRU_Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        # This will store the keys and their respective node in the doubly-linked list
        # Initialize the doubly-linked list with dummy head and tail nodes to 
        # avoid edge case checks
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            # Move the node to the end to mark it as recently used
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def set(self, key, value):
        if key in self.cache:
            # Remove the old node and add the new one to the end
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # Remove the least recently used item from the head
            node_to_remove = self.head.next
            self._remove(node_to_remove)
            del self.cache[node_to_remove.key]

    def _remove(self, node):
        # Remove an existing node from the doubly-linked list
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node):
        # Always add the new node right before the tail
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

# Example usage
our_cache = LRU_Cache(5)

# Basic example usage
print("Basic example usage:")
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached its capacity and 3 was the least recently used entry
print("\n")

# Test Case 1: Attempting to get and set null values
# Expected behavior: The cache should handle 'None' keys and values gracefully,
# either by ignoring them or by treating them as valid entries, based on the 
# implementation choice.

print("Test Case 1: Attempting to get and set null values")

# Setting a null key with a non-null value (Implementation dependent)
our_cache.set(None, 10)
print(our_cache.get(None))  # Expected: 10 if null keys are allowed, -1 otherwise

# Setting a null value
our_cache.set(1, None)
print(our_cache.get(1))  # Expected: None if null values are allowed, -1 otherwise

print("\n")

# Test Case 2: Working with empty strings or collections as keys/values
# Expected behavior: The cache treats empty strings and collections as valid keys/values.

print("Test Case 2: Working with empty strings or collections as keys/values")

# Setting an empty string as a key
our_cache.set("", "empty key")
print(our_cache.get(""))  # Expected: "empty key"

# Setting an empty string as a value
our_cache.set("empty value", "")
print(our_cache.get("empty value"))  # Expected: ""

# Setting an empty list as a value
our_cache.set("empty list", [])
print(our_cache.get("empty list"))  # Expected: []

print("\n")

# Test Case 3: Inserting very large values as keys or values
# Expected behavior: The cache should be able to handle very large integers or
# strings as keys/values without performance degradation.

print("Test Case 3: Inserting very large values as keys or values")

# Setting a very large number as a value
our_cache.set("large value", 10**18)
print(our_cache.get("large value"))  # Expected: 10**18

# Setting a very large string as a value
large_string = "a" * 10**6  # 1 million 'a's
our_cache.set("large string", large_string)
print(our_cache.get("large string") == large_string)  # Expected: True

# Using a very large number as a key (implementation and language-dependent)
our_cache.set(10**18, "large key")
print(our_cache.get(10**18))  # Expected: "large key" if large ints are allowed as keys


