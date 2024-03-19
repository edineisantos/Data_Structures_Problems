class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    union_set = set()
    result_list = LinkedList()

    # If both inputs are None, return an empty list
    if llist_1 is None and llist_2 is None:
        return result_list

    # If one of the lists is None, work with the non-None list
    if llist_1 is None:
        llist_1 = llist_2
    elif llist_2 is None:
        pass  # llist_1 remains unchanged and used for the operation

    # Add elements from llist_1 to the set
    current = llist_1.head
    while current:
        union_set.add(current.value)
        current = current.next

    # If llist_2 is not None, add its elements to the set
    if llist_2 is not None:
        current = llist_2.head
        while current:
            union_set.add(current.value)
            current = current.next

    # Append all unique values from the set to the result list
    for value in union_set:
        result_list.append(value)

    return result_list


def intersection(llist_1, llist_2):
    set_1 = set()
    intersection_set = set()
    result_list = LinkedList()

    result_list = LinkedList()
    if llist_1 is None or llist_2 is None:
        return result_list  # Return an empty list if either input is None

    current = llist_1.head
    while current:
        set_1.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        if current.value in set_1:
            intersection_set.add(current.value)
        current = current.next

    for value in intersection_set:
        result_list.append(value)

    return result_list


print("Test Case 1 - Linked List with and without common elements\n")
## Test case 1a - There are common elements in both linked lists
print("Test Case 1a")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
print("Element 1: ", element_1)
element_2 = [6,32,4,9,6,1,11,21,1]
print("Element 2: ", element_2)

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Union: ")
print (union(linked_list_1,linked_list_2))
print("Intersection: ")
print (intersection(linked_list_1,linked_list_2))
print("\n")

## Test case 1b - There are no common elements in both linked lists
print("Test Case 1b")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
print("Element 1: ", element_1)
element_2 = [1,7,8,9,11,21,1]
print("Element 2: ", element_2)

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Union: ")
print (union(linked_list_3,linked_list_4))
print("Intersection: ")
print (intersection(linked_list_3,linked_list_4))

# Test Case 2 - Linked Lists with Null and Valid Inputs

print("Test Case 2a - Both Linked Lists with Null Value\n")
# Test with both inputs as None
try:
    print("Union with both None: ")
    print(union(None, None))  # Expected to return an empty list
    print("Intersection with both None: ")
    print(intersection(None, None))  # Expected to return an empty list
except Exception as e:
    print("An unexpected error occurred:", str(e))
print("\n")

print("Test Case 2b - One Linked List with Null Value, the other is valid\n")
# Setup for a valid linked list
linked_list_valid = LinkedList()
element_valid = [1, 2, 3, 4, 5]
print("Valid LinkedList elements: ", element_valid)
for i in element_valid:
    linked_list_valid.append(i)

# Test with one None and one valid input for Union and Intersection
try:
    print("Union with one None and one valid input: ")
    print(union(None, linked_list_valid))  # Expected to return the valid input list
    print("Union with valid input and None: ")
    print(union(linked_list_valid, None))  # Expected to behave the same as above
    print("Intersection with one None and one valid input: ")
    print(intersection(None, linked_list_valid))  # Expected to return an empty list
    print("Intersection with valid input and None: ")
    print(intersection(linked_list_valid, None))  # Expected to return an empty list
except Exception as e:
    print("An unexpected error occurred:", str(e))
print("\n")


# Test Case 3 - Linked Lists with Empty Value
print("Test Case 3 - Linked Lists with Empty Value\n")
# Initializing two empty linked lists
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
print("Union: ")
print(union(linked_list_5, linked_list_6))
print("Intersection: ")
print(intersection(linked_list_5, linked_list_6))
print("\n")
