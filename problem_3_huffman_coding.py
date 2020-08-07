"""
implement logic for encoding and decoding via Huffman coding

Huffman encoding:
building the Huffman tree (a binary tree), and generating the encoded data

Huffman decoding:
decode the encoded data using the following steps:

Declare a blank decoded string
Pick a bit from the encoded data, traversing from left to right.
Start traversing the Huffman tree from the root.
If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
Repeat steps #2 and #3 until the encoded data is completely traversed.

"""

import sys

#######################
class Node:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

#######################
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.num_elements = 0
    
    def put(self, node):
        self.queue.append(node)
        self.num_elements += 1

    def pop_min_freq_elem(self):
        min_freq_node = self.queue[0]
        min_idx = 0

        for i in range(1, self.num_elements):
            if min_freq_node.freq > self.queue[i].freq:
                min_freq_node = self.queue[i]
                min_idx = i
        
        self.num_elements -= 1
        del self.queue[min_idx]

        return min_freq_node

    def is_empty(self):
        return (self.num_elements==0)

#######################
def generate_code(node, bit_val=""):
    encoding = {}
    if node:
        if not (node.left or node.right):
            if bit_val == "":
                encoding.update({node.char: "0"})
            else:
                encoding.update({node.char: bit_val})
        encoding.update(generate_code(node.left, bit_val+"0"))
        encoding.update(generate_code(node.right, bit_val+"1"))

    return encoding

#######################
def decode_tree(node, bit_val=""):
    decoding = {}
    if node:
        if not (node.left or node.right):
            if bit_val == "":
                decoding.update({"0": node.char})
            else:
                decoding.update({bit_val: node.char})
        decoding.update(decode_tree(node.left, bit_val+"0"))
        decoding.update(decode_tree(node.right, bit_val+"1"))

    return decoding

#######################
def huffman_encoding(data):
    if data is None or data=='':
        print("ERROR: no data provided for encoding")
        return None, None
    
    # get frequency
    for s in data:
        if s in codes:
            codes[s] += 1
        else:
            codes[s] = 1

    # build priority queue
    pr_queue = PriorityQueue()
    for ch in codes:
        node = Node(ch, codes[ch])
        pr_queue.put(node)
    
    # build tree
    while pr_queue.num_elements > 1:
        n1 = pr_queue.pop_min_freq_elem()
        n2 = pr_queue.pop_min_freq_elem()

        # create new node
        pr_queue.put(Node('', (n1.freq + n2.freq), n1, n2))

    # define tree
    huffman_tree = pr_queue.queue[0]

    # generate code
    encoding = generate_code(huffman_tree)

    huffman_code = data
    for c in encoding:
        huffman_code = huffman_code.replace(c, encoding[c])

    return huffman_code, huffman_tree

#######################
def huffman_decoding(data,tree):
    decoded_msg = decode_tree(tree)
    decoded_string = ""
    code = ""
    for c in data:
        code += c
        if code in decoded_msg:
            decoded_string += decoded_msg[code]
            code = ""

    return decoded_string

#######################
if __name__ == "__main__":
    codes = {}
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))