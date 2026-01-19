class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        pathLength = 1

        q = deque()
        visited = set()

        if grid[0][0] == 0:
            q.append((0,0))
            visited.add((0,0))
        else:
            return -1
        
        while q:
            for i in range(len(q)):
                currCoord = q.popleft()

                # if we are at the destination
                if currCoord == (len(grid) - 1, len(grid) - 1):
                    if grid[len(grid)-1][len(grid)-1] == 0:
                        return pathLength
                    else:
                        return -1
                
                # check neighbors for possible directions
                dxns = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1),(-1,1)]
                for dr, dc in dxns:
                    nr = currCoord[0] + dr
                    nc = currCoord[1] + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid):
                        if grid[nr][nc] == 0 and (nr,nc) not in visited:
                            q.append((nr,nc))
                            visited.add((nr,nc))
                

            # done with this level, add to the pathLength
            pathLength += 1

        return -1

