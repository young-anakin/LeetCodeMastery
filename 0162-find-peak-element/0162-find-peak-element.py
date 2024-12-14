class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for ind in range(1, len(nums)-1):
            if nums[ind] > nums[ind-1] and nums[ind] > nums[ind+1]:
                return ind
        
        return nums.index(max(nums))