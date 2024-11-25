class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashValues = {}
        output = []
        for a in range(0, len(nums)):
            if target - nums[a] not in hashValues:
                hashValues[nums[a]] = a
            else:
                output.append(hashValues[target-nums[a]])
                output.append(a)
                return output