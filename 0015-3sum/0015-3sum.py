class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        print(nums)
        ans = set()
        def twoSum(i, x):
            left = i
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == - nums[x]:
                    y = [nums[x]]
                    y.extend(list((nums[left], nums[right])))
                    # print(x)
                    ans.add(tuple(y))
                    left +=1
                    right -=1
                # return (nums[left], nums[right])
                elif nums[left] + nums[right] < - nums[x]:
                    left +=1
                else:
                    right -=1
            return None
        for i in range(len(nums)):
            # i + j + k = 0
            # j + k = -i
            # for j in range(i+1, len(nums)):
                # print(twoSum(j), )
            steve = twoSum(i+1, i)
            if steve != None:
                # print(twoSum(j))
                x = [nums[i]]
                x.extend(list((steve[0], steve[1])))
                # print(x)
                ans.add(tuple(x))

        return list(set(ans))