package Adapter.exam01;

public class AdapterExample {   // 상속
    public static void main(String[] args) {
        Print p = new PrintBanner("Hello");
        p.printWeak();
        p.printStrong();

        print(new PrintBanner("Hello Banner!"));
    }

    // 고정된 사용자측 코드
    public static void print(Print p) {
        p.printWeak();
        p.printStrong();
    }
}
