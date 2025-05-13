class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        mstack = []
        mn = float("inf")

        for ind in range(len(nums)):
            while mstack and mstack[-1][0] <= nums[ind]:
                mstack.pop()
            
            if mstack and mstack[-1][1] < nums[ind]:
                return True
            
            mn = min(mn, nums[ind])
            mstack.append((nums[ind], mn))
        
        return False