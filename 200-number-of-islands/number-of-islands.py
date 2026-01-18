class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visit(grid: List[List[str]], r: int, c: int):
            if grid[r][c] != '1':
                return

            grid[r][c] = '0'
            
            dxns = [(-1,0), (1,0), (0,1), (0,-1)]
            for dR,dC in dxns:
                newRow = r + dR
                newCol = c + dC

                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
                    visit(grid, newRow, newCol)

        numIslands = 0
        rows = len(grid)
        cols = len(grid[0])

        # for every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    numIslands += 1
                    visit(grid, r, c)

        return numIslands








































        # def dfs(row: int, col: int):
        #     if grid[row][col] != "1":
        #         return
            
        #     # print("marking node as visited",row,col)
        #     grid[row][col] = "-1" # mark as visited
        #     # print(grid)
        #     dxns = [(1,0),(-1,0),(0,1),(0,-1)]

        #     for d in dxns:
        #         nr = d[0] + row
        #         nc = d[1] + col
        #         if 0 <= nc < len(grid[0]) and 0 <= nr < len(grid):
        #             dfs(nr, nc)

        # numIslands = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         # print(i,j)
        #         if grid[i][j] == "1":
        #             # print("found a 1")
        #             numIslands += 1
        #             dfs(i,j)
        
        # # do bfs or dfs for every node in grid, and then mark as visited by changing in place

        # # num islands is the number of times we have to run a new dfs on an unvisited 1

        
        
        # return numIslands
