#119 Pascal's Triangle II
'''
Given an index k, return the kth row of the Pascal's triangle.
'''
# zip
def getRow(self, rowIndex):
	t = [1]
	for i in range(1,rowIndex):
		t = [x+y for x,y in zip(t+[0],[0]+t)]
	return t