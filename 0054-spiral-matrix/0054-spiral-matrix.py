class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1
        
        answer = []
        
        while len(answer) < rows * cols:
            # append the first row values starting from the left
            for index in range(left, right + 1):
                answer.append(matrix[top][index])
            top += 1
            # 1 2 3
            # from the top right to the bottom right 
            for index in range(top, bottom + 1):
                answer.append(matrix[index][right])
            right -= 1
            # 1 2 3 6 9 
            
            # from right to left
            if top <= bottom: 
                for index in range(right, left - 1, -1):
                    answer.append(matrix[bottom][index])

                bottom -= 1
            # 1 2 3 6 9 8 7
            
            # from bottom to the top
            if left <= right:
                for index in range(bottom, top - 1, -1):
                    answer.append(matrix[index][left])
                left += 1
            
        return answer