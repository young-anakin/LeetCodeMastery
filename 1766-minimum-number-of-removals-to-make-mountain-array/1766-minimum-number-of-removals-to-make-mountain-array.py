class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        maxDp = [0 for ind in range(len(nums))]
        minDp = [0 for ind in range(len(nums))]


        n = len(nums)-1
        ans = 0
        nums = nums[::-1]
        while n >= 0:
            mx = 1
            for ind in range(n, len(nums)):
                if nums[n] > nums[ind]:
                    mx = max(maxDp[ind]+1, mx)
            
            maxDp[n] = max(maxDp[n], mx)
            
            n -=1
        nums = nums[::-1]
        n = len(nums)-1
        while n >= 0:
            mx = 1
            for ind in range(n, len(nums)):
                if nums[n] > nums[ind]:
                    mx = max(minDp[ind]+1, mx)
            
            minDp[n] = max(minDp[n], mx)
            
            n -=1

        maxDp = maxDp[::-1]
        print(maxDp)
        print(minDp)

        for ind in range(1, len(maxDp)-1):
            if maxDp[ind] != 1 and minDp[ind] != 1:
                ans = max(ans, (maxDp[ind] + minDp[ind])-1 )
        
        return len(maxDp) - ans

        return 0



