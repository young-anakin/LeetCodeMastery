class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mx = 0

        a = 0
        b = k
        sm = 0
        dd = defaultdict(int)
        for ind in range(k):
            sm += nums[ind]
            dd[nums[ind]] +=1
        
        while b < len(nums):
            # print(dd)
            if len(dd) == k:
                mx = max(mx, sm)
            dd[nums[a]] -=1
            sm -= nums[a]
            if dd[nums[a]] == 0:
                del dd[nums[a]]
            dd[nums[b]] +=1
            sm += nums[b]
            a +=1
            b +=1
        # print(dd, sm)
        if len(dd) == k:
            mx = max(sm, mx)

        return mx