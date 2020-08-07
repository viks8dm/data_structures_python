"""
blockchain implementation using linked lists
"""
import hashlib
import datetime

######################
class Node:
    def __init__(self, data, previous_hash=None):
        self.block = Block(datetime.datetime.utcnow(), data, previous_hash)
        self.next = None
        # self.prev = None

######################
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        # hash_str = "We are going to encode this string of data!".encode('utf-8')
        hash_str = str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        text = "\nTimestamp: " + str(self.timestamp) + "\n" \
            + "Data: " + str(self.data) + "\n"  \
            + "Block-hash: " + str(self.hash) + "\n"  \
            + "Previous-hash: " + str(self.previous_hash) + "\n"

        return text

######################
class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data=None):
        if data is None:
            print('block provided is empty: nothing to append')
            return

        if data:
            if self.head is None:
                self.head = Node(data)
                self.tail = self.head
            else:
                self.tail.next = Node(data, self.tail.block.hash)
                self.tail = self.tail.next

        return
   
    def __str__(self):
        if self.head is None:
            return "Block chain is empty"
        
        node = self.head
        output = ""
        while node:
            output += str(node.block)
            node = node.next
        return output

######################
if __name__=="__main__":
    # test -1 : empty blockchain
    print('================================================')
    print('------ test - 1: empty blockchain case')
    b1 = Blockchain()
    print(b1)   # OUTPUT: Block chain is empty

    # test - 2: empty appends
    print('================================================')
    print('----- test - 2: empty appends, reduced chain size')
    b1.append() # OUTPUT: block provided is empty: nothing to append
    b1.append()   # OUTPUT: block provided is empty: nothing to append
    b1.append('new-b')
    b1.append()   # OUTPUT: block provided is empty: nothing to append
    print(b1)   # prints just one block for "new-b"

    #-------- test - 3: set of valid values printed in sequence
    print('================================================')
    print('---------- test - 3: print all or specified blocks in the blockchain')
    t1 = Blockchain()
    t1.append("b-1")
    t1.append("b-2")
    t1.append("b-3")
    print('-- print all ')
    print(t1)

    print('-- print specific')
    print(t1.head.block.previous_hash)  # OUTPUT: None
    print(t1.head.block.timestamp)  # OUTPUT: timestamp value for 1st element
    print(t1.head.block.hash)  # OUTPUT: hash value for 1st element
    print(t1.head.next.block.hash)  # OUTPUT: hash value for 2nd element
