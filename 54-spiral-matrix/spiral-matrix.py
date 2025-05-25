class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        minRow, minCol = 0, 0
        rows, cols = len(matrix), len(matrix[0])

        totalLength = rows * cols
        
        if rows == 0 and cols == 0:
            return res


        dxns = [(0,1), (1,0), (0,-1), (-1,0)]
        dIndex = 0
        i = minRow
        j = minCol

        k = 0
        while k < totalLength:
            # if out of bounds
            if not (minRow <= i < rows and minCol <= j < cols):
                if dIndex == 0:
                    minRow+=1
                    i = minRow
                    j = cols - 1

                if dIndex == 1:
                    cols-=1
                    i = rows - 1
                    j = cols - 1

                if dIndex == 2:
                    rows -= 1
                    i = rows - 1
                    j = minCol

                if dIndex == 3:
                    minCol += 1
                    i = minRow
                    j = minCol


                
                dIndex = (dIndex + 1) % 4

            else:
                res.append(matrix[i][j])
                i += dxns[dIndex][0]
                j += dxns[dIndex][1]
                k += 1

        return res