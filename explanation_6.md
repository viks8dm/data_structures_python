## Union and Intersection of Two Linked Lists

for this implementation python's set data-type is used to build master list for extracting union or intersection elements for the provided linked-lists. Use of set() helps in avoiding duplicate entries and hence it was selected.

For Union, elements are simply added to this master python set()

For intersection, the master set() is created using first linked-list and presence of elements from list-2 is checked. If an element in list-2 is not in master set(), then it is removed from the master set()

#### Efficiency

Time complexity 
* for Union is O(n1 + n2) where n1 and n2 are number of elements in each linked-list
* for intersection is O(n1) if n1>n2 or O(n2) if n2>n1

Space complexity for both cases is O(n1 + n2)