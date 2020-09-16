public class L338 {

    public int[] countBits(int num) {
        if(num==0){
            return  new int[]{0};
        }

        int[] numBits=new int[num+1];

        numBits[0]=0;
        numBits[1]=1;

        for(int i=2;i<=num;i++){
            if((i&1)==1){
                numBits[i]=numBits[i-1]+1;
            }else{
                numBits[i]=numBits[i/2];
            }
        }
        return numBits;
    }
}
