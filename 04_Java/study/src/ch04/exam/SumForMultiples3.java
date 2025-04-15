package ch04.exam;

public class SumForMultiples3 {
    public static void main(String[] args) {
        int sum = 0;

        for (int i = 3; i <= 100; i = i + 3) {
            sum += i;
        }

        System.out.println("1~100 3의 배수의 합 : " + sum);
    }
}
