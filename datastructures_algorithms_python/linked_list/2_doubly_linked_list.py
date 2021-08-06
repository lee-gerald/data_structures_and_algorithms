class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class Doubly_Linked_List():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
    def traverse_forward(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):
        actual_node = self.tail

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.previous

linked_list = Doubly_Linked_List()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)

print('------------TRAVERSE FORWARD---------------')
linked_list.traverse_forward()

print('------------TRAVERSE BACKWARD---------------')
linked_list.traverse_backward()
