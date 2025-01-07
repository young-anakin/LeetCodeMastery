class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        a, b = 0,0
        merged = []
        while a < len(nums1) and b < len(nums2):
            if nums1[a][0] == nums2[b][0]:
                merged.append([nums1[a][0], nums1[a][1] + nums2[b][1]])
                a +=1
                b +=1
            elif nums1[a][0] < nums2[b][0]:
                merged.append(nums1[a])
                a +=1
            else:
                merged.append(nums2[b])
                b +=1
        
        merged.extend(nums1[a:])
        merged.extend(nums2[b:])
        return merged