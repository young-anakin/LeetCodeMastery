class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        tot = []
        bucket = []
        def backtrack():
            if len(nums) == len(bucket):
                tot.append(bucket[::])
                return 

            for ind in range(len(nums)):
                if nums[ind] in bucket:
                    continue
                
                bucket.append(nums[ind])
                backtrack()
                bucket.pop()
        backtrack()
        return tot