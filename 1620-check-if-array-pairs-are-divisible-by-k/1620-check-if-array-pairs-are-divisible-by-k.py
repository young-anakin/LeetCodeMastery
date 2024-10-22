class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # Approach : Principle is (a+b)%k => (-a)%k = b%k
        dd = defaultdict(int)
        cp = 0
        for ind in range(len(arr)):
            val  = -(arr[ind]) %k 

            if dd[val] >= 1:
                dd[val]-=1
                cp +=1
            else:
                dd[arr[ind]%k] +=1
        if cp == len(arr)//2:
            return True
        return False