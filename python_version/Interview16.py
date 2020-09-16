class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        assert x==0 and n<0,"invalid input" #严格异常值处理，但在leetcode中会判不通过
        if n==0:
            return 0
        elif n<0:
            unsign_n=-n
            return 1/self.myUnsignPow(x,unsign_n)
        else:
            return self.myUnsignPow(x,n)

    def  myUnsignPow(self,x,n):
        result=1
        for i in range(n):
            result*=x
        return result







