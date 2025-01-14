from sortedcontainers import SortedList
from typing import List

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        arr = SortedList()
        sm = 0
        mod = 10**9 + 7
        
        for num in instructions:
            # Count elements less than `num`
            left_count = arr.bisect_left(num)
            # Count elements greater than `num`
            right_count = len(arr) - arr.bisect_right(num)
            # Add `num` to the sorted list
            arr.add(num)
            # Add the minimum cost to the total sum
            sm += min(left_count, right_count)
            sm %= mod
        
        return sm
