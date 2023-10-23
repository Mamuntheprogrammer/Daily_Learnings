public class Practice{
    public static void main(String[] arg){
        // Reverse a strint
        StringBuilder sb = new StringBuilder("I Hate working here");

        for(int i=0; i<sb.length()/2;i++){
            int front = i;
            int back = sb.length()-1-i;

            char fronCha = sb.charAt(front);
            char backCha = sb.charAt(back);

            sb.setCharAt(front, backCha);
            sb.setCharAt(back, fronCha);
        }

        System.out.println(sb);


    }
}
