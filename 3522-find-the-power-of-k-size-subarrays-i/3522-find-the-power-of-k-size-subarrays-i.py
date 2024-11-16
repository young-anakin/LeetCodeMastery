class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        x = 0
        arr = deque()
        for ind in range(k):
            arr.append(nums[ind])
        
        ans = []
        y = k
        while y <= len(nums):
            fl = True
            for ind in range(1, len(arr)):
                if arr[ind] == arr[ind-1] + 1:
                    fl = True
                else:
                    fl = False
                    break
            if fl:
                ans.append(max(arr))
            else:
                ans.append(-1)

            if y == len(nums):
                break
            arr.append(nums[y])
            arr.popleft()
            y +=1
        
        # print(arr)

        return ans
