class MyHashSet:

    def __init__(self):
        self.mp=defaultdict(int)

    def add(self, key: int) -> None:
        self.mp[key]=True

    def remove(self, key: int) -> None:
        self.mp[key]=False

    def contains(self, key: int) -> bool:
        if self.mp[key]!=0:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)