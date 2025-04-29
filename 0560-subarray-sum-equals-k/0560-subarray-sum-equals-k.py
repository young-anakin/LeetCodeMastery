class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sm = 0
        memo = defaultdict(int)
        memo[0] +=1
        ans = 0
        
        # to iterate over the array and calculate the subarrays
        for ind in nums:

            # what subracted from my current sum will give me k?
            # sm - x = k
            # sm - k = x
            sm += ind
            ans += memo[(sm - k)]
            memo[sm] += 1

        return ans

        