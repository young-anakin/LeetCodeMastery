class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dd = defaultdict(int)
        for ind in range(len(nums)):
            for j in range(ind+1, len(nums)):
                dd[nums[ind] * nums[j]] +=1
        
        sm = 0
        print(dd)
        for key, val in dd.items():
            if val > 1:
                sm += val * (val-1)//2 *8
        
        return sm

        # return sum(dd.values())