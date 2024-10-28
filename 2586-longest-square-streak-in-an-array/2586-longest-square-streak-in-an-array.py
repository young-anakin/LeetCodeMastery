class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        nums.sort()

        ss = set(nums)
        checked = set()
        mx =0 
        cp = 0
        dd = defaultdict(int)
        for ind in nums:
            if ind not in checked and int(ind*ind) in ss:
                dd[ind] +=1
                dd[ind*ind] += dd[ind]
                mx = max(mx, dd[ind])
                checked.add(ind)
        
        print(dd)
        if mx == 0:
            return -1
        return mx+1
