class Solution:
    def rob(self, nums: List[int]) -> int:
        # state = defaultdict(int)
        # def thief(ind):
        #     if  ind == 0:
        #         return nums[ind]
        #     if ind == 1:
        #         return max(nums[0], nums[1])
            
        #     if ind in state:
        #         return state[ind]
        #     res =  max(thief(ind-2) + nums[ind], thief(ind-1))
        #     state[ind] = res
        #     return res
        # return thief(len(nums) -1)
        memo = defaultdict(int)
        def dp(ind):
            if ind >= len(nums):
                return 0
            
            if ind in memo:
                return memo[ind]
            
            res = max(nums[ind] + dp(ind + 2), dp(ind + 1))
            memo[ind] = res
            return memo[ind]
        
        return dp(0)