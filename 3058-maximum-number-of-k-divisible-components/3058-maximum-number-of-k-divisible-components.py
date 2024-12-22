class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        visited = set()
        # visited.add()
        ans = 0
        def dfs(val):
            nonlocal ans
            visited.add(val)
            x = values[val]
            for ind in tree[val]:
                if ind not in visited:
                    x += dfs(ind)
            
            if x % k == 0:
                ans +=1
                return 0
            return x


        
        dfs(0)
        return ans
        print(ans)

