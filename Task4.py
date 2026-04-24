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

service_queue = Queue()
customers = ['Sonam', 'Pema', 'Karma'] 

for c in customers:
    service_queue.enqueue(c)

print("Customers waiting:")
service_queue.display() 
print(f"Serving customer: {service_queue.dequeue()}")
print("Remaining queue:")
service_queue.display() 