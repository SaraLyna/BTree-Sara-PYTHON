from Node import Node


class TreeBalanced:
    
    def __init__(self, degree):
        self.degree = degree
        self.root = None
        
        
    def search(self, key, node=None):
        if not node:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node
        elif len(node.childs) > 0:
            print(f"Descending to child {i}")
            return self.search(key, node.childs[i])
        else:
            print("Key not found")
            return None
        
    def linearize(self, node=None):
        if not node:
            node = self.root

        res = []
        i = 0

        while i < len(node.keys):
            if len(node.childs) > i:
                res.extend(self.linearize(node.childs[i]))

            res.append(node.keys[i])
            i += 1

        if len(node.childs) > i:
            res.extend(self.linearize(node.childs[i]))

        return res
    

    def is_btree(self, node):
        if node is None:
            return True

        if len(node.keys) > self.degree - 1 or len(node.keys) < (self.degree // 2) - 1:
            return False

        for i in range(len(node.childs)):
            if node.childs[i] and not self.is_btree(node.childs[i]):
                return False

        return True
    

# Adding nodes

node1 = Node(1, "A")
node2 = Node(2, "B")
node3 = Node(3, "C")
node4 = Node(4, "D")
node5 = Node(5, "E")
node6 = Node(6, "F")
node7 = Node(7, "G")


tree = TreeBalanced(degree=3)
tree.root = node4

node4.childs = [node2, node6]
node2.childs = [node1, node3]
node6.childs = [node5, node7]


# tree2 = TreeBalanced(degree=2)
# tree2.root= node7
# 
# node7.childs= [node1, node2]
# node1.childs= [node4]
# node2.childs= [node5, node6, node3]

key_to_search = 5
result_node = tree.search(key_to_search, tree.root)

if result_node is not None:
    print(f"Node with key {key_to_search} found: {result_node}")
else:
    print(f"Node with key {key_to_search} not found.")
    
print(tree.search(4, tree.root))  # Output: True
print(tree.search(8, tree.root))  # Output: False
print(tree.search(2, tree.root))  # Output: True

 
 # Checking if it's a B-tree
is_balanced = tree.is_btree(tree.root)
print(f"Is the tree balanced? {is_balanced}")

# not_balaned= tree2.is_Btree(tree2.root)
# print(f"Is the tree balanced? {not_balanced}")
# 
result1 = (tree.linearize()) == [1, 2, 3, 4, 5, 6, 7]
result2 = (tree.linearize()) == [1, 2, 3, 4, 5, 6, 7, 8]  # Fixing this line, assuming 8 is the last key
result3 = (tree.linearize()) == [1, 2, 3, 4, 5, 6, 7, 13]  # Fixing this line, assuming 13 is not present
result4 = (tree.linearize()) == [1, 2, 3, 4, 5, 6, 7]  # Fixing this line, assuming the correct key to search is 1

print(result1)
print(result2)
print(result3)
print(result4)
# 