# implement the queue abstract data type with enqueue() and dequeue()
# operations with stacks
# use 2 stacks to solve this problem. one stack for each operation
#FIFO

class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)
    
    def dequeue(self):
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("stacks are empty")
        
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        
        return self.dequeue_stack.pop()


queue = Queue()

queue.enqueue(4)
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(1)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())







    