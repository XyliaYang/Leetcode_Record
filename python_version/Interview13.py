# @Time : 2020/3/21 11:40
# @Author : Xylia_Yang
# @Description :

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold<=0 or rows<=0 or cols<=0:
            return 0

        visited=[[False]*cols  for _ in range(rows)]
        num=self.visitCore(rows,cols,0,0,visited,threshold)

        return num

    def visitCore(self,rows,cols,row,col,visited,threshold):
        num=0

        if self.checkVisited(rows,cols,row,col,visited,threshold):
            visited[row][col]=True


            num=1+self.visitCore(rows,cols,row-1,col,visited,threshold) \
            +self.visitCore(rows,cols,row+1,col,visited,threshold) \
            +self.visitCore(rows,cols,row,col-1,visited,threshold) \
            +self.visitCore(rows,cols,row,col+1,visited,threshold)


        return num

    def checkVisited(self,rows,cols,row,col,visited,threshold):
        if col<cols and row<rows and not visited[row][col] and self.getNumSum(row,col)<=threshold:
            return True
        return False

    def getNumSum(self,row,col):
        sum=0
        while row:
            sum+=row%10
            row/=10

        while col:
            sum+=col%10
            col/=10

        return sum





if __name__=='__main__':
    solution=Solution()
    print(solution.movingCount(10,3,4))
