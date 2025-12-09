# Union find implementation with path compression optimization and union by size rank

class UnionFind:
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        self.size = [1] * n
        self.components = n # optional
    
    def find(self, A):
        if self.parent[A] == A:
            return A
        self.parent[A] = self.find(self.parent[A])
        return self.parent[A]
        
    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)
        if root_A == root_B:
            return False

        self.components -= 1
        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        return True

    def is_fully_connected(self):
        return self.components == 1

