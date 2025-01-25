class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        size = [0 for ind in range(len(nums))]
        parent = [ind for ind in range(len(nums))]
        print(size)
        og = defaultdict(int)
        
        def find(ind):
            # Path halving: make each node point to its grandparent
            while ind != parent[ind]:
                parent[ind] = parent[parent[ind]]  # Point to grandparent
                ind = parent[ind]
            return ind
        
        def connect(ind, j):
            x = find(ind)
            y = find(j)

            if x == y:
                pass

            if size[x] >= size[y]:
                parent[y] = parent[x]
                size[x] += 1
            else:
                parent[x] = parent[y]
                size[y] += 1
        
        x = list()
        ss = list(sorted(nums))
        for ind in range(len(ss)):
            x.append((ss[ind], ind))
        for ind in range(1, len(x)):
            if abs(x[ind][0] - x[ind-1][0]) <= limit:
                # print(x[ind][0], x[ind-1][0])
                # print(ind, ind-1, size)
                connect(ind, ind-1)        
        p = defaultdict(deque)
        for ind in range(len(parent)):
            p[parent[ind]].append(x[ind])
            og[x[ind][0]] = parent[ind]
        ans = [0 for ind in range(len(nums))]
        q = defaultdict(deque)
        for ind, val in p.items():
            v = deque(sorted(val))
            q[ind] = v
        
        for ind in range(len(nums)):
            mama = og[nums[ind]]
            ans[ind] = q[mama].popleft()[0]


        return ans
