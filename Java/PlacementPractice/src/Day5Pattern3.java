public class Day5Pattern3 {
    public static void main(String[] args) {
//        0 - 1 TRIANGLE

        for (int i=1;i<8;i++){
            for (int j =1;j<i;j++){
                if ((i+j)%2==0) System.out.print(1);else System.out.print(0);
            }
            System.out.println();
        }
    }
}
