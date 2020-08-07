"""
blockchain implementation using linked lists
"""
import hashlib
import datetime

######################
class DoubleNode:
    def __init__(self, data, previous_hash=None):
        self.block = Block(datetime.datetime.utcnow(), data, previous_hash)
        self.next = None
        self.prev = None

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

    def append(self, data):
        if data:
            if self.head is None:
                self.head = DoubleNode(data)
                self.tail = self.head
            else:
                self.tail.next = DoubleNode(data, self.tail.block.hash)
                self.tail.next.prev = self.tail
                self.tail = self.tail.next
        else:
            print("ERROR: block is empty")

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
    ####### test #########
    testblock = Blockchain()
    print('------------- adding blocks ----------')
    testblock.append("b-1")
    testblock.append("b-2")
    testblock.append("b-3")

    print(testblock)
    print ('------ DONE ---------')