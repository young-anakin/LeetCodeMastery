class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = defaultdict(int)
        def dp(ind, tmp):

            if ind == len(nums):
                if tmp == target:
                    return 1
                else:
                    return 0
            
            if (ind, tmp) not in memo : 
                val1 = dp(ind+1, tmp + nums[ind])
                val2 = dp(ind+1, tmp - nums[ind])

                memo[(ind, tmp)] = val1 + val2
            

            return memo[(ind, tmp)]
        
        return dp(0,0)

