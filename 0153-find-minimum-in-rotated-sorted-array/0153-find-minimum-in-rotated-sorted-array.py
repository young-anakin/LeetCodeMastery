class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            md = (left + right)//2

            if nums[md] > nums[right]:
                left = md + 1
            else:
                right = md
        
        print(right)
        return nums[right]