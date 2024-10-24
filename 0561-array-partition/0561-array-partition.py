class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sm = 0
        fl = True
        for ind in range(0, len(nums)):
            if fl:
                sm += nums[ind]
                fl = False
            else:
                fl = True
        
        return sm
