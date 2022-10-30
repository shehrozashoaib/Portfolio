class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"🍪" * self.size

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) > 0:
            self._capacity = capacity
        else:
            raise ValueError

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if int(size) >= 0 and int(size) <= self.capacity:
            self._size = size
        else:
            raise ValueError


