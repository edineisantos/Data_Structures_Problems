## Explanation of the Blockchain Problem Solution

### Success Criteria: Security and Integrity

#### Cryptographic Hashing
The Blockchain implementation ensures the security and integrity of data through cryptographic hashing, specifically using SHA-256. This hash function creates a unique, tamper-evident identifier for each block, incorporating the block's data, timestamp, and the hash of the preceding block. This method secures the linkage between blocks, forming an immutable blockchain.

#### Immutable Ledger
Blockchain serves as an immutable ledger, securely recording data with precise timestamps. The cryptographic hash of each block, including the previous block's hash, secures the chain against alterations. Modifying any block's data would necessitate recalculating the hashes of all subsequent blocks, a prohibitively complex task due to SHA-256's design.

### Code Design

The blockchain's design emphasizes security, data integrity, and simplicity, featuring two main components: the Block class and the Blockchain class. Together, they facilitate a secure and straightforward blockchain implementation.

- **Block Class**: Represents each entry in the blockchain, holding the data, timestamp, previous block's hash, and its own hash. The `calc_hash` function guarantees the unique and secure identification of each block.

- **Blockchain Class**: Oversees the chain of blocks, allowing for the addition of new blocks. This structure not only secures the data but also preserves the chain's order and integrity.

### Time and Space Analysis

The efficiency of a blockchain implementation can be evaluated in terms of both time and space complexity.

- **Time Complexity**: The primary operation affecting time complexity is the calculation of the SHA-256 hash for each block. Since the hashing of each block is independent of the number of blocks in the chain, the time complexity for adding a new block is O(1), assuming the hash function's execution time is constant and does not depend on the input size. However, validating the entire blockchain or recalculating hashes due to data alteration involves traversing each block, leading to a time complexity of O(n), where n is the number of blocks in the chain.

- **Space Complexity**: The space complexity of the blockchain is O(n), where n is the number of blocks. Each block consumes a fixed amount of space, primarily due to the storage of data, timestamps, and hashes. As the chain grows, the space required increases linearly with the number of blocks.

### Conclusion

This blockchain implementation demonstrates the fundamental principles of blockchain technology, such as security, data integrity, and immutability. By employing cryptographic hashing and a carefully designed class structure, it lays the foundation for more complex blockchain applications while ensuring a secure and reliable digital ledger system. The analysis of time and space complexity provides insight into the practical considerations of maintaining a blockchain, highlighting its scalability and efficiency in handling a growing number of transactions.