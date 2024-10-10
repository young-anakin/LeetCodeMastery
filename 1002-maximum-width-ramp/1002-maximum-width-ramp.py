class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        mStack = []
        for i, val in enumerate(nums):
            if not mStack:
                mStack.append(i)
            else:
                if nums[mStack[-1]] > val:
                    mStack.append(i)
        
        other = list()
        other = nums[::-1]
        n = len(nums)-1

        print(mStack)
        print(nums)
        ans = 0
        for ind in range(len(nums)):
            while mStack and nums[mStack[-1]] <= other[ind]:
                # print(n, mStack[-1])
                # print(nums[ind], nums[mStack[-1]])
                ans = max(ans, n-mStack[-1])
                mStack.pop()
            n-=1
        
        return ans

