package Template_Method;

public class Main {
    public static void main(String[] args) {
        AbstractDisplay d1 = new CharDisplay('B');
        AbstractDisplay d2 = new StringDisplay("Hello, Bingbong!");

        d1.display();
        d2.display();
    }
}
