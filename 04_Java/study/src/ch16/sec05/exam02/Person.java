package ch16.sec05.exam02;

public class Person {
    public void ordering(Comparable comparable) {
        String a = "홍";
        String b = "김";

        int result = comparable.compare(a, b);

        if (result < 0) {
            System.out.println(a + "은 " + b + "보다 앞에 옴");
        } else if (result == 0) {
            System.out.println(a + "은 " + b + "과 같음");
        } else {
            System.out.println(a + "은 " + b + "보다 뒤에 옴");
        }
    }
}
