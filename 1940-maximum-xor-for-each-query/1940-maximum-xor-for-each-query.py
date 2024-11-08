class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        return [*accumulate(nums, xor, initial=(1<<maximumBit)-1)][:0:-1]