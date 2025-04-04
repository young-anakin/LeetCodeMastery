class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        curr = 0
        flag = False
        mn, mx = 0, 0
        ans = []
        while curr < len(intervals):
            if flag == False:
                flag = True
                mn = intervals[curr][0]
                mx = intervals[curr][1]
            else:
                curr_a, curr_b = intervals[curr][0], intervals[curr][1]
                if curr_a > mn and curr_a > mx:
                    ans.append([mn, mx])
                    mn = intervals[curr][0]
                    mx = intervals[curr][1]
                else:
                    mn = min(curr_a, mn)
                    mx = max(curr_b, mx)
                
            curr +=1
        
        if flag:
            ans.append([mn, mx])
        
        return ans


