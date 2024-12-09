class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ps = [0] * len(nums)
        ps[0] = 0
        ans = [False] * len(queries)
        for ind in range(1, len(nums)):
            if nums[ind] % 2 == nums[ind-1]%2:
                ps[ind] = ps[ind-1] + 1
            else:
                ps[ind] = ps[ind-1]
        
        for ind in range(len(queries)):
            query = queries[ind]
            start = query[0]
            end = query[1]

            ans[ind] = ps[end] - ps[start] == 0
        
        return ans
        # ps.append(nu)