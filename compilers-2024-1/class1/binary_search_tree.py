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
        if self.trunk is None:
            raise ValueError("Tree is empty.")

        self.trunk = self._remove_recursive(self.trunk, data)
        
    def _remove_recursive(self, current_node, data):
        if current_node is None:
            return current_node

        if data < current_node.data:
            current_node.left_node = self._remove_recursive(current_node.left_node, data)
        elif data > current_node.data:
            current_node.right_node = self._remove_recursive(current_node.right_node, data)
        else:
            if current_node.left_node is None and current_node.right_node is None:
                current_node = None
            elif current_node.left_node is None:
                current_node = current_node.right_node
            elif current_node.right_node is None:
                current_node = current_node.left_node
            else:
                successor_node = self._find_min(current_node.right_node)
                current_node.data = successor_node.data
                current_node.right_node = self._remove_recursive(current_node.right_node, successor_node.data)

        return current_node

    def _find_min(self, node):
        while node.left_node is not None:
            node = node.left_node
        return node
    
    def contains(self, data) -> bool:
        if self.trunk is not None and self.trunk.data is data: return True
        
        current_node = self.trunk

        #to-do: make this function recursive
        while current_node.left_node is not None or current_node.right_node is not None and current_node.data is not data:            
            if data > current_node.data:
                current_node = current_node.right_node
            else:
                current_node = current_node.left_node
        
        return current_node.data is data

    def get_min(self) -> int:
        if self.trunk is None:
            raise ValueError("The tree is empty.")
        
        if self.trunk.left_node is None:
            return self.trunk.data
    
        actual_node = self.trunk

        while actual_node.left_node is not None:
            actual_node = actual_node.left_node
        
        return actual_node.data

    def get_max(self) -> int:
        if self.trunk is None:
            raise ValueError("The tree is empty.")
        
        if self.trunk.right_node is None:
            return self.trunk.data
        
        actual_node = self.trunk

        while actual_node.right_node is not None:
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
numbers_to_add = [10, 20, 5, 2, 40, 60]
bst = BinarySearchTree()

for number in numbers_to_add:
    bst.add(number)

bst.print_tree()