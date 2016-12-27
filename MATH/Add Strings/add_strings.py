class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        i, j, c= 0, 0, 0
        ans = ""
        while (i < len(num1) or j < len(num2) or c != 0):
            if (i == len(num1) and j == len(num2)):
                ans += str(c)
                break
            elif (i == len(num1)):
                tem = c + int(num2[j])
                ans += str(tem%10)
                c = tem / 10
                j += 1
                continue
            elif (j == len(num2)):
                tem = c + int(num1[i])
                ans += str(tem%10)
                c = tem / 10   
                i += 1
                continue
            tem = int(num1[i]) + int(num2[j]) + c
            ans += str(tem%10)
            c = tem/10
            i += 1
            j += 1
        ans = ans[::-1]
        return ans