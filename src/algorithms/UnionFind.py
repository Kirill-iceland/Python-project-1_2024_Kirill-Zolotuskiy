class UnionFind:
    data = []
    def __init__(self, size):
        for i in range(size):
            self.data.append(i)

    def find(self, index: int) -> int:
        if self.data[index] == index:
            return index
        self.data[index] = self.find(self.data[index])
        return self.data[index]
    
    def connected(self, index1: int, index2: int) -> bool:
        return self.find(index1) == self.find(index2)
    
    def union(self, index1: int, index2: int):
        index1 = self.find(index1)
        index2 = self.find(index2)
        self.data[index1] = index2
