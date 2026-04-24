class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item) 

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) 
        return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0 

    def display(self):
        print(self.queue)

q = Queue()
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)

q.display()
print("Front: ", q.front())
print("Dequeued: ", q.dequeue())
q.display()
