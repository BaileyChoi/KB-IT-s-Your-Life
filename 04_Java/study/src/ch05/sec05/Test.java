package ch05.sec05;

import java.util.Random;

public class Test {
    int a;  //필드
    static int b;

    public static void main(String[] args) {
        int a = 100;
        System.out.println("a = " + a);

        System.out.println("필드 b = " + b);
        System.out.println("필드 a = " + new Test().a);

        double rand = Math.random();
        System.out.println("rand = " + rand);

        double rand2 = new Random().nextDouble();
        System.out.println("rand2 = " + rand2);

        int num1 = 0, num2 = 0;
        boolean result;

        result = ((num1 += 10) < 0 && (num2 += 10) > 0);
        System.out.println("result = " + result);
        System.out.println("num1 = " + num1 + " num2 = " + num2);
        System.out.println();

        result = ((num1 += 10) > 0 || (num2 += 10) > 0);
        System.out.println("result = " + result);
        System.out.println("num1 = " + num1 + " num2 = " + num2);
        System.out.println();
    }
}
