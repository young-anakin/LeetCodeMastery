class Solution(object):
    def searchRange(self, nums, target):
        low, high = 0, len(nums)-1
        pos = True
        mid = -1
        
        while low <= high:
            mid = (low+high)//2
            if target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
            else :
                pos = False
                break
        # print(mid)
        # print(nums[:mid])
        # print(nums[mid:])
        print(mid)
        if pos == True:
            return [-1,-1]
        else :
            left = bisect_left((nums[:mid]), nums[mid])
            right = bisect_right(nums, nums[mid])
            return [left, right-1]
