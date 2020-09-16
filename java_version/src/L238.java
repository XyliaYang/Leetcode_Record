public class L238 {

    public int[] productExceptSelf(int[] nums) {
        int[] res=new int[nums.length];
        int p=1;
        int q=1;

        for(int i=0;i<nums.length;i++){
            res[i]=p;
            p*=nums[i];
        }
        for (int i=nums.length-1;i>=0;i--){
            res[i]*=q;
            q*=nums[i];
        }
        return res;
    }

    public static void main(String[] args) {
        L238 test=new L238();
        int[] res=test.productExceptSelf(new int[]{1,2,3,4});

        System.out.println(res);


    }
}
