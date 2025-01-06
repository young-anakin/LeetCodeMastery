class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for ind in range(len(boxes)):
            cp = 0
            for j in range(len(boxes)):
                if ind == j:
                    continue
                if boxes[j] == "1":

                    cp += abs(ind-j)
            ans.append(cp)


        return ans