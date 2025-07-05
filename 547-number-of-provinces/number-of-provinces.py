class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if par[x] != x:
                par[x] = find(par[x])  # Path compression
            return par[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # already connected
            if rank[rootX] > rank[rootY]:
                par[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                par[rootX] = rootY
            else:
                par[rootY] = rootX
                rank[rootX] += 1
            return True

        numCities = len(isConnected)
        par = [i for i in range(numCities)]
        rank = [1] * numCities
        numProvinces = numCities

        for i in range(numCities):
            for j in range(i + 1, numCities):  # Avoid duplicate edges and self-connections
                if isConnected[i][j] == 1:
                    if union(i, j):
                        numProvinces -= 1

        return numProvinces


