class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sm = 0
        # fl = True
        for ind in range(0, len(nums)):
            if ind%2 == 0:
                sm += nums[ind]

        
        return sm
