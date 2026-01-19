class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top = 0
        bottom = len(matrix) - 1
        right = len(matrix) - 1
        left = 0

        while top < bottom and left < right:
            numItemsToRotate = bottom - top
            for i in range(numItemsToRotate):
                temp = matrix[top][left+i]
                
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = temp
            
            top +=1
            bottom -=1
            left +=1
            right -=1

        