class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        
        nums.sort()
        # 0 1 4 4 5 7
        ans = 0
        print(nums)
        for ind in range(len(nums)-1):
            x = nums[ind]
            minimumOption = lower - nums[ind]
            
            maximumOption = upper - nums[ind]
            mn = bisect_left(nums, minimumOption, ind+1)
            mx = bisect_right(nums, maximumOption, ind+1)-1

            if mn <= mx:
                ans += abs(mx - mn)+1
        return ans