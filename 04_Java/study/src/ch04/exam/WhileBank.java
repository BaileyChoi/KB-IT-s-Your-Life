package ch04.exam;

import java.util.Scanner;

public class WhileBank {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean run = true;
        int money = 0;

        while (run) {
            System.out.println("-----------------------------");
            System.out.println("1. 예금 | 2. 출금 | 3. 잔고 | 4. 종료");
            System.out.println("-----------------------------");
            System.out.print("선택> ");

            String strNum = scanner.nextLine();

            if (strNum.equals("1")) {
                System.out.print("예금액> ");
                Integer deposit = scanner.nextInt();
                scanner.nextLine();
                money += deposit;
            } else if (strNum.equals("2")) {
                System.out.print("출금액> ");
                Integer withdrawal = scanner.nextInt();
                scanner.nextLine();
                money -= withdrawal;
            } else if (strNum.equals("3")) {
                System.out.println("잔고> " + money);
            } else if (strNum.equals("4")) {
                run = false;
            }
        }
        System.out.println("프로그램 종료");
    }
}
