# FIFO - First In First Out

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    # O(1)
    # O(N) if we used a standard linked list. fastest to use doubly linked list.
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) linear runnning time. would be faster to use a doubly linked list.
    # when manipulating the first of the array, the whole array would have to shift afterwards
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return -1

    def peek(self):
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print('size: %d' % queue.size_queue())
print('dequeue %d' % queue.dequeue())
print('size: %d' % queue.size_queue())

