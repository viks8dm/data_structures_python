## Data Compression - Huffman Coding

Based on basic Huffman algorithm, following steps are performed:

* count frequency of each character
* buld Huffman tree usnig priority-queue, using frequency as priority
* encode tree elements with 0 for left and 1 for right child and save encoding for each character in a dictionary
* decode following reverse encoding and comparing with characters saved in the encoded dictionary in previous step

#### Efficiency

Time efficiency is O(n-logn)

* frequency counting is O(n)
* building priority tree is O(n)
* code generation is a recursive call on half the number of elements in each recursive call, hence it is O(n-logn)
* decoding the tree is same as encoding and hence O(n-logn)
* getting the string from decoded tree is O(n)

Space efficiency is O(n-logn) in the worst case due to recursive implementation



