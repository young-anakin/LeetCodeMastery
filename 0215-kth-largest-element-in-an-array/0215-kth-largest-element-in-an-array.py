class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def split(arr):
            if len(arr) <= 1:
                return arr
            
            md = len(arr)//2
            first = arr[:md]
            second = arr[md:]

            first = split(first)
            second = split(second)

            return merge(first, second)

        
        def merge(first, second):
            i = 0
            j = 0
            new = []
            while i < len(first) and j < len(second):
                if first[i] < second[j]:
                    new.append(first[i])
                    i +=1
                else:
                    new.append(second[j])
                    j +=1
            
            new.extend(first[i:])
            new.extend(second[j:])
            return new
        
        return(split(nums)[-k])
