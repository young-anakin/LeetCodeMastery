class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dd = defaultdict(int)

        for i in range(len(nums)):
            if target - nums[i] in dd:
                return [i, dd[target-nums[i]]]
            else:
                dd[nums[i]] = i
        
        return 