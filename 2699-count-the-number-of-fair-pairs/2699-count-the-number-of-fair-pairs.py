from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0

        for ind in range(len(nums) - 1):
            # Calculate the range of values to find pairs within the bounds
            minimumOption = lower - nums[ind]
            maximumOption = upper - nums[ind]

            # Use bisect_left and bisect_right with the adjusted start index to avoid slicing
            mn = bisect_left(nums, minimumOption, ind + 1)
            mx = bisect_right(nums, maximumOption, ind + 1) - 1

            # If valid indices are found within bounds, count the pairs
            if mn <= mx:
                ans += mx - mn + 1

        return ans
