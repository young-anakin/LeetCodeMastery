class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # 1 2 4 6

        mx = -1
        nums.sort()
        for ind, val in enumerate(nums):
            x = bisect.bisect_right(nums, val + (2*k))
            mx = max(mx, abs(x-ind))
            # print(x)
        
        return mx