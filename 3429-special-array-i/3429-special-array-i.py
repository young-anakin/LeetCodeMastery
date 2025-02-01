class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for ind in range(len(nums)-1):
            if nums[ind] %2 == nums[ind+1]%2:
                return False
        
        return True