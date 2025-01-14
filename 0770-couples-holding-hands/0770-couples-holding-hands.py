class Solution:
    def minSwapsCouples(self, nums: List[int]) -> int:
        dic = dict()
        for i in range(len(nums)):
            dic[nums[i]] = i

        count = 0
        for i in range(0,len(nums),2):
            if nums[i]%2==0:
                partener = nums[i]+1
            else:
                partener = nums[i]-1

            stranger = nums[i+1]
            if stranger!=partener:
                nums[i+1], nums[dic[partener]] = partener, stranger
                dic[partener], dic[stranger] = i+1, dic[partener]
                count+=1
        return count