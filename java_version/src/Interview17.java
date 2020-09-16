//Interview17
public  class Interview17 {

    public void PrintToMaxOfDigits(int n){
        if(n<=0){
            return ;
        }

        char[] numOfStr=new char[n];
//        初始化为全0
        for(int i=0;i<n;i++){
            numOfStr[i]='0';
        }
        

        while(addOne(numOfStr)){  
            printNumofStr(numOfStr);
        }

    }

    /**
     * 模拟字符串+1：从后到前逐个计算置换，注意溢出处理
     * @param numOfStr
     * @return
     */
    public boolean addOne(char[] numOfStr){
        boolean isOver=false; 
        int n=numOfStr.length;
//        进位标志
        int carryBit=0;
//        该位的数字
        int nSum;
        

        for(int i=n-1;i>=0;i--){
            nSum=numOfStr[i]-'0';
            nSum+=carryBit;

            if(i==n-1){
                nSum+=1;
            }
            if(nSum<10){
                numOfStr[i]=(char)(nSum+'0');
                carryBit=0;
                break;
            }
            else{
                if(i==0){
                    isOver=true;
                    break;
                }
                nSum-=10;
                numOfStr[i]='0';
                carryBit=1;
            }
        }
        return !isOver;
    }

    /**
     * 输出字符串形式的数字：当遇到第一个非0数字就将后面的数字全部输出
     * @param numOfStr
     */
    public void printNumofStr(char[] numOfStr){
        int n=numOfStr.length;
        boolean startPrint=false;

        for(int i=0;i<n;i++){
            if(numOfStr[i]!='0'&&!startPrint){
                startPrint=true;
            }
            if(startPrint){
                System.out.print(numOfStr[i]);
            }
        }
        System.out.println();
    }
    public  static void main(String[] args) {
        Interview17 interview17=new Interview17();
        interview17.PrintToMaxOfDigits(5);

    }
}