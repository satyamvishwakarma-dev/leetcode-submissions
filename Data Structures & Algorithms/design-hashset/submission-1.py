class MyHashSet:

    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.buckets = [[] for _ in range(self.capacity)]

    def MyHashSet_index(self, key) -> int:
        return hash(key) % self.capacity

    def add(self, key: int) -> None:
        index = self.MyHashSet_index(key)
        buckets = self.buckets[index]
        if key not in buckets:
            buckets.append(key)

    def remove(self, key: int) -> None:
        index = self.MyHashSet_index(key)
        bucket = self.buckets[index]
        
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        index = self.MyHashSet_index(key)
        bucket = self.buckets[index]
        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)