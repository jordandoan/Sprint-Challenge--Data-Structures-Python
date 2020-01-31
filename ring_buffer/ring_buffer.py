from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length >= self.capacity:
            self.current.value = item
            self.current = self.current.next
        else:
            self.storage.add_to_tail(item)
        if not self.current:
            self.current = self.storage.head
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head
        while current:
            if current.value is not None:
                list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity
        self.size = 0

    def append(self, item):
        if self.size == self.capacity:
            self.storage[self.current] = item
            self.current += 1
            if self.current == self.capacity:
                self.current = 0
        else:
            self.storage[self.size] = item
            self.size += 1

    def get(self):
        return [i for i in self.storage if i is not None]
