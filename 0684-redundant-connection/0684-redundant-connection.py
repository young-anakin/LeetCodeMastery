class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges)+1)]
        size = [0 for _ in range(len(edges)+1)]

        def find(x):
            root = x
            while root != parent[root]:
                root = parent[root]
            
            while x != root:
                next_node  = parent[x]
                parent[x] = root
                x = next_node
            
            return root
        def connect(i, j):
            x = find(i)
            y = find(j)

            if x == y:
                pass
            else:
                if size[x] > size[y]:
                    parent[y] = x
                elif size[x] < size[y]:
                    parent[x] = y
                else:
                    parent[y] = x
                    size[x] +=1
        
        def connected(x, y):
            return find(x) == find(y)

        graph = defaultdict(list)
        for u, v in edges:
            if connected(u, v):
                return [u, v]
            else:
                connect(u, v)
        
                