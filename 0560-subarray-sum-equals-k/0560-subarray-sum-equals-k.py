class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # store for past records

        ps = nums
        
        # for i in range(len(nums)):
        #     ps.append(ps[-1] + nums[i])

        dd = defaultdict(int)
        dd[0] +=1
        ans = 0
        sm = 0
        for i in ps:
            sm += i
            ans += dd[sm - k]
            dd[sm] += 1
        
        return ans
            
        print(ps)
                