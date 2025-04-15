package ch04.sec02;

public class IfExample {
    public static void main(String[] args) {
        int score = 53;

        if (score >= 90) {
            System.out.println("점수가 90보다 큼");
            System.out.println("등급: A");
        }

        if (score < 90) {
            System.out.println("점수가 90보다 작음");
            System.out.println("등급: B");
        }
    }
}
