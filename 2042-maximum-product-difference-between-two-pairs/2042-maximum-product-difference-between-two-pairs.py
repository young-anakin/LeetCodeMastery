class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return abs(nums[0]*nums[1] - nums[-1]*nums[-2])