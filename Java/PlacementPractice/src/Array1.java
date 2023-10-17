import java.util.Scanner;

public class Array1 {



    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int row = scan.nextInt();
        int col = scan.nextInt();

  int[][] mat = new int[row][col];

  for(int i =0;i<row;i++){
      for (int j = 0;j<col;j++){
          mat[i][j] = scan.nextInt();
      }
  }
        for(int i =0;i<row;i++){
            for (int j = 0;j<col;j++){
                System.out.print(mat[i][j]);
            }
            System.out.println();
        }
    }
}
