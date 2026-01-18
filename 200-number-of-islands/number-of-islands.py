class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        numIslands = 0

        # BFS solution
        def bfs(r:int, c:int):
            # bfs algo
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                currentLevel = []
                for i in range(len(q)):
                    currentRow, currentCol = q.popleft()

                    directions = [(1,0), (-1,0), (0,1), (0,-1)]
                    for dR, dC in directions:
                        newRow = currentRow + dR
                        newCol = currentCol + dC

                        if (0 <= newRow < rows and 
                        0 <= newCol < cols and
                        grid[newRow][newCol] == '1' and
                        (newRow, newCol) not in visited):
                            q.append((newRow, newCol))
                            visited.add((newRow, newCol))

                        




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    # visit and fill in neighbors
                    bfs(r,c)
                    numIslands += 1
        
        return numIslands





        
            



        # # DFS SOLUTION
        # def visit(grid: List[List[str]], r: int, c: int):
        #     if grid[r][c] != '1':
        #         return

        #     grid[r][c] = '0'
            
        #     dxns = [(-1,0), (1,0), (0,1), (0,-1)]
        #     for dR,dC in dxns:
        #         newRow = r + dR
        #         newCol = c + dC

        #         if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]):
        #             visit(grid, newRow, newCol)

        # numIslands = 0
        # rows = len(grid)
        # cols = len(grid[0])

        # # for every cell in the grid
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == '1':
        #             numIslands += 1
        #             visit(grid, r, c)

        # return numIslands







































