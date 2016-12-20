class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                num = int(num1[i]) * int(num2[j])
                position1 = i + j
                position2 = i + j + 1
                s = num + ans[position2]
                ans[position1] += s/10 
                ans[position2] = s%10
        index = next((i for i, x in enumerate(ans) if x), None)
        if (index == None): return "0"
        re = ''.join(str(e) for e in ans[index:])
        return re