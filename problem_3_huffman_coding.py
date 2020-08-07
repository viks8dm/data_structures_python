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
    if (data is None) or (data=='') or (not bool(data)):
        # print("ERROR: no data provided for encoding")
        return '', None
    
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
def message_info(test_string):
    """
    function to get information for a message type to develop test cases
    """
    print ("The size of the data is: {}\n".format(sys.getsizeof(test_string)))
    print ("The content of the data is: {}\n".format(test_string))

    encoded_data, tree = huffman_encoding(test_string)

    if len(encoded_data)>0:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    else:
        print ("The size of the encoded data is: 0\n")
        return
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

#######################
def test(test_string, test_string_size, test_encoded_data, test_encode_size):
    encoded_data, tree = huffman_encoding(test_string)

    print("Pass \t (string-size)" if sys.getsizeof(test_string)==test_string_size else "FAIL (string-size)")
    print("Pass \t (encoding)" if encoded_data==test_encoded_data else "FAIL (encoding)")

    if (test_encode_size == 0):
        print('--> not checking other params since encoded data size is 0')
        return
    
    print("Pass \t (encoding-size)" if sys.getsizeof(int(encoded_data, base=2))==test_encode_size else "FAIL (encoding-size)")
    
    decoded_data = huffman_decoding(encoded_data, tree)

    print("Pass \t (decoded-size)" if sys.getsizeof(decoded_data)==test_string_size else "FAIL (decoded-size)")
    print("Pass \t (decoded-string)" if decoded_data==test_string else "FAIL (decoded-string)")
    return

#######################
if __name__ == "__main__":
    get_tests = True

    # get_message_info = False
    # if get_message_info:
    #     # get message info
    #     print('-----------------  getting information --------')
    #     test_string = 'done with data structures for now -:)'
    #     codes = {}
    #     message_info(test_string)
    #     get_tests = False

    if get_tests:
        #-----------------------
        # test - 1-4 : iinvalid cases
        print('=======================================')
        print("testing: invalid cases")
        test_string = [None, '', False, {}]
        test_string_size = [16, 37, 24, 280]
        test_encoded_data = ['','','','']
        test_encode_size = [0, 0, 0, 0]

        for i in range(4):
            codes = {}
            print('----------- test - ' + str(i+1) + '--------------')
            test(test_string[i], test_string_size[i], test_encoded_data[i], test_encode_size[i])

        # -----------------------
        # test 5-9: repetitive and random cases
        print('=======================================')
        print("testing: repetitive and random cases")
        test_string = ['000000000', '1111111111', 'vvv', 'hello world',
                    'done with data structures for now -:)' ]
        test_string_size = [46, 47, 40, 48, 74]
        test_encode_size = [24, 24, 24, 24, 44]
        test_encoded_data = ['000000000', '0000000000', '000', '00111111010110111001111001010000',
                    '001110110100001011001111001000010011110001111111000111111100101000111001101000000001101110001001011101000110111110110010010110111110101001111010101']

        for i in range(5):
            codes = {}
            print('----------- test - ' + str(i+5) + '--------------')
            test(test_string[i], test_string_size[i], test_encoded_data[i], test_encode_size[i])

        # -----------------------
        # test -10
        print('=======================================')
        print("-------------- test - 10: default provided case -------------")
        codes = {}
        test_string = "The bird is the word"
        test_string_size = 57
        test_encode_size = 36
        test_encoded_data = '1001001111011001100000101111110000100011010110011110110101001110101111'
        test(test_string, test_string_size, test_encoded_data, test_encode_size)

    
