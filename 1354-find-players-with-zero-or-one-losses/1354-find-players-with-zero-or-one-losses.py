class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        notLost = []
        oneLoss = []
        frequency = {}
        for i in range(0, len(matches)):
            if matches[i][0]  not in frequency:
                frequency[matches[i][0]] = 0
            if matches[i][1] not in frequency:
                frequency[matches[i][1]] = 1
            else:
                frequency[matches[i][1]] += 1
        for key, values in frequency.items():
            if values == 0:
                notLost.append(key)
            if values == 1:
                oneLoss.append(key)
        notLost.sort()
        oneLoss.sort()
        return((notLost), 
               (oneLoss))