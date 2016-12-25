import numpy as np
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        if len(grid) == 0:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == '1'):
                    self.dfsgrid(grid, i, j)
                    ans += 1
        return ans
        
    def dfsgrid(self, grid, i, j):
        grid[i][j] = '0'
        if (i > 0 and grid[i-1][j] == '1'): self.dfsgrid(grid, i-1, j)
        if (i + 1 < len(grid) and grid[i+1][j] == '1'): self.dfsgrid(grid, i+1, j)
        if (j > 0 and grid[i][j-1] == '1'): self.dfsgrid(grid, i, j-1)
        if (j + 1 < len(grid[0]) and grid[i][j+1] == '1'): self.dfsgrid(grid, i, j+1)