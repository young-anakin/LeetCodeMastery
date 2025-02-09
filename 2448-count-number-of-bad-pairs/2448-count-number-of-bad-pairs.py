class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        cp = 0
        tot = 0
        dd = defaultdict(int)
        for ind, val in enumerate(nums):
            x = ind - val
            tot += (ind - dd[x])
            dd[ind - val] +=1
        
        return tot
        