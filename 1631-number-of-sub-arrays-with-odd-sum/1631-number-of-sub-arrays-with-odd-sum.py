class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        oddCount = 0
        evenCount = 0

        mod = 10 **9 + 7

        prefix = [0]
        for ind in range(len(arr)):
            prefix.append(prefix[-1] + arr[ind])
        
        print(prefix)
        ans = 0
        for ind in range(len(prefix)):
            if prefix[ind] != 0 and prefix[ind] %2 == 0:
                evenCount +=1
                # ans +=1
                ans += oddCount
            
            elif prefix[ind] != 0 and prefix[ind] %2 == 1:
                oddCount +=1
                ans += 1
                ans += evenCount
        
        return ans % mod


        print(prefix)