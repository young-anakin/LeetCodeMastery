class Solution(object):
    def removeDuplicates(self, nums):
        dict = {}
        count = 0
        a = 0
        b = 1
        dict[nums[0]] = 1
        while (b < len(nums)):
            if nums[b] not in dict:
                dict[nums[b]] = 1
                nums[a+1] = nums[b]
                a+=1
            b+=1
        return len(dict)
        