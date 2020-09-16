
/**
 *
 题目：矩阵中的路径
 题：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
 如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。

 思路：
 回溯法->递归


 */
public class Interview12{

    public boolean hasPath(char[][] matrix,char[] str){
        /**
         * 判断matrix矩阵中是否存在字符串str.
         */
        if(matrix ==null || str ==null){
            return false;
        }

        int rows=matrix.length;
        int cols=matrix.length;

        int pathLength=0;
        // 定义一个访问数组表明matrix数组相应位置有没有被访问过
        boolean[][] visited=new boolean[rows][cols];
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                visited[i][j]=false;
            }
        }

        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(hasPathCore(matrix,rows,cols,i,j,visited,str,pathLength)){
                    return true;
                }

            }
        }
        return false;
    }


    public boolean hasPathCore(char[][] matrix,int rows,int cols,int row,int col,boolean[][] visited,char[] str,int pathLength){
        /**
         * 从matrix矩阵开始寻找，是否存在路径str的第pathLength个元素的匹配路径.
         */
        // 匹配成功
        if(pathLength>=str.length){
            return true;
        }
        // 递归终止条件
        if(row<0||row>=rows||col<0||col>=cols||visited[row][col]==true||str[pathLength]!=matrix[row][col]){
            return false;
        }

        visited[row][col]=true;
        // 上下左右存在路径
        if (hasPathCore(matrix, rows, cols, row-1, col, visited, str, pathLength+1)||
                hasPathCore(matrix, rows, cols, row+1, col, visited, str, pathLength+1)||
                hasPathCore(matrix, rows, cols, row, col-1, visited, str, pathLength+1)||
                hasPathCore(matrix, rows, cols, row, col+1, visited, str, pathLength+1)
        ){
            return true;
        }

        // 到此说明不存在路径
        visited[row][col]=false;
        return false;
    }

    public static void main(String[] args) {
        char[][] matrix={{'a','b','t','g'},{'c','f','c','s'},{'j','d','e','h'}};
        char[] str={'a','b','f','b'};

        Interview12 interview12=new Interview12();
        boolean has_path=interview12.hasPath(matrix, str);

        System.out.println(has_path);
    }
}