import numpy as np
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s = (len(grid), len(grid[0]))
        table = np.zeros(s, dtype=int)
        table[0][0] = grid[0][0]
        for i in range(1, len(grid), 1):
            table[i][0] = table[i-1][0] + grid[i][0]
        for i in range(1, len(grid[0]), 1):
            table[0][i] = table[0][i-1] + grid[0][i]
        for i in range(1, len(grid), 1):
            for j in range(1, len(grid[0]), 1):
                table[i][j] = min(table[i-1][j], table[i][j-1]) + grid[i][j]
                
        return int(table[len(grid)-1][len(grid[0])-1])