class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        sm = 0
        mx = max(nums)
        for ind in range(k):
            sm += mx
            mx +=1
        
        return sm