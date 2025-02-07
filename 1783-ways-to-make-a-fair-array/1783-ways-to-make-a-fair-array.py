class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd = [0]
        even = [0]
        for ind in range(len(nums)):
            if ind %2 == 0:
                even.append(even[-1] + nums[ind])
                odd.append(odd[-1])
            else:
                odd.append(odd[-1] + nums[ind])
                even.append(even[-1])
        
        even = even[1:]
        odd = odd[1:]
        ans = 0
        # print("e", even)
        # print("O", odd)
        oddCp, evenCp = 0,0
        ans = 0
        for ind in range(len(nums)):
            if ind %2 == 0:
                rightEven = even[-1] - even[ind]
                oddCount = oddCp + rightEven

                rightOdd = odd[-1] - odd[ind]
                evenCount = evenCp + rightOdd

                evenCp += nums[ind]
                # rightOdds = 
            else:
                rightOdd = odd[-1] - odd[ind]
                evenCount = evenCp + rightOdd

                rightEven = even[-1] - even[ind]
                oddCount = oddCp + rightEven

                oddCp += nums[ind]
            if oddCount - evenCount == 0:
                ans +=1
        return ans
            # print(oddCount, evenCount)
        # print(even)
        # print(odd)
