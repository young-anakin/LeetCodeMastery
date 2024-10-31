class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a = 0
        b = k

        if k == 1 and len(nums) == 1:
            return False
        cp = defaultdict(int)
        ind = 0
        while ind < len(nums) and ind <= b:
            cp[nums[ind]] +=1
            if cp[nums[ind]] == 2:
                return True
            ind +=1

        print(cp)
        
        
        for ind in range(b+1, len(nums)):
            cp[nums[a]] -=1
            cp[nums[ind]] +=1
            a+=1
            if cp[nums[ind]] >=2 :
                return True
        
        return False
