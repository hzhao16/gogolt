#118 Pascal's triangle
'''
Given numRows, generate the first numRows of Pascal's triangle.
'''

''' row[i] = (row[i-1]+[0]) + ([0]+row[i-1])
'''

# map
def generate(numRows):
	if numRows==0:
        return []
    t = [[1]]
    for i in range(1,numRows):
        t.append([i for i in map(lambda x, y: x+y, t[-1] + [0], [0] + t[-1])])
    return t


# zip
def generate1(numRows):
	if numRows==0:
        return []
    t = [[1]]
    for i in range(numRows):
        t.append([i+j for i,j in zip(t[-1] + [0], [0] + t[-1])])
    return t
