class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1

        while low <= high:
            md = (low + high)//2

            if nums[md] == target:
                return md
            elif nums[md] < target:
                low = md+1
            else:
                high = md-1
        
        return -1
                
        

