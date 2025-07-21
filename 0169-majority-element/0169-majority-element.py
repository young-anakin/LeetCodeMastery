class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # dictionary -> data structure 
        # Counter - > Dictionary

        cp = Counter(nums)
        mx = 0
        ans = 0
        for a, b in cp.items():
            if b > mx:
                mx = b
                ans = a

        
        # cp = {2: 4, 1: 3} 
        # mx = 0, ans = 0
        # key = 2 value = 4
        # mx = 4
        # ans = 2

        # key = 1, value = 3
        # mx = 4 value = 3
        # mx = 4
        # ans = 2

        return ans




            
