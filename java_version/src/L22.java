import java.util.ArrayList;
import java.util.List;


public class L22 {

    public List<String> generateParenthesis(int n) {
        List<String> res=new ArrayList<>();

        if(n==0)
            return res;

        dfs("",n,n,res);
        return  res;

    }

    private void dfs(String curStr, int leftN, int rightN, List<String> res){

        if(leftN==0 && rightN==0){
            res.add(curStr);
            return;
        }

        if(leftN>0){
            dfs(curStr+"(",leftN-1,rightN,res);
        }
        if(rightN>leftN){
            dfs(curStr+")",leftN,rightN-1,res);
        }

    }
}