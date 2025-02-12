class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        cp = defaultdict(list)
        for ind in nums:
            val = str(ind)
            
            tmp = 0
            for i in val:
                tmp += int(i)
            
            val = str(tmp)
            cp[val].append(ind)
        mx = -1
        # print(cp)
        for key, val in cp.items():
            x = list(sorted(val))
            if len(x) >= 2:
                mx = max(mx, x[-1] + x[-2])
        
        return mx
        print(cp)
