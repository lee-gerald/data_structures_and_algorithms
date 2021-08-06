# track the largest item during insertion
# the get_max operation needs to be O(1) running time
# the memory complexity can be O(N) which means we can use another stack
# in the implementation

class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, data):
        self.stack.append(data)

        if (len(self.stack) == 1):
            self.max_stack.append(data)
            return

        if (data > self.max_stack[-1]):
            self.max_stack.append(data)
        else:
            # if it's not the largest in the stack, we can duplicate the largest one into the max_stack
            self.max_stack.append(self.max_stack[-1])

        return self.stack
    
    def pop(self):
        last_item = self.stack[-1]
        del self.stack[-1]
        return last_item

    def stack_size(self):
        return len(self.stack)

    def get_max(self):
        # O(1)
        return self.max_stack[-1]

stack = Stack()

stack.push(10)
stack.push(5)
stack.push(1)
stack.push(122)
stack.push(100)
print('stack size %d' % stack.stack_size())

print('max: %d' % stack.get_max())




    