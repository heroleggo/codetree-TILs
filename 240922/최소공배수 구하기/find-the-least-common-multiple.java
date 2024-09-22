import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println(a * b / getGCD(a, b));
    }

    public static int getGCD(int a, int b) {
        if (a == b) {
            return a;
        }
        int c, d;

        if (a > b) {
            c = a;
            d = b;
        } else {
            c = b;
            d = a;
        }

        int tmp;
        while (d != 0) {
            tmp = c % d;
            c = d;
            d = tmp;
        }

        return c;
    }
}