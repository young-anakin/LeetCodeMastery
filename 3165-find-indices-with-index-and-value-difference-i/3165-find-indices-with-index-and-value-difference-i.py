class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for ind in range(0, len(nums)):
            for j in range(ind, len(nums)):
                if abs(ind-j) >= indexDifference and abs(nums[ind] - nums[j]) >= valueDifference:
                    return [ind,j]
        
        return [-1, -1]