class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # checker function
        def checker(md):
                capacity = 0
                expectedDays = 0
                for val in weights:
                    capacity += val
                    if capacity > md:
                        expectedDays +=1
                        capacity = val
                
                expectedDays +=1

                return expectedDays <= days


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
        
        



