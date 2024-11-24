class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sm = 0
        mn = float("inf")
        pos, neg = 0,0
        for ind in range(len(matrix)):
            # cp = 0
            # neg, pos = [], []
            for j in range(len(matrix)):
                sm += abs(matrix[ind][j])
                mn = min(abs(matrix[ind][j]), mn)
                if matrix[ind][j] > 0:
                    pos +=1
                else:
                    neg +=1
        
        print(mn, neg, sm)
        if neg % 2 == 0:
            return sm
        else:
            return sm - 2*mn

            

                

                        
            