class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return "Element found"
            current = current.next
        return "Element not found" 

    def display(self):
        current = self.head
        output = []
        while current:
            output.append(str(current.data))
            current = current.next
        print(" -> ".join(output) + " -> None") 

llist = LinkedList()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
print("Linked List after adding 10, 20, 30:")
llist.display() 
llist.insert_at_beginning(5)
print("\nAfter inserting 5 at beginning:")
llist.display() 
print(f"\nSearch 30: {llist.search(30)}") 
print(f"Search 100: {llist.search(100)}") 
llist.delete_node(20)
print("\nAfter deleting 20:")
llist.display() 