## Least Recently Used Cache

Since all operations have to be O(1) and the only operations needed for this implementation are related to accessing data and putting data in place, I have used a double-linked-list for cache dictionary.

#### Efficiency

Time omplexity for all operations is O(1) as these are simple assignment operations

Space complexity is O(n) in the worst case, as a dictionary is used to store all recently used elements.