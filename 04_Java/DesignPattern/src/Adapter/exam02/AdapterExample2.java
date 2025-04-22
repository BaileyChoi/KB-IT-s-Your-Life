package Adapter.exam02;

public class AdapterExample2 {   // 상속
    public static void main(String[] args) {
        Print p = new PrintBanner("Hello");
        p.printWeak();
        p.printStrong();

        print(new PrintBanner("Hello Banner!"));

        print(new PrintBanner(new Banner("Hello Banner Banner!")));
    }

    // 고정된 사용자측 코드
    public static void print(Print p) {
        p.printWeak();
        p.printStrong();
    }
}
