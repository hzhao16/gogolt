#453 Minimum Moves to Equal Array Elements

'''Given a non-empty integer array of size n, 
find the minimum number of moves required to make all array elements equal, 
where a move is incrementing n - 1 elements by 1.'''

'''Adding 1 to n-1 elements is equal to dropping 1 to the max number until it equals to the min.'''

def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)- min(nums)*len(nums)