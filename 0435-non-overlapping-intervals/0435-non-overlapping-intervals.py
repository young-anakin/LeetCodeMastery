class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        cp = 0
        last = intervals[0]
        for ind in range(1, len(intervals)):
            if intervals[ind][0] < last[1]:
                cp +=1
            else:
                last = intervals[ind]
        
        print(intervals)
        return cp