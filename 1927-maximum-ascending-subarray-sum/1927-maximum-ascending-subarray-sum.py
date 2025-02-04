class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mx = 0

        stack = [0]

        for ind in nums:
            if ind > stack[-1]:
                stack.append(ind)
            else:
                mx = max(mx, sum(stack))
                stack = [0]
                stack.append(ind)
            
            # print(stack)
        
        mx = max(mx, sum(stack))
        
        return mx