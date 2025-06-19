class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        # we want a checker to check wether a certain capacity can haul all of the ships

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
        

        low, high = max(weights), sum(weights)
        valid = 0
        print(high)
        while low < high:
            md = (low + high)//2
            print(md, checker(md))
            if checker(md):
                valid = md
                high = md 
            else:
                low = md + 1
        
        return low
            
