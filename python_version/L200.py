# @Time : 2020/3/27 8:54
# @Author : Xylia_Yang
# @Description :

class Solution:
    def numIslands(self, grid) :
        if not grid:
            return 0

        rows=len(grid)
        cols=len(grid[0])

        sum=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    sum+=1
                    self.dfs(grid,rows,cols,i,j)

        return  sum

    def dfs(self,grid,rows,cols,i,j):
        if i<rows and i>=0 and j<cols and j>=0 and  grid[i][j]=="1":
            grid[i][j]="0"

            self.dfs(grid,rows,cols,i+1,j)
            self.dfs(grid,rows,cols,i,j+1)
            self.dfs(grid, rows, cols, i - 1, j)
            self.dfs(grid, rows, cols, i, j -1)

        return

if __name__=='__main__':
    solution=Solution()
    t_grid=[["1","0","1","1","0","1","1"]]
    print(solution.numIslands(t_grid))


