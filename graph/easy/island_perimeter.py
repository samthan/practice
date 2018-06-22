# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 
# represents water. Grid cells are connected horizontally/vertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island 
# (i.e., one or more connected land cells). 
# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
# Determine the perimeter of the island.

# This screams dfs/bfs traversal, but it's pretty straighforward without it.  DFS/BFS saves on the
# number of nodes you have to hit

def islandPerimeter(self, grid):
        
    def getNeighbors(i, j):
        n = 0
        if i - 1 >= 0 and grid[i - 1][j]:
            n += 1
        if j - 1 >= 0 and grid[i][j - 1]:
            n += 1
        if j + 1 < len(grid[0]) and grid[i][j + 1]:
            n += 1
        if i + 1 < len(grid) and grid[i + 1][j]:
            n += 1
        return n
    
    # straightforward approach: search the entire matrix, add 4 - #neighbors to result, return result
    def brute(grid):
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    n = getNeighbors(i, j)
                    res += (4 - n)

        return res
    
    return brute(grid)