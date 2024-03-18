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

