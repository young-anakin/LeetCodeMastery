class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dd = defaultdict(int)
        cp = 0
        mx = 0
        dd[0] = -1
        for ind in range(len(nums)):
            if nums[ind] == 0:
                cp -=1
                # dd[cp] = ind
            else:
                cp +=1
                # dd[cp] = ind
            
            if cp in dd:
                mx = max(mx, abs(ind - dd[cp]))
            else:
                dd[cp] = ind

            # print(cp)
            # dd[cp] = ind
        
        return mx







