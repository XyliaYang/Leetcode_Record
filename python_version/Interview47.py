# @Time : 2020/3/11 10:17
# @Author : Xylia_Yang
# @Description :


class Solution_1(object):
    def getMaxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return

        rows=len(grid)
        cols=len(grid[0])

        maxValues=[[None]*cols for i in range(rows)]
        maxValues[0][0]=grid[0][0]

        return self.getMaxValueatIndex(grid,rows,cols,rows-1,cols-1,maxValues)

    def  getMaxValueatIndex(self,grid,rows,cols,row,col,maxValues):
        if  maxValues[row][col]:
            return maxValues[row][col]

        if row==0:
            return self.getMaxValueatIndex(grid,rows,cols,row,col-1,maxValues)+grid[row][col]
        if col==0:
            return self.getMaxValueatIndex(grid,rows,cols,row-1,col,maxValues)+grid[row][col]


        if not maxValues[row-1][col]:
            top=self.getMaxValueatIndex(grid,rows,cols,row-1,col,maxValues)
        if not  maxValues[row][col-1]:
            left=self.getMaxValueatIndex(grid,rows,cols,row,col-1,maxValues)

        return max(top,left)+grid[row][col]




if __name__=='__main__':
    solution=Solution_1()
    grid=[[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]
    print(solution.getMaxValue(grid))