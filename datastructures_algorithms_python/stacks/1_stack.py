#LIFO - Last In First Out

class Stack:
    def __init__(self):
        self.stack = []

    # insert item into stack
    def push(self, data):
        self.stack.append(data)

    # remove and return the last item we have inserted // O(1)
    def pop(self):

        if self.stack_size() < 1:
            return -1

        data = self.stack[-1]
        del self.stack[-1]
        return data

    # peek: returns last item without removing it // O(1)
    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print('size: %d' % stack.stack_size())
print('popped item: %d' % stack.pop())
print('size: %d' % stack.stack_size())
print('peek item: %d' % stack.peek())