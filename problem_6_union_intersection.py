"""
fill out the union and intersection functions

given two linked lists and return a linked list that 
is composed of either the union or intersection, respectively.
"""
############################
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

############################
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

############################
def union(llist_1, llist_2):
    # union of two lists
    if llist_1.size()==0:
        return llist_2
    
    if llist_2.size()==0:
        return llist_1
    
    elem_set = set()
    n1 = llist_1.head
    n2 = llist_2.head
    while (n1 or n2):
        if n1:
            elem_set.add(n1.value)
            n1 = n1.next
        if n2:
            elem_set.add(n2.value)
            n2 = n2.next

    new_list = LinkedList()
    for elem in elem_set:
        new_list.append(elem)

    return new_list

############################
def intersection(llist_1, llist_2):
    # union of two lists
    if (llist_1.size()==0) or (llist_2.size()==0):
        # print("WARNING: intersection of None type list with other list is not defined")
        return LinkedList()
    
    new_list = LinkedList()
    elem_set = set()
    n1 = llist_1.head
    while n1:
        elem_set.add(n1.value)
        n1 = n1.next
    
    n2 = llist_2.head
    while n2:
        if (elem_set) and (n2.value in elem_set):
            elem_set.remove(n2.value)
            new_list.append(n2.value)
        n2 = n2.next

    return new_list

############################
def tests_given(testcase):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    if testcase==1:
        element_1 = [3,2,4,35,6,65,6,4,3,21]
        element_2 = [6,32,4,9,6,1,11,21,1]
        union_list = [32,65,2,35,4,6,1,9,11,3,21]
        intersect_list = [6,4,21]
    
    elif testcase==2:
        element_1 = [3,2,4,35,6,65,6,4,3,23]
        element_2 = [1,7,8,9,11,21,1]
        union_list = [1,2,3,4,6,7,8,9,11,35,21,23,65]
        intersect_list = []
    
    elif testcase == 3: # all empty
        element_1 = []
        element_2 = []
        union_list = []
        intersect_list = []

    elif testcase == 4: # all same
        element_1 = [1,2,3,4,5,6,7]
        element_2 = [1,2,3,4,5,6,7]
        union_list = [1,2,3,4,5,6,7]
        intersect_list = [1,2,3,4,5,6,7]

    elif testcase == 5: # one empty
        element_1 = [1,2,3,4,5,6,7,8,9]
        element_2 = []
        union_list = [1,2,3,4,5,6,7,8,9]
        intersect_list = []

    # union check
    for i in element_1:
        linked_list_1.append(i)
    for i in element_2:
        linked_list_2.append(i)

    u_list = union(linked_list_1,linked_list_2)
    if u_list.size() != 0:
        print(u_list)
        llist_u = LinkedList()
        for u in union_list:    llist_u.append(u)
        print("Pass (Union)" if (str(union(linked_list_1,linked_list_2))==str(llist_u)) else "FAIL")
    else:
        print("UNION returned empty list")
        if len(union_list)==0:
            print("Pass (union)")

    # intersection check
    int_list = intersection(linked_list_1,linked_list_2)
    if int_list.size() != 0:
        print(int_list)
        llist_i = LinkedList()
        for i in intersect_list:    llist_i.append(i)
        print("Pass (Intersection)" if (str(int_list)==str(llist_i)) else "FAIL")
    else:
        print("INTERSECTION returned empty list")
        if len(intersect_list)==0:
            print("Pass (intersection)")

################################
if __name__ == "__main__":
    print("\n------ test 1 --------")
    tests_given(1)
    print("\n------ test 2 --------")
    tests_given(2)
    print("\n------ test 3 --------")
    tests_given(3)
    print("\n------ test 4 --------")
    tests_given(4)
    print("\n------ test 5 --------")
    tests_given(5)

    print("\n")