class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
         l = 0

         while l < len(nums):
            if l == nums[l] - 1:
                l += 1
                continue
            
            prev = nums[l]
            nums[nums[l] - 1],nums[l] = nums[l], nums[nums[l] - 1]

            if prev == nums[l]:
                return nums[l]
