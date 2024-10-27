class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # Create a DP table with the same dimensions as the matrix
        dp = [[0] * cols for _ in range(rows)]

        # Variable to store the total number of square submatrices
        total_squares = 0

        # Iterate over each cell in the matrix
        for i in range(rows):
            for j in range(cols):
                # If the current cell is 1, check for square possibilities
                if matrix[i][j] == 1:
                    # If we're in the first row or column, just copy the value
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # Use the min value of the top, left, and diagonal-up-left cells + 1
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                    # Add the number of squares ending at this cell to the total count
                    total_squares += dp[i][j]

        return total_squares