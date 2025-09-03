class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        b1 = 0
        b2 = 0

        if sum(nums)%2 != 0:
            return False
        # @cache
        memo = defaultdict(int)
        def dfs(i, target):
            if target == 0:
                return True
            
            if i >= len(nums):
                return False

            if target < 0:
                return False
            

            if (i, target) not in memo:
                memo[(i, target)] = dfs(i+1, target- nums[i]) or dfs(i+1, target)
            return memo[(i, target)]
        
        return dfs(0, target)




                