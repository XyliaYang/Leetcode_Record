/**
 * 题目：机器人的运动范围
 * 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
 * 但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
 * 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
 * 
 * 
 * 思路：回溯，且同层递归时访问矩阵不能再次被访问
 */


public class Interview13 {

    public int movingCount(int threshold, int rows, int cols){
        /**
         * 从（0,0）开始可以访问m*n个网格多少个格子,且坐标数位之和不大于k.
         */
        if(rows<=0||cols<=0||threshold<=0){
            return 0;
        }   

        //  被访问记录矩阵
         boolean[][] visited=new boolean[rows][cols]; 
         for(int i=0;i<rows;i++){
             for(int j=0;j<cols;j++){
                 visited[i][j]=false;
             }
         }
        int num=visit_grid_core(rows,cols,0,0,visited,threshold);

         return num;
    }

    public int visit_grid_core(int m,int n,int row,int col,boolean[][] visited,int k){
        /**
         * 从m*n矩阵的当前row行col开始计算可以被访问的个数
         */
        int num=0;
        if ( checkVisit(m,n,row,col,visited,k)){
            visited[row][col]=true;

            num=1+visit_grid_core(m, n, row-1, col, visited, k)
            +visit_grid_core(m, n, row+1, col, visited, k)
            +visit_grid_core(m, n, row, col-1, visited, k)
            +visit_grid_core(m, n, row, col+1, visited, k);
        }
         return num;
    }

    public boolean checkVisit(int m,int n,int row,int col,boolean[][] visited,int k){
        /**
         * 是否能够访问
         */
        if(row>=0&&col>=0&&row<m&&col<n&&(getDigitSum(row)+getDigitSum(col)<=k)&&!visited[row][col]){
            return true;
        }
        return false;
    }

    public int getDigitSum(int num){
        /**
         * 计算一个数字的各个位数的数字之和
         */

         int sum=num%10;
         while(num/10>0){
             num=num/10;
             sum+=num%10;
         }
         return sum;
    }
    public static void main(String[] args) {
    }
}