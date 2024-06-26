class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def get_element_at_index(self, index):
        if index < len(self.items):
            return self.items[index]
        else:
            return None

# تست کد
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.get_element_at_index(1))  # خروجی: 2