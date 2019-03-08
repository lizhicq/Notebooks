class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.father = [0 for _ in range(n+1)]
        self.size = [1 for _ in range(n+1)]

    def find(self, x):
        if self.father[x] == 0:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size[root_b] += self.size[root_a]

    def query(self, a):
        return self.size[self.find(a)]