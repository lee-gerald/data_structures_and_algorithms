class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = parent


class Binary_Search_Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # inserting to the left subtree
        if data < node.data:
            if node.left_child: # if not none
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
        # inserting to the right subtree
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)
        
    def get_max(self, node):
        if node.right_child:
            return self.get_max(node.right_child)
        
        return node.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)
        
    def get_min(self, node):
        if node.left_child:
            return self.get_min(node.left_child)
        
        return node.data

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)
    
    def traverse_in_order(self, node):
        if node.left_child: # is not none
            self.traverse_in_order(node.left_child)

        print('%s' % node.data)

        if node.right_child: # is not none
            self.traverse_in_order(node.right_child)
    
    def remove_node(self, data, node):
        if node is None:
            return
        
        if data < node.data:
            self.remove_node(data, node.left_child)
        elif data > node.data:
            self.remove_node(data, node.right_child)
        else:
            
            if node.left_child is None and node.right_child is None:
                print('removing leaf node: %d' % node.data)
                parent = node.parent

                if parent is not None and parent.left_child == node:
                    parent.left_child = None
                if parent is not None and parent.right_child == node:
                    parent.right_child = None 
                
                if parent is None:
                    self.root = None

                del node
            
            elif node.left_child is None and node.right_child is not None:
                print("removing a node with a single right child...")
                parent = node.parent

                if parent is not None:
                    if parent.left_child == node:
                        parent.left_child = node.right_child
                    if parent.right_child == node:
                        parent.right_child = node.right_child
                else:
                    self.root = node.right_child

                node.right_child.parent = parent
                del node
            
            elif node.right_child is None and node.left_child is not None:
                print("removing a node with a single left child..")

                parent = node.parent

                if parent is not None:
                    if parent.left_child == node:
                        parent.left_child = node.left_child
                    if parent.right_child == node:
                        parent.right_child = node.left_child
                
                else:
                    self.root = node.left_child
                
                node.left_child.parent = parent
                del node
            
            else:
                print('removing node with 2 children...')
                
                # get the largest item in the left subtree
                predecessor = self.get_predecessor(node.left_child)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)
    
    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)
        return node
    
    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)
                


bst = Binary_Search_Tree()
bst.insert(10)
bst.insert(5)
bst.insert(-5)
bst.insert(1)
bst.insert(66)
bst.insert(34)

bst.traverse()

print('after removal')

bst.remove(10)
bst.traverse()