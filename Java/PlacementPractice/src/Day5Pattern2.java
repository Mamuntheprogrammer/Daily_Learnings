public class Day5Pattern2 {
    public static void main(String[] args) {
//        Number pyramid

        System.out.println();

        System.out.println("Number pyramid");
        System.out.println();

        for (int i=1;i<8;i++){
            for (int j=1; j<i;j++){
                System.out.print(j+" ");
            }
            System.out.println();
        }


        System.out.println();

        System.out.println("Inverted Number pyramid");
        System.out.println();

        for (int i=1;i<8;i++){
            for (int j=1; j<8-i;j++){
                System.out.print(j+" ");
            }
            System.out.println();
        }


        System.out.println();

        System.out.println("Floy'd triangle ");
        System.out.println();

        int number = 1;
        for (int i=1;i<8;i++){
            for (int j=1; j<i;j++){
                System.out.print(number+" ");
                number++;
            }
            System.out.println();
        }
    }
}
