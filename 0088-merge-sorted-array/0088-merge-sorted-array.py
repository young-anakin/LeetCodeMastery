class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # a place to store the other characters
        other = nums1[:m]

        # one by one, put the elements of other and nums2 into nums1
        i, j = 0, 0
        for x in range(len(nums1)):
            if i == m:
                nums1[x] = nums2[j]
                j +=1
            elif j == n:
                nums1[x] = other[i]
                i +=1
            else:
                if other[i] <= nums2[j]:
                    nums1[x] = other[i]
                    i +=1
                else:
                    nums1[x] = nums2[j]
                    j +=1
        return nums1