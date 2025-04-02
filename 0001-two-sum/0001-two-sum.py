class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dd = defaultdict(int)

        for i, val in enumerate(nums):
            dd[val] = i

        
        for i, val in enumerate(nums):
            if target - val in dd and i != dd[target-val]:
                return [i, dd[target-val]]