class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.num_matrix = [[0]*(col+1)for r in range((row+1))]
        for r in range(row):
            prefix = 0
            for c in  range(col):
                prefix += matrix[r][c]
                above = self.num_matrix[r][c+1]
                self.num_matrix[r+1][c+1] = prefix + above

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 , col1, row2 , col2 = row1+1 ,col1+1 , row2 +1 ,col2 + 1
        bottom_right = self.num_matrix[row2][col2]
        top_left = self.num_matrix[row1-1][col1-1]
        left = self.num_matrix[row2][col1-1]
        above = self.num_matrix[row1-1][col2]
        return bottom_right - left - above  + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)