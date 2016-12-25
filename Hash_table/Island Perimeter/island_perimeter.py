import numpy as np
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l = 0
        num_table = grid
        l1 = len(num_table)
        l2 = len(num_table[0])
        for j in range(l1):
            for i in range(l2):
                if (num_table[j][i] == 0):
                    continue
                l += 4
                if ((num_table[j][i] != 0) and (i < len(num_table[0]) - 1) and (num_table[j][i+1] != 0)):
                    l -= 2
                if ((num_table[j][i] != 0) and j >= 1 and (num_table[j-1][i] != 0)):
                    l -= 2
        return l        
        """#slow version
        num_table = np.asarray(grid)
        num_table[num_table != 0] *= 4
        for j in range(len(num_table)):
            for i in range(len(num_table[0])):
                if ((num_table[j][i] != 0) and (i < len(num_table[0]) - 1) and (num_table[j][i+1] != 0)):
                    num_table[j][i] -= 1
                    num_table[j][i+1] -= 1
                if ((num_table[j][i] != 0) and j >= 1 and (num_table[j-1][i] != 0)):
                    num_table[j-1][i] -= 1
                    num_table[j][i] -= 1
        l = sum(sum(x) for x in num_table.tolist())
        return l
        """