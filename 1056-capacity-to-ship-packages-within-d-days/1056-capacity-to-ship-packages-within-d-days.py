class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # checker function
        def checker(md):
            # if we can ship -> return True

            capacity = 0
            curr = 0
            for ind in weights:
                curr += ind
                if curr <= md:
                    continue
                else:
                    capacity += 1
                    curr = ind
            
            capacity +=1
            
            return capacity <= days


        # Binary Search function
        valid = 0
        def binarySearch(left, right):
            nonlocal valid
            while left <= right:
                md = (left + right)//2
                print(md)
                # this means that the md point can ship the packages 
                if checker(md):
                    valid = md
                    right = md - 1 
                else:
                    left = md + 1
        

        binarySearch(max(weights), sum(weights))
        return valid
        
        



