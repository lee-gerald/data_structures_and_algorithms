
class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def reverse(self):
        current_node = self.head
        next_node = None
        previous_node = None

        while current_node is not None:
            next_node = current_node.nextNode
            current_node.nextNode = previous_node # flip the reference backwards
            previous_node = current_node
            current_node = next_node
        
        self.head = previous_node

    # O(1)
    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    # O(N)
    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode
        
        actual_node.nextNode = new_node

    def remove(self, data):
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.nextNode
        
        # if item is not in the linkedlist
        if actual_node is None:
            return
        
        if previous_node is None:
            self.head = actual_node.nextNode
        else:
            previous_node.nextNode = actual_node.nextNode
            self.numOfNodes = self.numOfNodes - 1

    
    # O(1)
    def size_of_list(self):
        return print('size of is = ', self.numOfNodes)

    # O(N)
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode


linked_list = LinkedList()
linked_list.insert_start(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.traverse()

print("---reverse---")
linked_list.reverse()
linked_list.traverse()