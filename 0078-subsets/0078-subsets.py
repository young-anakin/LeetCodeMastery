class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        bucket = list()

        # [], [1], [1, 2]
        def backtracking(ind, unique):
            if ind >= len(nums):
                bucket.append(unique)
                return
            
            # bucket.append(unique)
            unique.append(nums[ind])
            # we add a number at an index
            backtracking(ind+1, unique.copy())

            # we leave a number at an index
            unique.pop()
            backtracking(ind+1, unique.copy())
        
        backtracking(0, [])
    
        return(bucket)
