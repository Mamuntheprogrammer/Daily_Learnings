public class Day5Patterns {
    public static void main(String[] args) {

        System.out.println("Printing Rectangle Pattern ");
        System.out.println();
//        Rectangle pattern
        for (int i=0;i<5;i++){
            for (int j=0;j<6;j++){
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println();

        System.out.println("Printing Hollow Rectangle");
        System.out.println();

//        Hollow Rectangle

        for (int i = 0; i<5;i++){
            for (int j=0;j<6;j++){
                if (i==0||j==0||i==4||j==5){
                    System.out.print("*");
                }else {
                    System.out.print(" ");
                }
            }
            System.out.println();

        }

        System.out.println();

        System.out.println("Printing Pyramid");
        System.out.println();

for (int i =0;i<8;i++){
    for (int j=0;j<i;j++){
        System.out.print("*");
    }
    System.out.println();
}




        System.out.println();

        System.out.println("Printing Inverted Pyramid");
        System.out.println();

        for (int i =0;i<8;i++){
            for (int j=0;j<8-i;j++){
                System.out.print("*");
            }
            System.out.println();
        }

        System.out.println();

        System.out.println("Printing Inverted 180* Pyramid");
        System.out.println();

        for(int i=0;i<8;i++){
            for (int j=0;j<8-i;j++){
                System.out.print(" ");
            }
            for (int j=0;j<i;j++){
                System.out.print("*");
            }
            System.out.println();

        }



    }
}
