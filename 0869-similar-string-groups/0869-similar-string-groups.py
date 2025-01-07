class UnionFind:
    def __init__(self, size):
        # Initially, each element is its own parent (self loop) and the rank is 1
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        # Iterative path compression
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        
        # Path compression step: make all nodes on the path point directly to the root
        while x != root:
            next_node = self.parent[x]
            self.parent[x] = root
            x = next_node
        
        return root

    def union(self, x, y):
        # Find the root of the sets that x and y belong to
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank heuristic: attach the shorter tree under the root of the taller tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        # Check if x and y are in the same subset
        return self.find(x) == self.find(y)
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        uf = UnionFind(len(strs))
        word = strs
        for ind in range(len(strs)):
            # print(word[ind])
            for j in range(ind + 1, len(strs)):

                cp = 0
                if len(word[ind]) != len(word[j]):
                    continue
                for x in range(len(word[j])):
                    # print(word[ind], word[j])
                    if word[ind][x] != word[j][x]:
                        cp +=1
                # print(word[ind], word[j], cp)
                if cp <= 2:
                    # print("Simmilar", word[ind], word[j])
                    uf.union(ind, j)
        
        for ind in range(len(strs)):
            uf.find(ind)
        # print(uf.parent)
        # print(uf.rank)
        return len(set(uf.parent))

