class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

     def insert(self,value, idx):

         if self.count == self.capacity:

         if idx >= self.count:

        for i in range(self.count, idx, -1):
            self.storage[i] = self.storage[i - 1]

        self.storage[idx] = value
        self.count += 1

    def append(self, value):
        if self.count = self.capacity:
            print("Error: Array is full")
            return

        self.storage[self.count] = value 
        self.count += 1


    def double_Size(self):
        self.capacity *= 2

        temp_storage = [None] * self.capacity

        for i in range(self.count):
            temp_storage[i] = self.storage[i]

        self.storage = temp_storage
        
