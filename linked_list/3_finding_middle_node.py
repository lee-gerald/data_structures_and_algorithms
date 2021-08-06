
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0
    
    def get_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head

        #O(N) linear running time complexity
        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node
        
        return slow_pointer.data

    # O(1)
    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    # O(N)
    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node
        
        actual_node.next_node = new_node

    def remove(self, data):
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node
        
        # if item is not in the linkedlist
        if actual_node is None:
            return
        
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node
            self.numOfNodes = self.numOfNodes - 1

    
    # O(1)
    def size_of_list(self):
        return print('size of is = ', self.numOfNodes)

    # O(N)
    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

linked_list = LinkedList()
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(7)
linked_list.insert_end(10)
linked_list.insert_start(12)
linked_list.insert_start(20)

print(linked_list.get_middle_node())

