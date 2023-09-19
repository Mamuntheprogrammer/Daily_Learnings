import java.util.Stack;

public class BuiltinStack {
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();

        s.push(25);
        s.push(23);
        s.push(12);
        System.out.println(s.peek());
    }
}
