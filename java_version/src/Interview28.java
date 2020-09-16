import java.util.ArrayList;
import java.util.List;

public class Interview28{
    public List<Integer> spiralOrder(int[][] matrix) {
        int index = 0;
        int rows = matrix.length;
        int cols = matrix[0].length;
        List<Integer> elements =new ArrayList<Integer>();

        while (rows > index * 2 && cols > index * 2) {
            getMatrixInCircle(matrix, rows,cols,index, elements);
        }
        return elements;
    }

    void  getMatrixInCircle(int[][] matrix,int rows,int cols,int index,List<Integer> elements){
        int row_index=index;
        int col_index=index;

        for(int col=index;col<cols-index;col++){
            elements.add(matrix[index][col]);
            row_index=index;
            col_index=col;
        }
        for (int row=row_index+1;row<rows-row_index;row++){
            elements.add(matrix[row][col_index]);
            row_index=row;
        }
        for(int col=col_index;col>cols-col_index;col--){
            elements.add(matrix[row_index][col]);
            col_index=col;
        }
        for (int row=row_index-1;row>rows-row_index-1;row--){
            elements.add(matrix[row][col_index]);
        }

    }
}
