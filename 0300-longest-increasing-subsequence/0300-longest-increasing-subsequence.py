class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]

        n -=1
        while n >= 0:
            if n == len(nums) - 1:
                dp[n] = 1
                n -=1
            
            else:
                mx = 1
                for ind in range(n, len(nums)):
                    if nums[n] < nums[ind]:
                        mx = max(mx, dp[ind]+1)
                
                dp[n] = mx
        
                n -=1
        
        # print(dp)
        return max(dp)



            

            






