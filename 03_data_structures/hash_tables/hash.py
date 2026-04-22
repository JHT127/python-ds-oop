import math
from node import Node


class HashTable:
    def __init__(self, size=7, threshold=0.7):
        self.size = size
        self.threshold = threshold
        self.count = 0
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def load_factor(self):
        return self.count / self.size

    def is_prime(self, x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    def find_next_prime(self):
        double_size = 2 * self.size
        while not self.is_prime(double_size):
            double_size += 1
        return double_size

    def rehash(self):
        old_table = self.table
        self.size = self.find_next_prime()
        self.table = [None] * self.size
        self.count = 0
        for node in old_table:
            if node is not None:
                self.insert(node.key, node.value)

    def insert(self, key, value):
        if self.load_factor() >= self.threshold:
            self.rehash()
        indx = self.hash_function(key)
        probe = 0
        while probe < self.size:
            new_indx = (indx + probe * probe) % self.size # Quadratic probing
            if self.table[new_indx] is None:
                self.table[new_indx] = Node(key, value)
                self.count += 1
                return
            probe += 1

    def delete(self, key):
        indx = self.hash_function(key)
        probe = 0
        while probe < self.size:
            new_indx = (indx + probe * probe) % self.size  # Quadratic probing
            node = self.table[new_indx]
            if node and node.key == key:
                self.table[new_indx] = None
                self.count -= 1
                return True
            probe += 1
        return False

    def search(self, key):
        indx = self.hash_function(key)
        probe = 0
        while probe < self.size:
            new_indx = (indx + probe * probe) % self.size  # Quadratic probing
            node = self.table[new_indx]
            if node and node.key == key:
                return node
            probe += 1
        return None