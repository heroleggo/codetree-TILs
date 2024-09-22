import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        printStr(n);
    }

    public static void printStr(int cnt) {
        for (int i = 0; i < cnt; i++) {
            System.out.println("12345^&*()_");
        }
    }
}