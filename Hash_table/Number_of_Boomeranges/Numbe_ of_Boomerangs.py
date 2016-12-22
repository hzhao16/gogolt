class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        ans = 0
        for i in range(len(points)):
            d = {}
            for j in range(len(points)):
                dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                d[dis] = d.get(dis, 0) + 1 
            for i in d.values():
                if (i > 1):
                    ans += i * (i - 1)
        return ans
        
        """ time out error
        ans = 0
        for i in range(len(points)):
            d = []
            for j in range(len(points)):
                dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                if dis in d:
                    ans += d.count(dis)
                d.append(dis)
        return ans * 2        
        """