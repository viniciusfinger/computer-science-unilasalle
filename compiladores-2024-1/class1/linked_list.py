class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def __repr__(self):
        return "[" + str(self.head) + "]"
    
    def insert_after(self, previous_node, data):
        node = Node(data)
        node.next = previous_node.next
        previous_node.next = node

    def find(self, data):
        actual_node = self.head
        while actual_node and actual_node.data != data:
            actual_node = actual_node.next
        
        return actual_node

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            before_node = None
            actual_node = self.head

            while actual_node and actual_node.data != data:
                before_node = actual_node
                actual_node = actual_node.next
            
            if actual_node:
                before_node.next = actual_node.next
            else:
                before_node.next = None

# Testing the list:
list = LinkedList()
for i in range(8):
    list.insert_at_beginning(i)
print("List:", list)

for i in range(8, -4, -2):
    element = list.find(i)
    if element:
        print("List contains element {0}.".format(i))
    else:
        print("List doesn't contains element {0}.".format(i))