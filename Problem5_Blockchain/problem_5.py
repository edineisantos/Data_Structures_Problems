import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        # Ensure data_str is bytes. Encode an empty string if data is None.
        data_bytes = ("" if self.data is None else self.data).encode('utf-8')
        # Ensure timestamp and previous_hash are also encoded as bytes
        timestamp_bytes = self.timestamp.encode('utf-8')
        previous_hash_bytes = self.previous_hash.encode('utf-8')
        # Concatenate all bytes components
        hash_components = data_bytes + timestamp_bytes + previous_hash_bytes
        sha.update(hash_components)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.tail = None  # Reference to the last block in the chain
        self.blocks = {}  # Maps hashes to blocks for reverse lookup

    def append(self, data):
        """Appends a new block with the given data to the chain."""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        previous_hash = self.tail.hash if self.tail else '0'
        new_block = Block(timestamp, data, previous_hash)
        
        # Store the block in the hash table and update the tail reference
        self.blocks[new_block.hash] = new_block
        self.tail = new_block

    def print_chain(self):
        """Prints the blockchain from the latest to the genesis block using the hashes."""
        current_hash = self.tail.hash if self.tail else None
        while current_hash in self.blocks:
            current_block = self.blocks[current_hash]
            print(
                f"Timestamp: {current_block.timestamp}\n"
                f"Data: {current_block.data}\n"
                f"Prev Hash: {current_block.previous_hash}\n"
                f"Hash: {current_block.hash}\n"
            )
            current_hash = current_block.previous_hash


# Test Case 1: Creation of 3 Blocks
def test_three_blocks():
    print("Test Case 1: Creation of 3 Blocks")
    # Initialize the blockchain
    blockchain = Blockchain()
    # Append three blocks with distinct data
    blockchain.append("Genesis Block")
    blockchain.append("Second Block")
    blockchain.append("Third Block")
    # Print the blockchain to verify the three blocks are appended correctly
    blockchain.print_chain()
    print("\n")

test_three_blocks()

# Test Case 2: Append Block with Null Value
def test_null_value_block():
    print("Test Case 2: Append Block with Null Value")
    # Initialize the blockchain
    blockchain = Blockchain()
    # Attempt to append a block with null data
    blockchain.append(None)
    # Print the blockchain to see how it handles the null data
    blockchain.print_chain()
    print("\n")

test_null_value_block()

# Test Case 3: Append Block with Empty Value
def test_empty_value_block():
    print("Test Case 3: Append Block with Empty Value")
    # Initialize the blockchain
    blockchain = Blockchain()
    # Append a block with an empty string as data
    blockchain.append("")
    # Print the blockchain to verify the block with empty data is appended correctly
    blockchain.print_chain()
    print("\n")

test_empty_value_block()


