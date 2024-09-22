import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        printData(n);
    }

    public static void printData(int n) {
        for (int i = 0; i < n; i++) {
            boolean isFirst = true;
            for (int j = 0; j < n; j++) {
                int num = (((i) * n + (j + 1)) % 9);
                if (isFirst) {
                    System.out.printf("%d", num == 0 ? 9 : num);
                    isFirst = false;
                } else {
                    System.out.printf(" %d", num == 0 ? 9 : num);
                }
            }
            System.out.printf("\n");
        }
    }
}