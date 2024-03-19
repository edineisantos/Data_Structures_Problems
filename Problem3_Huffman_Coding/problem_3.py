import heapq
import sys

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # For priority queue to compare nodes
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(data):
    if data is None:
        raise ValueError("Cannot encode NoneType data")

    if not data:
        return "", None
    
    # Calculate frequency of each character
    freq = {}
    for char in data:
        if not char in freq:
            freq[char] = 0
        freq[char] += 1

    # Create a priority queue (min-heap) from frequencies
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    # Build the Huffman tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    # The final element of the heap is the root of the Huffman tree
    tree = heap[0]

    # Generate Huffman codes
    codes = {}
    def generate_codes(node, path):
        if node is not None:
            if node.char is not None:
                codes[node.char] = path
            generate_codes(node.left, path + "0")
            generate_codes(node.right, path + "1")

    generate_codes(tree, "")

    # Encode the data
    encoded_data = ''.join([codes[char] for char in data])
    
    return encoded_data, tree

def huffman_decoding(data, tree):
    if not data or tree is None:
        return ""
    
    decoded_data = ""
    node = tree
    for bit in data:
        node = node.left if bit == "0" else node.right
        if node.char is not None:  # Leaf node
            decoded_data += node.char
            node = tree  # Reset for next character
    
    return decoded_data

if __name__ == "__main__":
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    # Test Case 1: Encode and Decode an Empty String
    print("Test Case 1: Encode and Decode an Empty String")
    empty_sentence = ""
    encoded_data, tree = huffman_encoding(empty_sentence)
    if encoded_data:
        print("Encoded data:", encoded_data)
    else:
        print("Encoded data is empty.")
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded data:", decoded_data)
    if decoded_data == empty_sentence:
        print("Test passed: Empty string encoded and decoded correctly.")
    else:
        print("Test failed: Decoded data does not match original.")
    print("\n")

    # Test Case 2: Encode and Decode with None Value
    print("Test Case 2: Encode and Decode with None Value")
    try:
        encoded_data, tree = huffman_encoding(None)
        print("Encoded data:", encoded_data)  # This line should not execute
        decoded_data = huffman_decoding(encoded_data, tree)  # Neither should this
        print("Decoded data:", decoded_data)  # Nor this
    except ValueError:
        print("Test passed: ValueError caught for None input.")
    except Exception as e:
        print(f"Test failed: Unexpected exception caught: {e}")
    else:
        print("Test failed: No exception caught for None input.")
    print("\n")

    # Test Case 3: Encode and Decode a Large String
    print("Test Case 3: Encode and Decode a Large String")
    large_sentence = "A" * 1000 + "B" * 1000 + "C" * 1000 + "D" * 500 + "E" * 500  # Large string
    encoded_data, tree = huffman_encoding(large_sentence)
    print(f"Encoded data length: {len(encoded_data)}")
    decoded_data = huffman_decoding(encoded_data, tree)
    if decoded_data == large_sentence:
        print("Test passed: Large string encoded and decoded correctly.")
    else:
        print("Test failed: Decoded data does not match original.")
    print("\n")






