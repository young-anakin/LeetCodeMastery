class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        ans = []
        fl = False
        start = 0
        end = 0
        for ind in range(len(nums)-1):
            if nums[ind] +1 != nums[ind+1]:
                if fl:
                    val = str(start) + "->" + str(nums[ind])
                    ans.append(val)
                    fl = False
                else:
                    ans.append(str(nums[ind]))
            else:
                if fl:
                    continue
                fl = True
                start = nums[ind]
        
        if fl:
            ans.append(str(start) + "->" + str(nums[-1]))
        else:
            ans.append(str(nums[-1]))
        
        return ans
