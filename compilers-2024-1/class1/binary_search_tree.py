class Node:
    def __init__(self, data=None, left_node=None, right_node=None) -> None:
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

class BinarySearchTree:
    def __init__(self, trunk=None) -> None:
        self.trunk = trunk

    def add(self, data):
        if self.trunk is None:
            self.trunk = Node(data)
        else:
           self._add_recursive(data, self.trunk)
                    
    def _add_recursive(self, data, current_node):
        if data < current_node.data:
                if current_node.left_node is None:
                    current_node.left_node = Node(data)
                else:
                    self._add_recursive(data, current_node.left_node)
        elif data >= current_node.data:
            if current_node.right_node is None: 
                current_node.right_node = Node(data)
            else:
                self._add_recursive(data, current_node.right_node)
        else:
            raise ValueError("Duplicated value found in tree.")
    
    def remove(self, data):
        pass
    
    def contains(self, data):
        pass

    def get_min(self):
        pass

    def get_max(self):
        if self.trunk is None:
            raise ValueError("The tree is empty.")
        
        if self.trunk.right_node is None:
            return self.trunk.data
        
        actual_node = self.trunk

        while actual_node.right_node != None:
            actual_node = actual_node.right_node
        
        return actual_node.data
        

    def size(self):
        # return total nodes
        pass

    def height(self):
        # return the height of the tree
        pass    

    def print_tree(self):
        if self.trunk is None:
            print("Tree is empty")
        else:
            self._print_inorder(self.trunk)

    def _print_inorder(self, node):
        if node is not None:
            self._print_inorder(node.left_node)
            print(node.data, end=" ")
            self._print_inorder(node.right_node)

## testing 
intList = [10, 20, 5, 2, 40, 60]
bst = BinarySearchTree()

for num in intList:
    bst.add(num)

bst.print_tree()
bst.get_max()
