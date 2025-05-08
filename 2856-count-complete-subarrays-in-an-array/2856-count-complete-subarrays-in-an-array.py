class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # dictionary to store the count of values
        cp = defaultdict(int)
        # variable to store amount of unique values
        unique = len(set(nums))

        i = 0
        j = 0
        count = 0
        ans = 0
        while i < len(nums):
            if cp[nums[i]] == 0:
                count +=1
            cp[nums[i]] +=1
            
            while count >= unique:
                ans += (len(nums) - (i))

                cp[nums[j]] -=1
                if cp[nums[j]] == 0:
                    count -=1
                    j +=1
                    break
                j +=1
            i +=1
        
            # while count >= unique:
            #     ans += (len(nums) - (i))
            #     cp[nums[j]] -=1
            #     if cp[nums[j]] == 0:
            #         count -=1
            #         j +=1
            #         break
            #     j +=1
        return ans

