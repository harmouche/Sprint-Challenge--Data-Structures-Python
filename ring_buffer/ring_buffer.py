
class RingBuffer:
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
        self.oldest_item_index = 0

    def append(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.oldest_item_index] = item
        self.oldest_item_index += 1

        if self.oldest_item_index == self.capacity:
            self.oldest_item_index = 0

    def get(self):
        return self.items

# From Readme File

buffer = RingBuffer(3)

buffer.get()   # should return []
print(buffer.get())

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']
print(buffer.get())

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']
print(buffer.get())

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']        
print(buffer.get())