class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        mx = 0
        nums.sort()
        # print(nums)
        for ind in range(1, len(nums)):
            mx = max(mx, abs(nums[ind] - nums[ind-1]))
        
        return mx