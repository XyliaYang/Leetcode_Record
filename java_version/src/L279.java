public class L279 {

    public int numSquares(int n) {
        if(n<1){
            return 0;
        }
        int r= (int) Math.sqrt(n);
        if(r*r==n){
            return 1;
        }

        int[] dp=new int[n+1];
        for(int i=0;i<n+1;i++){
            dp[i]=i;
        }

        for(int i=1;i<=n;i++){
            r= (int) Math.sqrt(i);
            if(r*r==i){
                dp[i]=1;
            }
            else{
                for(int j=1;j<=Math.sqrt(i);j++){
                    dp[i]=Math.min(dp[i],dp[i-(int)Math.pow(j,2)]+1);
                }
            }
        }

        return dp[n];
    }
}
